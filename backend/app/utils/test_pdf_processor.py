from backend.app.utils.pdf_processor import extract_text_from_pdf


pdf_path = "data/papers/paper1.pdf"


text = extract_text_from_pdf(pdf_path)


print("\nPDF TEXT EXTRACTION TEST")
print("=" * 60)

print("Characters extracted:", len(text))

print("\nFirst 2000 characters:")
print("-" * 60)
print(text[:2000])