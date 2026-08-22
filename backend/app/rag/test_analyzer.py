from backend.app.utils.pdf_processor import extract_text_from_pdf
from backend.app.rag.chunker import chunk_text
from backend.app.rag.analyzer import analyze_paper
from backend.app.services.gap_analyzer import compare_papers
from backend.app.services.gap_scorer import score_research_gap
from backend.app.services.evidence_mapper import map_gap_evidence
from backend.app.llm.groq_client import generate_answer


# ==========================================
# PDF FILES
# ==========================================

pdf_files = [
    "data/papers/paper1.pdf",
    "data/papers/paper2.pdf",
    "data/papers/paper3.pdf"
]


analyses = []


# ==========================================
# STEP 1: ANALYZE ALL PAPERS
# ==========================================

for i, pdf_path in enumerate(pdf_files, start=1):

    print("\n")
    print("=" * 60)
    print(f"ANALYZING PAPER {i}")
    print("=" * 60)

    # Extract PDF text
    text = extract_text_from_pdf(pdf_path)

    print("Characters:", len(text))

    # Create chunks
    chunks = chunk_text(text)

    print("Chunks:", len(chunks))

    # Use first 5 chunks for analysis
    selected_text = "\n\n".join(chunks[:5])

    print("Selected text length:", len(selected_text))
    print("Sending paper to LLM...")

    # Analyze paper
    analysis = analyze_paper(selected_text)

    analyses.append(analysis)

    print("\nPaper Analysis:")
    print("-" * 60)
    print(analysis)


# ==========================================
# STEP 2: CROSS-PAPER COMPARISON
# ==========================================

print("\n")
print("=" * 60)
print("CROSS-PAPER ANALYSIS")
print("=" * 60)

comparison = compare_papers(analyses)

print(comparison)


# ==========================================
# STEP 3: CANDIDATE RESEARCH GAP
# ==========================================

gap_prompt = f"""
From the following cross-paper analysis,
identify ONE strongest potential research gap.

Return ONLY the research gap statement.

Use ONLY the information provided.
Do not invent facts.

Cross-Paper Analysis:
{comparison}
"""

print("\n")
print("=" * 60)
print("CANDIDATE RESEARCH GAP")
print("=" * 60)

candidate_gap = generate_answer(gap_prompt)

print(candidate_gap)


# ==========================================
# STEP 4: GAP SCORE
# ==========================================

print("\n")
print("=" * 60)
print("GAP SCORE")
print("=" * 60)

gap_score = score_research_gap(
    candidate_gap,
    analyses
)

print(gap_score)


# ==========================================
# STEP 5: EVIDENCE MAPPING
# ==========================================

print("\n")
print("=" * 60)
print("EVIDENCE MAPPING")
print("=" * 60)

evidence = map_gap_evidence(
    candidate_gap,
    analyses
)

print(evidence)


# ==========================================
# FINAL STATUS
# ==========================================

print("\n")
print("=" * 60)
print("RESEARCH GAP FINDER PIPELINE COMPLETE")
print("=" * 60)

print("Papers analyzed:", len(analyses))
print("Comparison: SUCCESS")
print("Candidate gap: SUCCESS")
print("Gap scoring: SUCCESS")
print("Evidence mapping: SUCCESS")