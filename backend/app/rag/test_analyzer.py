from backend.app.rag.analyzer import analyze_paper


paper_text = """
This study proposes a machine learning model for detecting
misinformation on social media platforms.

The researchers trained the model using a dataset containing
English-language social media posts. The model achieved
promising classification performance on the test dataset.

However, the dataset was relatively small and contained only
English-language content. The model was also evaluated on a
limited number of social media platforms.

The authors suggest that future research should investigate
multilingual misinformation detection and evaluate the model
across additional social media platforms.
"""


analysis = analyze_paper(paper_text)


print("\nPaper Analysis")
print("=" * 50)
print(analysis)