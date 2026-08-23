from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.pdf_api import router as pdf_router


app = FastAPI(
    title="Research Gap Finder API",
    description="AI-powered system for identifying research gaps from research papers.",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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