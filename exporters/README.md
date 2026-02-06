# Exporters

The Exporters module handles exporting creative books to various formats.

## Supported Formats

### PDF (Active Development)
- Print-ready PDF generation
- Customizable page sizes and margins
- Support for text and visual content

### EPUB (Planned)
- Digital reading format
- Reflowable content
- Metadata support

## Usage

```python
from exporters.pdf_exporter import PDFExporter

# Export to PDF
pdf_exporter = PDFExporter()
pdf_exporter.set_page_size("A4")
pdf_exporter.export(book_content, "output.pdf")
```

## Dependencies

The following libraries will be used (to be added to requirements.txt):
- `reportlab` or `weasyprint` for PDF generation
- `ebooklib` for EPUB generation (future)

## Status

- PDF: 🚧 Under Development
- EPUB: 📋 Planned
