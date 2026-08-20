from fastapi import FastAPI

from backend.app.api.pdf_api import router as pdf_router


app = FastAPI(
    title="Research Gap Finder API",
    description="AI-powered system for identifying research gaps from research papers.",
    version="1.0.0"
)

app.include_router(
    pdf_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Research Gap Finder API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }