const API_URL = "http://127.0.0.1:8000/api/analyze-papers";

const analyzeButton = document.getElementById("analyzeButton");
const loading = document.getElementById("loading");
const error = document.getElementById("error");
const results = document.getElementById("results");

analyzeButton.addEventListener("click", analyzePapers);


async function analyzePapers() {

    const paper1 = document.getElementById("paper1").files[0];
    const paper2 = document.getElementById("paper2").files[0];
    const paper3 = document.getElementById("paper3").files[0];

    // Reset previous state
    error.hidden = true;
    error.textContent = "";
    results.hidden = true;


    // Validate files
    if (!paper1 || !paper2 || !paper3) {

        error.textContent =
            "Please upload all three research papers.";

        error.hidden = false;

        return;
    }


    // Validate PDF files
    const papers = [paper1, paper2, paper3];

    for (const paper of papers) {

        if (!paper.name.toLowerCase().endsWith(".pdf")) {

            error.textContent =
                "Only PDF files are allowed.";

            error.hidden = false;

            return;
        }
    }


    // Prepare form data
    const formData = new FormData();

    formData.append("paper1", paper1);
    formData.append("paper2", paper2);
    formData.append("paper3", paper3);


    // Loading state
    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";
    loading.hidden = false;


    try {

        const response = await fetch(API_URL, {
            method: "POST",
            body: formData
        });


        let data;

        try {

            data = await response.json();

        } catch {

            throw new Error(
                "Server returned an invalid response."
            );
        }


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Research analysis failed."
            );
        }


        displayResults(data);


    } catch (err) {

        console.error("Analysis Error:", err);

        error.textContent =
            err.message ||
            "Unable to connect to the backend.";

        error.hidden = false;


    } finally {

        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Papers";

        loading.hidden = true;
    }
}



function displayResults(data) {

    results.hidden = false;


    // =========================
    // RESEARCH GAP
    // =========================

    document.getElementById("researchGap").textContent =
        data.research_gap ||
        "No sufficiently supported research gap identified.";


    // =========================
    // GAP SCORE
    // =========================

    document.getElementById("gapScore").textContent =
        formatResult(data.gap_score);


    // =========================
    // CROSS PAPER ANALYSIS
    // =========================

    document.getElementById("comparison").textContent =
        formatResult(
            data.cross_paper_analysis
        );


    // =========================
    // EVIDENCE
    // =========================

    document.getElementById("evidence").textContent =
        formatResult(
            data.evidence
        );


    // =========================
    // INDIVIDUAL PAPER ANALYSIS
    // =========================

    const paperContainer =
        document.getElementById("paperAnalyses");

    paperContainer.innerHTML = "";


    if (
        data.paper_analyses &&
        Array.isArray(data.paper_analyses)
    ) {

        data.paper_analyses.forEach(
            (paper, index) => {

                const div =
                    document.createElement("div");

                div.style.marginBottom = "25px";


                const heading =
                    document.createElement("h3");

                heading.textContent =
                    `Paper ${index + 1}: ${
                        paper.filename || "Unknown"
                    }`;


                const analysis =
                    document.createElement("pre");

                analysis.textContent =
                    paper.analysis ||
                    "Analysis not available.";

                analysis.style.whiteSpace =
                    "pre-wrap";

                analysis.style.lineHeight =
                    "1.7";


                div.appendChild(heading);
                div.appendChild(analysis);

                paperContainer.appendChild(div);
            }
        );

    } else {

        paperContainer.textContent =
            "Individual paper analysis not available.";
    }
}



function formatResult(value) {

    if (
        value === null ||
        value === undefined ||
        value === ""
    ) {

        return "Not available";
    }


    if (typeof value === "object") {

        return JSON.stringify(
            value,
            null,
            2
        );
    }


    return String(value);
}