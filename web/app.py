"""
Plot & Form Web

Flask application for local web interface.
"""

import os
import sys
from flask import Flask, render_template, request, jsonify, send_file

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plot_engine.prompt_interpreter import PromptInterpreter
from form_engine.mandala_generator import MandalaGenerator
from form_engine.illustration_generator import IllustrationGenerator
from exporters.pdf_exporter import PDFExporter
from exporters.epub_exporter import EPUBExporter


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-only-for-local-testing')

# Inicializar motores
prompt_interpreter = PromptInterpreter()
mandala_generator = MandalaGenerator()
illustration_generator = IllustrationGenerator()
pdf_exporter = PDFExporter()
epub_exporter = EPUBExporter()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/interpret-prompt', methods=['POST'])
def interpret_prompt():
    """
    Interpreta el prompt del usuario y determina qué tipo de contenido generar.
    """
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        book_type = data.get('bookType', 'mandalas')
        
        # Usar el plot_engine para interpretar
        interpretation = prompt_interpreter.interpret(prompt)
        interpretation['bookType'] = book_type
        interpretation['suggestedTitle'] = generate_title(prompt, book_type)
        
        return jsonify({
            'status': 'success',
            'interpretation': interpretation
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/generate-book', methods=['POST'])
def generate_book():
    """
    Genera el libro completo con texto e ilustraciones.
    """
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        book_type = data.get('bookType', 'mandalas')
        page_count = data.get('pageCount', 20)
        include_text = data.get('includeText', True)
        illustration_style = data.get('illustrationStyle', 'geometrico')
        color_mode = data.get('colorMode', 'color')
        target_audience = data.get('targetAudience', 'general')
        
        # Generar título
        title = generate_title(prompt, book_type)
        
        # Generar páginas
        pages = []
        for i in range(page_count):
            page = {
                'number': i + 1,
                'text': generate_page_text(i, page_count, book_type, prompt, include_text),
                'illustration': generate_illustration(i, illustration_style, color_mode, book_type)
            }
            pages.append(page)
        
        # Estructura del libro
        book = {
            'metadata': {
                'title': title,
                'bookType': book_type,
                'pageCount': page_count,
                'illustrationStyle': illustration_style,
                'colorMode': color_mode,
                'targetAudience': target_audience,
                'prompt': prompt
            },
            'pages': pages
        }
        
        return jsonify({
            'status': 'success',
            'book': book
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/regenerate-illustration', methods=['POST'])
def regenerate_illustration():
    """
    Regenera la ilustración de una página específica.
    """
    try:
        data = request.get_json()
        page_index = data.get('pageIndex', 0)
        style = data.get('style', 'geometrico')
        
        # Generar nueva ilustración
        illustration = generate_illustration(page_index, style, 'color', 'mandalas')
        
        return jsonify({
            'status': 'success',
            'illustration': illustration
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/export-pdf', methods=['POST'])
def export_pdf():
    """
    Exporta el libro a PDF listo para Amazon KDP.
    """
    try:
        data = request.get_json()
        book = data
        
        # Generar nombre de archivo
        filename = f"{sanitize_filename(book['metadata']['title'])}.pdf"
        output_path = os.path.join('output', filename)
        
        # Asegurar que existe el directorio output
        os.makedirs('output', exist_ok=True)
        
        # Exportar usando el PDF exporter
        success = pdf_exporter.export(book, output_path)
        
        if success:
            return jsonify({
                'status': 'success',
                'filename': filename,
                'message': 'PDF generado exitosamente',
                'download_url': f'/download/{filename}'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Error al generar PDF'
            }), 500
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/api/export-epub', methods=['POST'])
def export_epub():
    """
    Exporta el libro a EPUB.
    """
    try:
        data = request.get_json()
        book = data
        
        # Generar nombre de archivo
        filename = f"{sanitize_filename(book['metadata']['title'])}.epub"
        output_path = os.path.join('output', filename)
        
        # Asegurar que existe el directorio output
        os.makedirs('output', exist_ok=True)
        
        # Exportar usando el EPUB exporter
        success = epub_exporter.export(book, output_path)
        
        if success:
            return jsonify({
                'status': 'success',
                'filename': filename,
                'message': 'EPUB generado exitosamente',
                'download_url': f'/download/{filename}'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'EPUB aún no implementado completamente'
            }), 501
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500


@app.route('/download/<filename>')
def download_file(filename):
    """
    Descarga un archivo generado.
    """
    try:
        file_path = os.path.join('output', filename)
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 404


# Funciones auxiliares

def generate_title(prompt, book_type):
    """Genera un título basado en el prompt y tipo de libro."""
    if 'mandala' in prompt.lower() or book_type == 'mandalas':
        return "Mandalas para Colorear"
    elif book_type == 'fantasia':
        return "Aventuras de Fantasía"
    elif book_type == 'cuento':
        return "Cuentos Mágicos"
    elif book_type == 'educativo':
        return "Aprendiendo con Imágenes"
    else:
        # Usar primeras palabras del prompt
        words = prompt.split()[:3]
        return ' '.join(words).title()


def generate_page_text(page_num, total_pages, book_type, prompt, include_text):
    """Genera texto para una página."""
    if not include_text:
        return ""
    
    if book_type == 'mandalas':
        return f"Mandala {page_num + 1} - Encuentra la paz interior coloreando este diseño único."
    elif book_type == 'fantasia':
        return f"En esta página de nuestra aventura, nuestro héroe descubre nuevos desafíos y maravillas."
    elif book_type == 'cuento':
        return f"Érase una vez, en un lugar mágico, donde las historias cobran vida..."
    elif book_type == 'educativo':
        return f"Lección {page_num + 1}: Aprende y descubre el mundo que te rodea."
    else:
        return f"Página {page_num + 1} de {total_pages}"


def generate_illustration(page_num, style, color_mode, book_type):
    """Genera una ilustración usando form_engine."""
    try:
        # Generar mandala con diferentes parámetros según la página
        symmetry = 6 + (page_num % 6)  # Varía la simetría
        complexity = ['simple', 'medium', 'complex'][page_num % 3]
        
        mandala_data = mandala_generator.generate(seed=page_num, complexity=complexity)
        mandala_generator.set_symmetry(symmetry)
        
        # Por ahora retornamos SVG simple como placeholder
        # TODO: Implementar generación real de SVG
        svg = create_simple_mandala_svg(symmetry, color_mode, page_num)
        
        return svg
    except Exception as e:
        print(f"Error generando ilustración: {e}")
        return '<svg width="400" height="400"><circle cx="200" cy="200" r="100" fill="#667eea"/></svg>'


def create_simple_mandala_svg(symmetry, color_mode, seed):
    """Crea un SVG simple de mandala."""
    import math
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe']
    if color_mode == 'bw':
        colors = ['#000000']
    
    svg_parts = ['<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">']
    svg_parts.append('<rect width="400" height="400" fill="white"/>')
    
    # Centro
    cx, cy = 200, 200
    
    # Círculos concéntricos
    for i in range(5, 0, -1):
        radius = i * 30
        color = colors[(i + seed) % len(colors)]
        svg_parts.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{color}" stroke-width="2"/>')
    
    # Pétalos radiales
    for i in range(symmetry):
        angle = (360 / symmetry) * i
        rad = math.radians(angle)
        x = cx + math.cos(rad) * 80
        y = cy + math.sin(rad) * 80
        color = colors[i % len(colors)]
        svg_parts.append(f'<circle cx="{x}" cy="{cy}" r="20" fill="{color}" opacity="0.7"/>')
    
    svg_parts.append('</svg>')
    return ''.join(svg_parts)


def sanitize_filename(filename):
    """Limpia el nombre de archivo de caracteres no válidos."""
    import re
    # Eliminar caracteres especiales
    filename = re.sub(r'[^\w\s-]', '', filename)
    # Reemplazar espacios con guiones bajos
    filename = re.sub(r'\s+', '_', filename)
    return filename[:50]  # Limitar longitud


if __name__ == '__main__':
    # Run locally only - not for production
    # Debug mode is enabled for development convenience
    # SECURITY: Only run on localhost (127.0.0.1) - never expose to public network
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 'yes')
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)
