from backend.app.services.paper_manager import PaperManager


manager = PaperManager()


manager.add_paper(
    paper_id="paper_1",
    filename="paper1.pdf",
    text="This is the text of the first research paper."
)


manager.add_paper(
    paper_id="paper_2",
    filename="paper2.pdf",
    text="This is the text of the second research paper."
)


manager.add_paper(
    paper_id="paper_3",
    filename="paper3.pdf",
    text="This is the text of the third research paper."
)


print("Number of papers:", manager.get_paper_count())

print("\nStored Papers:")

for paper in manager.get_papers():

    print("\nID:", paper.paper_id)
    print("Filename:", paper.filename)
    print("Text:", paper.text)