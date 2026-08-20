import os
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from backend.app.utils.pdf_processor import extract_text_from_pdf
from backend.app.rag.chunker import chunk_text


router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    try:
        file_content = await file.read()

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(file_content)
            temp_file_path = temp_file.name

        text = extract_text_from_pdf(temp_file_path)
        chunks = chunk_text(text)

        os.remove(temp_file_path)

        return {
    "filename": file.filename,
    "characters": len(text),
    "number_of_chunks": len(chunks),
    "first_chunk_preview": chunks[0] if chunks else ""
}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF processing failed: {str(e)}"
        )