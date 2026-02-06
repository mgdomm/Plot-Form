# Web

Flask-based web interface for Plot & Form (local only).

## Features

- Creative prompt interpretation interface
- Visual content generation controls
- PDF export functionality
- Clean, modern UI

## Running the Interface

```bash
python web_interface/app.py
```

Then open your browser to: `http://127.0.0.1:5000`

## API Endpoints

- `POST /api/interpret` - Interpret a creative prompt
- `POST /api/generate-visual` - Generate visual content
- `POST /api/export` - Export book to PDF

## Security Note

⚠️ This interface is designed for **local use only**. Do not expose it to the internet without proper security measures.

## Status

🚧 Under Development
