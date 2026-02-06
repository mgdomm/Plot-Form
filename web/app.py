"""
Plot & Form Web

Flask application for local web interface.
"""

import os
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-only-for-local-testing')


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/interpret', methods=['POST'])
def interpret_prompt():
    """
    API endpoint to interpret a creative prompt.
    
    Expected JSON: {"prompt": "your creative prompt"}
    """
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    # Placeholder - will integrate with plot_engine
    result = {
        "status": "success",
        "prompt": prompt,
        "interpretation": "Placeholder interpretation"
    }
    
    return jsonify(result)


@app.route('/api/generate-visual', methods=['POST'])
def generate_visual():
    """
    API endpoint to generate visual content.
    
    Expected JSON: {"type": "mandala|illustration", "params": {...}}
    """
    data = request.get_json()
    visual_type = data.get('type', 'mandala')
    
    # Placeholder - will integrate with form_engine
    result = {
        "status": "success",
        "type": visual_type,
        "visual_data": "Placeholder visual data"
    }
    
    return jsonify(result)


@app.route('/api/export', methods=['POST'])
def export_book():
    """
    API endpoint to export book to PDF.
    
    Expected JSON: {"format": "pdf", "content": {...}}
    """
    data = request.get_json()
    export_format = data.get('format', 'pdf')
    
    # Placeholder - will integrate with exporters
    result = {
        "status": "success",
        "format": export_format,
        "message": "Export functionality coming soon"
    }
    
    return jsonify(result)


if __name__ == '__main__':
    # Run locally only - not for production
    app.run(debug=True, host='127.0.0.1', port=5000)
