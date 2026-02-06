# Plot & Form

Plot & Form is a creative engine that transforms ideas into books — blending narrative (plot) and visual structure (form) to generate print-ready and digital publications.

## Project Structure

```
Plot-Form/
├── plot_engine/          # Interprets creative prompts into narrative structures
├── form_engine/          # Generates mandalas and illustrations
├── exporters/            # Exports to PDF, EPUB (future)
├── web/                  # Flask local web interface
├── assets/               # Fonts, images, and other resources
├── output/               # Generated books and exports
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

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
python web/app.py
```

Then open your browser to: `http://127.0.0.1:5000`

## Modules

### Plot Engine
Interprets creative prompts and generates narrative structures.

### Form Engine
Generates visual elements including mandalas and illustrations.

### Exporters
Handles exporting books to various formats (PDF now, EPUB later).

### Web Interface
Local Flask-based interface for interacting with the platform.

## Status

🚧 **Under Active Development** - Project structure and placeholder modules created.

## License

TBD

## Contributing

TBD

