import os
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.app.utils.pdf_processor import extract_text_from_pdf
from backend.app.rag.chunker import chunk_text
from backend.app.rag.retriever import Retriever
from backend.app.rag.analyzer import analyze_paper
from backend.app.services.gap_analyzer import compare_papers
from backend.app.services.gap_scorer import score_research_gap
from backend.app.services.evidence_mapper import map_gap_evidence
from backend.app.llm.groq_client import generate_answer


router = APIRouter()


# ============================================================
# SINGLE PDF UPLOAD
# ============================================================

@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    temp_file_path = None

    try:

        file_content = await file.read()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(file_content)
            temp_file_path = temp_file.name

        text = extract_text_from_pdf(
            temp_file_path
        )

        chunks = chunk_text(text)

        return {
            "filename": file.filename,
            "characters": len(text),
            "number_of_chunks": len(chunks),
            "first_chunk_preview": (
                chunks[0]
                if chunks
                else ""
            )
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"PDF processing failed: {str(e)}"
        )

    finally:

        if (
            temp_file_path
            and os.path.exists(temp_file_path)
        ):
            os.remove(temp_file_path)


# ============================================================
# MULTIPLE PDF RESEARCH GAP ANALYSIS
# ============================================================

@router.post("/analyze-papers")
async def analyze_papers(
    files: list[UploadFile] = File(
        ...,
        description="Upload 2 or more research paper PDF files"
    )
):

    # --------------------------------------------------------
    # CHECK NUMBER OF FILES
    # --------------------------------------------------------

    if len(files) < 2:

        raise HTTPException(
            status_code=400,
            detail="At least two PDF files are required."
        )

    # --------------------------------------------------------
    # CHECK FILE TYPES
    # --------------------------------------------------------

    for file in files:

        if not file.filename.lower().endswith(".pdf"):

            raise HTTPException(
                status_code=400,
                detail=f"{file.filename} is not a PDF file."
            )

    analyses = []

    try:

        # ====================================================
        # PROCESS EACH PAPER
        # ====================================================

        for paper_number, file in enumerate(
            files,
            start=1
        ):

            print("\n")
            print("=" * 60)
            print(
                f"PROCESSING PAPER {paper_number}: "
                f"{file.filename}"
            )
            print("=" * 60)

            temp_file_path = None

            try:

                # --------------------------------------------
                # READ PDF
                # --------------------------------------------

                file_content = await file.read()

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_file:

                    temp_file.write(file_content)

                    temp_file_path = temp_file.name

                # --------------------------------------------
                # EXTRACT TEXT
                # --------------------------------------------

                text = extract_text_from_pdf(
                    temp_file_path
                )

                print(
                    "Characters:",
                    len(text)
                )

                # --------------------------------------------
                # CHUNK TEXT
                # --------------------------------------------

                chunks = chunk_text(text)

                print(
                    "Chunks:",
                    len(chunks)
                )

                if not chunks:

                    continue

                # --------------------------------------------
                # CREATE RETRIEVER
                # --------------------------------------------

                retriever = Retriever(
                    chunks
                )

                # --------------------------------------------
                # RESEARCH QUERIES
                # --------------------------------------------

                queries = [

                    "research problem and objectives",

                    "methodology and experimental approach",

                    "key findings and results",

                    "limitations of the study",

                    "future work and research directions"

                ]

                retrieved_chunks = []

                # --------------------------------------------
                # RETRIEVE RELEVANT CHUNKS
                # --------------------------------------------

                for query in queries:

                    results = retriever.retrieve(
                        query,
                        top_k=2
                    )

                    for result in results:

                        if (
                            result["text"]
                            not in retrieved_chunks
                        ):

                            retrieved_chunks.append(
                                result["text"]
                            )

                print(
                    "Relevant chunks retrieved:",
                    len(retrieved_chunks)
                )

                # --------------------------------------------
                # PREPARE TEXT
                # --------------------------------------------

                selected_text = "\n\n".join(
                    retrieved_chunks
                )

                print(
                    "Selected text length:",
                    len(selected_text)
                )

                # --------------------------------------------
                # LLM ANALYSIS
                # --------------------------------------------

                print(
                    "Sending relevant chunks to LLM..."
                )

                analysis = analyze_paper(
                    selected_text
                )

                analyses.append({

                    "filename": file.filename,

                    "analysis": analysis

                })

                print(
                    f"Paper {paper_number} analysis complete."
                )

            finally:

                if (
                    temp_file_path
                    and os.path.exists(temp_file_path)
                ):

                    os.remove(
                        temp_file_path
                    )

        # ====================================================
        # CHECK ANALYSES
        # ====================================================

        if len(analyses) < 2:

            raise HTTPException(
                status_code=400,
                detail=(
                    "At least two papers must "
                    "contain readable text."
                )
            )

        # ====================================================
        # CROSS-PAPER ANALYSIS
        # ====================================================

        print("\n")
        print("=" * 60)
        print("CROSS-PAPER ANALYSIS")
        print("=" * 60)

        analysis_texts = [

            item["analysis"]

            for item in analyses

        ]

        comparison = compare_papers(
            analysis_texts
        )

        # ====================================================
        # CANDIDATE RESEARCH GAP
        # ====================================================

        print("\n")
        print("=" * 60)
        print("CANDIDATE RESEARCH GAP")
        print("=" * 60)

        gap_prompt = f"""
From the following cross-paper analysis,
identify ONE strongest potential research gap.

Return ONLY the research gap statement.

Use ONLY the information provided.
Do not invent facts.

Cross-Paper Analysis:
{comparison}
"""

        candidate_gap = generate_answer(
            gap_prompt
        )

        print(candidate_gap)

        # ====================================================
        # GAP SCORE
        # ====================================================

        print("\n")
        print("=" * 60)
        print("GAP SCORE")
        print("=" * 60)

        gap_score = score_research_gap(
            candidate_gap,
            analysis_texts
        )

        print(gap_score)

        # ====================================================
        # EVIDENCE MAPPING
        # ====================================================

        print("\n")
        print("=" * 60)
        print("EVIDENCE MAPPING")
        print("=" * 60)

        evidence = map_gap_evidence(
            candidate_gap,
            analysis_texts
        )

        print(evidence)

        # ====================================================
        # FINAL RESPONSE
        # ====================================================

        return {

            "papers_analyzed": len(analyses),

            "paper_analyses": analyses,

            "cross_paper_analysis": comparison,

            "research_gap": candidate_gap,

            "gap_score": gap_score,

            "evidence": evidence

        }

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=(
                "Research gap analysis failed: "
                f"{str(e)}"
            )
        )