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

    error.hidden = true;
    results.hidden = true;

    if (!paper1 || !paper2 || !paper3) {
        error.textContent = "Please upload all three research papers.";
        error.hidden = false;
        return;
    }

    const formData = new FormData();

    formData.append("paper1", paper1);
    formData.append("paper2", paper2);
    formData.append("paper3", paper3);

    analyzeButton.disabled = true;
    loading.hidden = false;

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Research analysis failed."
            );
        }

        displayResults(data);

    } catch (err) {

        error.textContent = err.message;
        error.hidden = false;

    } finally {

        analyzeButton.disabled = false;
        loading.hidden = true;
    }
}


function displayResults(data) {

    results.hidden = false;

    document.getElementById("researchGap").textContent =
        data.research_gap || "Not available";

    document.getElementById("gapScore").textContent =
        formatResult(data.gap_score);

    document.getElementById("comparison").textContent =
        formatResult(data.cross_paper_analysis);

    document.getElementById("evidence").textContent =
        formatResult(data.evidence);


    const paperContainer =
        document.getElementById("paperAnalyses");

    paperContainer.innerHTML = "";

    if (data.paper_analyses) {

        data.paper_analyses.forEach((paper, index) => {

            const div = document.createElement("div");

            div.innerHTML = `
                <h3>Paper ${index + 1}: ${paper.filename}</h3>
                <pre>${paper.analysis}</pre>
            `;

            paperContainer.appendChild(div);
        });
    }
}


function formatResult(value) {

    if (value === null || value === undefined) {
        return "Not available";
    }

    if (typeof value === "object") {
        return JSON.stringify(value, null, 2);
    }

    return String(value);
}