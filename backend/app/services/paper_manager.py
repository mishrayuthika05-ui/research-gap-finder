from dataclasses import dataclass


@dataclass
class ResearchPaper:
    paper_id: str
    filename: str
    text: str


class PaperManager:

    def __init__(self):
        self.papers = []

    def add_paper(
        self,
        paper_id: str,
        filename: str,
        text: str
    ):
        paper = ResearchPaper(
            paper_id=paper_id,
            filename=filename,
            text=text
        )

        self.papers.append(paper)

    def get_papers(self):
        return self.papers

    def get_paper_count(self):
        return len(self.papers)