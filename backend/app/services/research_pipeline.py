from backend.app.rag.analyzer import analyze_paper
from backend.app.services.gap_analyzer import compare_papers
from backend.app.services.gap_scorer import score_research_gap
from backend.app.services.evidence_mapper import map_gap_evidence


class ResearchPipeline:

    def analyze_papers(self, papers: list[str]) -> dict:
        """
        Analyze multiple research papers and
        identify and evaluate potential research gaps.
        """

        if len(papers) < 2:
            return {
                "error": "At least two research papers are required."
            }

        # Step 1: Analyze each paper
        analyses = []

        for paper in papers:
            analysis = analyze_paper(paper)
            analyses.append(analysis)

        # Step 2: Compare papers
        comparison = compare_papers(analyses)

        # Step 3: Ask LLM to extract a candidate gap
        gap_prompt = f"""
From the following cross-paper analysis,
identify ONE strongest potential research gap.

Return ONLY the research gap statement.

Cross-Paper Analysis:
{comparison}
"""

        from backend.app.llm.groq_client import generate_answer

        candidate_gap = generate_answer(gap_prompt)

        # Step 4: Score the gap
        score = score_research_gap(
            candidate_gap,
            analyses
        )

        # Step 5: Map evidence
        evidence = map_gap_evidence(
            candidate_gap,
            analyses
        )

        return {
            "paper_analyses": analyses,
            "comparison": comparison,
            "candidate_gap": candidate_gap,
            "gap_score": score,
            "evidence": evidence
        }