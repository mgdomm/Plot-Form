"""
Flask Application - Main web interface for Plot & Form.

This module provides a local-only Flask web application for generating books.
"""

import os
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-please-set-SECRET_KEY-in-env')


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/interpret', methods=['POST'])
def interpret_prompt():
    """
    API endpoint to interpret a creative prompt.
    
    Returns:
        JSON response with interpreted plot elements
    """
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    # Placeholder - will use plot_engine
    result = {
        "success": True,
        "plot_elements": {
            "theme": "extracted theme",
            "characters": [],
            "setting": "extracted setting"
        }
    }
    return jsonify(result)


@app.route('/api/generate-visual', methods=['POST'])
def generate_visual():
    """
    API endpoint to generate visual content.
    
    Returns:
        JSON response with visual data
    """
    data = request.get_json()
    visual_type = data.get('type', 'mandala')
    
    # Placeholder - will use form_engine
    result = {
        "success": True,
        "visual_data": {
            "type": visual_type,
            "svg_data": None
        }
    }
    return jsonify(result)


@app.route('/api/export', methods=['POST'])
def export_book():
    """
    API endpoint to export book to PDF.
    
    Returns:
        JSON response with export status
    """
    data = request.get_json()
    format_type = data.get('format', 'pdf')
    
    # Placeholder - will use exporters
    result = {
        "success": True,
        "message": f"Book export to {format_type} queued",
        "file_path": None
    }
    return jsonify(result)


if __name__ == '__main__':
    # Local only - do not expose to external networks
    app.run(debug=True, host='127.0.0.1', port=5000)
