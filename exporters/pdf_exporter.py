"""
PDF Exporter

Exports creative books to PDF format ready for Amazon KDP.
"""

import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


class PDFExporter:
    """
    Exports books to PDF format with text and visual content.
    Configured for Amazon KDP specifications.
    """
    
    def __init__(self):
        """Initialize the PDF exporter."""
        # KDP recommended settings for 8.5 x 11 inch (Letter size)
        self.page_size = letter
        # KDP margins (0.25 inch minimum for bleed)
        self.margins = {
            "top": 0.5 * inch,
            "bottom": 0.5 * inch,
            "left": 0.5 * inch,
            "right": 0.5 * inch
        }
    
    def export(self, content: dict, output_path: str) -> bool:
        """
        Export book content to PDF ready for Amazon KDP.
        
        Args:
            content: Dictionary containing book content (metadata, pages, etc.)
            output_path: Path where the PDF should be saved
            
        Returns:
            True if export was successful, False otherwise
        """
        try:
            # Create PDF canvas
            c = canvas.Canvas(output_path, pagesize=self.page_size)
            width, height = self.page_size
            
            # Get book metadata
            metadata = content.get('metadata', {})
            title = metadata.get('title', 'Libro sin título')
            
            # Set PDF metadata
            c.setTitle(title)
            c.setAuthor('Plot & Form Generator')
            c.setSubject('Generated Book')
            
            # Generate cover page
            self._create_cover_page(c, title, metadata)
            c.showPage()
            
            # Generate content pages
            pages = content.get('pages', [])
            for page_data in pages:
                self._create_content_page(c, page_data, metadata)
                c.showPage()
            
            # Save PDF
            c.save()
            print(f"✓ PDF exported successfully: {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error exporting PDF: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def _create_cover_page(self, c, title, metadata):
        """Create an attractive cover page."""
        width, height = self.page_size
        
        # Background gradient effect (simulated with rectangles)
        c.setFillColorRGB(0.4, 0.49, 0.92)  # #667eea
        c.rect(0, 0, width, height, fill=1, stroke=0)
        
        # Title
        c.setFillColorRGB(1, 1, 1)  # White
        c.setFont("Helvetica-Bold", 48)
        
        # Center title
        title_width = c.stringWidth(title, "Helvetica-Bold", 48)
        x = (width - title_width) / 2
        y = height * 0.6
        c.drawString(x, y, title)
        
        # Subtitle
        c.setFont("Helvetica", 24)
        subtitle = f"Tipo: {metadata.get('bookType', 'General')}"
        subtitle_width = c.stringWidth(subtitle, "Helvetica", 24)
        x = (width - subtitle_width) / 2
        c.drawString(x, y - 50, subtitle)
        
        # Generator credit
        c.setFont("Helvetica-Oblique", 14)
        credit = "Generado con Plot & Form"
        credit_width = c.stringWidth(credit, "Helvetica-Oblique", 14)
        x = (width - credit_width) / 2
        c.drawString(x, height * 0.1, credit)
    
    def _create_content_page(self, c, page_data, metadata):
        """Create a content page with illustration and text."""
        width, height = self.page_size
        margin_left = self.margins['left']
        margin_top = self.margins['top']
        margin_right = self.margins['right']
        margin_bottom = self.margins['bottom']
        
        # Available space
        content_width = width - margin_left - margin_right
        content_height = height - margin_top - margin_bottom
        
        # Page number
        c.setFont("Helvetica", 10)
        c.setFillColorRGB(0.4, 0.4, 0.4)
        page_num_text = f"Página {page_data.get('number', 1)}"
        c.drawString(margin_left, margin_bottom / 2, page_num_text)
        
        # Reset color
        c.setFillColorRGB(0, 0, 0)
        
        # Draw illustration placeholder
        illustration_svg = page_data.get('illustration', '')
        if illustration_svg:
            # For MVP, draw a placeholder box with text
            # TODO: Full SVG rendering will be added in next iteration
            img_size = min(content_width * 0.7, content_height * 0.6)
            x = margin_left + (content_width - img_size) / 2
            y = height - margin_top - img_size - 20
            
            # Draw decorative border
            c.setStrokeColorRGB(0.4, 0.49, 0.92)  # Purple/blue
            c.setLineWidth(3)
            c.rect(x, y, img_size, img_size, fill=0, stroke=1)
            
            # Add "Illustration" placeholder text
            c.setFont("Helvetica-Oblique", 12)
            c.setFillColorRGB(0.5, 0.5, 0.5)
            placeholder_text = "[ Ilustración / Mandala ]"
            text_width = c.stringWidth(placeholder_text, "Helvetica-Oblique", 12)
            c.drawString(x + (img_size - text_width) / 2, y + img_size / 2, placeholder_text)
        
        # Draw text if present
        text = page_data.get('text', '')
        if text:
            c.setFont("Helvetica", 14)
            c.setFillColorRGB(0.2, 0.2, 0.2)
            
            # Text area below illustration
            text_y = margin_bottom + 120
            text_width = content_width * 0.9
            x_text = margin_left + (content_width - text_width) / 2
            
            # Word wrap
            lines = self._wrap_text(c, text, text_width, "Helvetica", 14)
            
            # Draw each line centered
            line_height = 22
            for i, line in enumerate(lines):
                if text_y - (i * line_height) > margin_bottom:
                    line_width = c.stringWidth(line, "Helvetica", 14)
                    x_centered = margin_left + (content_width - line_width) / 2
                    c.drawString(x_centered, text_y - (i * line_height), line)
    
    def _wrap_text(self, c, text, max_width, font, font_size):
        """Wrap text to fit within max_width."""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, font, font_size) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def set_page_size(self, size: str):
        """
        Set the page size for the PDF.
        
        Args:
            size: Page size (e.g., "A4", "Letter", "A5")
        """
        if size.upper() == "A4":
            self.page_size = A4
        elif size.upper() == "LETTER":
            self.page_size = letter
        else:
            self.page_size = letter
    
    def set_margins(self, top: float, bottom: float, left: float, right: float):
        """
        Set the page margins in inches.
        
        Args:
            top: Top margin in inches
            bottom: Bottom margin in inches
            left: Left margin in inches
            right: Right margin in inches
        """
        self.margins = {
            "top": top * inch,
            "bottom": bottom * inch,
            "left": left * inch,
            "right": right * inch
        }
