# 🔬 Research Gap Finder

An AI-powered research assistant that analyzes multiple research papers, retrieves relevant information, and helps identify potential research gaps using Retrieval-Augmented Generation (RAG).

## 📌 About the Project

Reading multiple research papers and identifying unexplored areas can be time-consuming. **Research Gap Finder** aims to simplify this process by analyzing research papers and comparing their key information to highlight potential research gaps.

The project uses PDF text extraction, text chunking, embeddings, vector search, and an LLM-based analysis pipeline to generate research insights from multiple papers.

## ✨ Features

- 📄 **PDF Text Extraction:** Extracts text from research papers in PDF format.
- ✂️ **Text Chunking:** Splits extracted text into smaller, manageable chunks.
- 🧠 **Text Embeddings:** Converts text into vector representations for semantic retrieval.
- 🔎 **Semantic Search:** Uses FAISS to retrieve relevant information from research papers.
- 🤖 **AI-Powered Analysis:** Uses the Groq API to analyze retrieved research content.
- 🔬 **Research Gap Identification:** Compares insights from multiple papers to highlight potential research gaps.
- 📚 **Multi-Paper Analysis:** Combines information from multiple research papers to support comparative analysis.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| PyMuPDF | PDF text extraction |
| Embeddings | Text representation for semantic search |
| FAISS | Vector storage and similarity search |
| Groq API | LLM-based text analysis |
| Git & GitHub | Version control and project hosting |

## ⚙️ How It Works

The project follows a Retrieval-Augmented Generation (RAG) workflow.

1. **Input:** Research papers are provided as PDF files.
2. **Extraction:** Text is extracted from the PDFs.
3. **Chunking:** The extracted text is divided into smaller chunks with overlapping context.
4. **Embedding Generation:** Text chunks are converted into vector embeddings.
5. **Vector Search:** FAISS retrieves relevant chunks from the research papers.
6. **AI Analysis:** Retrieved content is passed to an LLM through the Groq API.
7. **Gap Identification:** Findings from multiple papers are compared to generate a consolidated research gap analysis.

## 🏗️ Project Architecture

```text
Research Papers (PDF)
        |
        v
   PDF Extraction
        |
        v
    Text Chunking
        |
        v
 Embedding Generation
        |
        v
  FAISS Vector Store
        |
        v
 Relevant Information Retrieval
        |
        v
    Groq LLM Analysis
        |
        v
 Research Gap Analysis
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or a compatible Python version
- Git
- A Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/mishrayuthika05-ui/research-gap-finder.git
```

### 2. Navigate to the Project Directory

```bash
cd research-gap-finder
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

If your repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies listed in your project's setup instructions.

### 5. Configure Environment Variables

Create a `.env` file in the appropriate project directory and add your Groq API key using the variable name expected by your application.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual API key. Never commit your `.env` file or expose your API key publicly.

### 6. Run the Project

Start the FastAPI application using the entry point configured in your repository.

For example, if your application entry point is `backend.main:app`, run:

```bash
python -m uvicorn backend.app.main:app --reload
```

If your entry point is different, replace `backend.main:app` with the correct Python module and FastAPI application variable.

## 🧪 Example Use Case

Suppose you have three research papers related to Retrieval-Augmented Generation (RAG).

Research Gap Finder can:

- Extract relevant information from each paper.
- Retrieve chunks related to the research topic.
- Analyze the papers using an LLM.
- Compare the findings across papers.
- Generate a consolidated report highlighting potential research gaps.

The generated gaps should be treated as research directions to investigate further, not as proof that no previous research exists.

## 🎯 Project Objectives

- Explore practical applications of Retrieval-Augmented Generation.
- Understand document processing and semantic retrieval.
- Apply vector search to research paper analysis.
- Integrate an LLM into a Python backend.
- Explore AI-assisted academic literature analysis.

## 🔮 Future Improvements

- Develop a user-friendly web interface for uploading research papers.
- Add source references for individual research gap statements.
- Improve retrieval quality and evaluate the relevance of retrieved chunks.
- Add downloadable research analysis reports.
- Deploy the application for online access.
- Introduce evaluation metrics to assess the quality of generated research gaps.

## ⚠️ Limitations

- Analysis quality depends on the quality and relevance of the uploaded research papers.
- The model may generate incomplete or inaccurate conclusions.
- Relevant research gaps may be missed if the supplied papers do not cover the topic adequately.
- Generated results require verification against existing academic literature.

## 👩‍💻 Author

**Yuthika Mishra**

B.Tech CSE (AI & ML) Student

- GitHub: [@mishrayuthika05-ui](https://github.com/mishrayuthika05-ui)
- LinkedIn: [Yuthika Mishra](https://www.linkedin.com/in/yuthika-mishra-0ab189337/)

## 📄 License

This project is intended for learning and educational purposes. Add a license file to the repository if you want to specify the terms under which others may use, modify, or distribute the project.
