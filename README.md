# 🔬 Research Gap Finder

An AI-powered research assistant that analyzes multiple research papers, retrieves relevant information, and helps identify potential research gaps using **Retrieval-Augmented Generation (RAG)**.

## 📌 About the Project

Reading multiple research papers and identifying unexplored areas can be time-consuming. **Research Gap Finder** aims to simplify this process by analyzing research papers and comparing their key information to highlight potential research gaps.

The project uses PDF text extraction, text chunking, embeddings, vector search, and an LLM-based analysis pipeline to generate research insights from multiple papers.

It includes a simple web frontend where users can upload research papers and view the generated research gap analysis.

## ✨ Features

- 📄 **PDF Text Extraction:** Extracts text from research papers in PDF format.
- ✂️ **Text Chunking:** Splits extracted text into smaller, manageable chunks.
- 🧠 **Text Embeddings:** Converts text into vector representations for semantic retrieval.
- 🔎 **Semantic Search:** Uses FAISS to retrieve relevant information from research papers.
- 🤖 **AI-Powered Analysis:** Uses the Groq API to analyze retrieved research content.
- 🔬 **Research Gap Identification:** Compares insights from multiple papers to highlight potential research gaps.
- 📚 **Multi-Paper Analysis:** Combines information from multiple papers for comparative analysis.
- 🖥️ **Web Interface:** Provides a frontend through which users can upload papers and view the analysis.
- 📊 **Research Gap Evaluation:** Generates a gap score and supporting evidence to help assess the identified research gap.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| HTML, CSS, JavaScript | Frontend web interface |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Text embeddings |
| FAISS | Vector storage and similarity search |
| Groq API | LLM-based text analysis |
| Git & GitHub | Version control and project hosting |

## 🖥️ Frontend

The project includes a simple frontend for interacting with the Research Gap Finder.

Users can:

1. Open the Research Gap Finder web interface.
2. Upload multiple research papers in PDF format.
3. Start the analysis.
4. Wait while the backend processes the uploaded papers.
5. View the generated research gap.
6. View the gap score and supporting evidence.
7. View the individual paper analysis and cross-paper comparison.

The frontend communicates with the FastAPI backend through API requests.

### Frontend Structure

```text
frontend/
├── index.html
├── style.css
└── script.js
```

- `index.html` → Main user interface
- `style.css` → Frontend styling
- `script.js` → Handles PDF upload and communication with the FastAPI backend

## ⚙️ How It Works

The project follows a Retrieval-Augmented Generation (RAG) workflow.

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
        |
        v
      Frontend
        |
        v
   Results Display
```

### Workflow

1. **Input:** Users upload research papers through the frontend.
2. **Extraction:** Text is extracted from the uploaded PDFs.
3. **Chunking:** The extracted text is divided into smaller chunks with overlapping context.
4. **Embedding Generation:** Text chunks are converted into vector embeddings.
5. **Vector Search:** FAISS retrieves relevant chunks from the research papers.
6. **AI Analysis:** Retrieved content is passed to an LLM through the Groq API.
7. **Paper Analysis:** Important information such as research problems, methodology, findings, limitations, and future work is analyzed.
8. **Gap Identification:** Findings from multiple papers are compared to generate a consolidated research gap.
9. **Result Display:** The frontend displays the research gap, score, supporting evidence, and paper-level analysis.

## 🏗️ Project Architecture

```text
                    User
                     |
                     v
              Frontend Interface
              (HTML/CSS/JS)
                     |
                     v
              FastAPI Backend
                     |
                     v
              PDF Processing
                     |
                     v
               Text Chunking
                     |
                     v
              Embeddings
                     |
                     v
             FAISS Retrieval
                     |
                     v
                Groq LLM
                     |
                     v
           Research Gap Analysis
                     |
                     v
              Frontend Results
```

## 📁 Project Structure

```text
research-gap-finder/
│
├── backend/
│   ├── app/
│   │   └── main.py
│   │
│   └── rag/
│       ├── chunker.py
│       ├── embeddings.py
│       ├── vector_store.py
│       ├── analyzer.py
│       └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
│   └── papers/
│
├── requirements.txt
├── .env
└── README.md
```

> The exact files inside the `backend` and `rag` directories may vary as the project evolves.

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

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace `your_groq_api_key` with your actual API key.

**Never commit your `.env` file or expose your API key publicly.**

### 6. Start the Backend

Run the FastAPI application:

```bash
python -m uvicorn backend.app.main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

You can also open the FastAPI Swagger documentation at:

```text
http://127.0.0.1:8000/docs
```

### 7. Start the Frontend

Open a **new terminal** while keeping the backend running.

Navigate to the frontend directory:

```bash
cd frontend
```

If the frontend is a simple HTML/CSS/JavaScript frontend, start a local web server:

```bash
python -m http.server 5500
```

The frontend will normally be available at:

```text
http://127.0.0.1:5500
```

Open this URL in your browser to use the application.

### 8. Use the Application

1. Open the frontend in your browser.
2. Upload the required research papers in PDF format.
3. Start the analysis.
4. Wait for the backend to process the papers.
5. View the generated research gap.
6. Review the gap score and confidence.
7. Check the supporting evidence.
8. Review the individual paper analyses and cross-paper comparison.

## 🧪 Example Use Case

Suppose you have three research papers related to Retrieval-Augmented Generation (RAG).

Research Gap Finder can:

- Extract relevant information from each paper.
- Retrieve chunks related to the research topic.
- Analyze the papers using an LLM.
- Compare the findings across papers.
- Identify limitations and future-work areas.
- Generate a consolidated report highlighting potential research gaps.

The generated gaps should be treated as **research directions to investigate further**, not as proof that no previous research exists.

## 📊 Research Gap Evaluation

The project can also evaluate the identified research gap using factors such as:

- Evidence available across papers
- Number of papers supporting the gap
- Coverage of the research topic
- Potential novelty
- Supporting evidence from the analyzed papers

The result can include:

```text
GAP SCORE
CONFIDENCE
SUPPORTING EVIDENCE
REASONING
```

This helps provide additional context for the generated research gap instead of relying only on the LLM-generated statement.

## 🎯 Project Objectives

- Explore practical applications of Retrieval-Augmented Generation.
- Understand document processing and semantic retrieval.
- Apply vector search to research paper analysis.
- Integrate an LLM into a Python backend.
- Build a simple web interface for AI-assisted research analysis.
- Explore AI-assisted academic literature analysis.

## 🔮 Future Improvements

- Add source references for individual research gap statements.
- Improve retrieval quality and evaluate the relevance of retrieved chunks.
- Add downloadable research analysis reports.
- Improve frontend usability and visualization.
- Deploy the application for online access.
- Introduce more evaluation metrics to assess the quality of generated research gaps.
- Support larger numbers of research papers.

## ⚠️ Limitations

- Analysis quality depends on the quality and relevance of the uploaded research papers.
- The model may generate incomplete or inaccurate conclusions.
- Relevant research gaps may be missed if the supplied papers do not cover the topic adequately.
- Generated results require verification against existing academic literature.
- The quality of the final result depends on the retrieved information provided to the LLM.
- Large research papers may require more processing time and memory.

## 👩‍💻 Author

**Yuthika Mishra**

B.Tech CSE (AI & ML) Student

- GitHub: [@mishrayuthika05-ui](https://github.com/mishrayuthika05-ui)
- LinkedIn: [Yuthika Mishra](https://www.linkedin.com/in/yuthika-mishra-0ab189337/)

## 📄 License

This project is intended for learning and educational purposes. Add a license file to the repository if you want to specify the terms under which others may use, modify, or distribute the project.
