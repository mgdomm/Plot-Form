# Plot & Form

Plot & Form is a creative engine that transforms ideas into books — blending narrative (plot) and visual structure (form) to generate print-ready and digital publications.

## Project Structure

```
Plot-Form/
├── plot_engine/           # Interprets creative prompts
│   ├── __init__.py
│   └── prompt_interpreter.py
├── form_engine/           # Generates mandalas and illustrations
│   ├── __init__.py
│   ├── mandala_generator.py
│   └── illustration_generator.py
├── exporters/             # Export to PDF and EPUB
│   ├── __init__.py
│   ├── pdf_exporter.py
│   └── epub_exporter.py
├── web_interface/         # Flask-based local web UI
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
├── requirements.txt       # Python dependencies
└── README.md
```

## Modules

### Plot Engine
Interprets creative prompts and generates narrative structures. The `PromptInterpreter` class extracts themes, characters, settings, and plot points from user input.

### Form Engine
Generates visual content including:
- **Mandala Generator**: Creates geometric mandala patterns
- **Illustration Generator**: Generates illustrations based on narrative content

### Exporters
Converts book content to various formats:
- **PDF Exporter**: Exports to PDF format (ready for implementation)
- **EPUB Exporter**: Placeholder for future EPUB support

### Web Interface
Flask-based local web application that provides:
- Prompt interpretation interface
- Visual generation controls
- Export functionality
- Local-only access (127.0.0.1:5000)

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mgdomm/Plot-Form.git
cd Plot-Form
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Web Interface

```bash
python web_interface/app.py
```

Then open your browser to `http://127.0.0.1:5000`

## Development Status

This project is in early development. Current status:
- ✅ Modular folder structure created
- ✅ Placeholder classes and methods defined
- ✅ Basic Flask web interface
- 🔄 Plot interpretation (to be implemented)
- 🔄 Visual generation (to be implemented)
- 🔄 PDF export (to be implemented)
- ⏳ EPUB export (planned for future)

## License

TBD
