from PyPDF2 import PdfReader

print("=" * 50)
print("📄 RAG v1 - PDF Reader")
print("=" * 50)

pdf_file = "sample.pdf"

print(f"\nReading PDF: {pdf_file}")

reader = PdfReader(pdf_file)

total_pages = len(reader.pages)

print(f"\nTotal Pages: {total_pages}\n")

for page_number, page in enumerate(reader.pages, start=1):
    print("-" * 50)
    print(f"Page {page_number}")
    print("-" * 50)

    text = page.extract_text()

    if text:
        print(text)
    else:
        print("No text found on this page.")

print("\n✅ PDF text extraction completed successfully!")