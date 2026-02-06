// Plot & Form - JavaScript Principal

// Estado global del libro
let currentBook = null;
let currentPage = 0;

document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const generateBtn = document.getElementById('generate-book-btn');
    const progressSection = document.getElementById('progress-section');
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    const previewSection = document.getElementById('preview-section');
    const exportPdfBtn = document.getElementById('export-pdf-btn');
    const exportEpubBtn = document.getElementById('export-epub-btn');
    const prevPageBtn = document.getElementById('prev-page-btn');
    const nextPageBtn = document.getElementById('next-page-btn');
    const editPageBtn = document.getElementById('edit-page-btn');
    const regeneratePageBtn = document.getElementById('regenerate-page-btn');
    
    // Enlaces del menú
    document.getElementById('my-books-link').addEventListener('click', (e) => {
        e.preventDefault();
        alert('Funcionalidad "Mis Libros" próximamente disponible');
    });
    
    document.getElementById('help-link').addEventListener('click', (e) => {
        e.preventDefault();
        showHelp();
    });
    
    document.getElementById('settings-link').addEventListener('click', (e) => {
        e.preventDefault();
        alert('Funcionalidad "Configuración" próximamente disponible');
    });

    // Generar Libro
    generateBtn.addEventListener('click', async function() {
        const prompt = document.getElementById('book-prompt').value.trim();
        
        if (!prompt) {
            alert('Por favor, describe el libro que quieres crear');
            return;
        }
        
        // Recopilar datos del formulario
        const bookData = {
            prompt: prompt,
            bookType: document.getElementById('book-type').value,
            targetAudience: document.getElementById('target-audience').value,
            includeText: document.getElementById('include-text').value === 'yes',
            pageCount: parseInt(document.getElementById('page-count').value),
            illustrationStyle: document.getElementById('illustration-style').value,
            colorMode: document.getElementById('color-mode').value
        };
        
        // Mostrar progreso
        showProgress();
        
        try {
            // Paso 1: Interpretar prompt
            updateProgress(20, 'Interpretando tu idea...');
            const interpretation = await interpretPrompt(bookData);
            
            // Paso 2: Generar estructura
            updateProgress(40, 'Creando estructura del libro...');
            await sleep(1000);
            
            // Paso 3: Generar contenido
            updateProgress(60, 'Generando contenido y visuales...');
            const book = await generateBook(bookData, interpretation);
            
            // Paso 4: Preparar vista previa
            updateProgress(80, 'Preparando vista previa...');
            await sleep(500);
            
            // Paso 5: Completado
            updateProgress(100, '¡Libro generado con éxito!');
            
            // Guardar libro actual
            currentBook = book;
            currentPage = 0;
            
            // Mostrar vista previa
            setTimeout(() => {
                hideProgress();
                showPreview(book);
            }, 1000);
            
        } catch (error) {
            console.error('Error generando libro:', error);
            hideProgress();
            alert('Error al generar el libro: ' + error.message);
        }
    });
    
    // Navegación de páginas
    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 0) {
            currentPage--;
            displayPage(currentBook, currentPage);
        }
    });
    
    nextPageBtn.addEventListener('click', () => {
        if (currentPage < currentBook.pages.length - 1) {
            currentPage++;
            displayPage(currentBook, currentPage);
        }
    });
    
    // Editar página
    editPageBtn.addEventListener('click', () => {
        const newText = prompt('Edita el texto de esta página:', currentBook.pages[currentPage].text);
        if (newText !== null) {
            currentBook.pages[currentPage].text = newText;
            displayPage(currentBook, currentPage);
        }
    });
    
    // Regenerar ilustración
    regeneratePageBtn.addEventListener('click', async () => {
        try {
            regeneratePageBtn.disabled = true;
            regeneratePageBtn.textContent = '🔄 Regenerando...';
            
            const response = await fetch('/api/regenerate-illustration', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    pageIndex: currentPage,
                    style: currentBook.metadata.illustrationStyle
                })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                currentBook.pages[currentPage].illustration = data.illustration;
                displayPage(currentBook, currentPage);
            }
        } catch (error) {
            console.error('Error regenerando ilustración:', error);
            alert('Error al regenerar la ilustración');
        } finally {
            regeneratePageBtn.disabled = false;
            regeneratePageBtn.textContent = '🔄 Regenerar Ilustración';
        }
    });
    
    // Exportar PDF
    exportPdfBtn.addEventListener('click', async () => {
        try {
            exportPdfBtn.disabled = true;
            exportPdfBtn.textContent = '⏳ Exportando...';
            
            const response = await fetch('/api/export-pdf', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(currentBook)
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                showExportResult('PDF generado con éxito: ' + data.filename, 'success');
                
                // Descargar archivo
                if (data.download_url) {
                    window.location.href = data.download_url;
                }
            } else {
                showExportResult('Error al exportar PDF', 'error');
            }
        } catch (error) {
            console.error('Error exportando PDF:', error);
            showExportResult('Error al exportar PDF: ' + error.message, 'error');
        } finally {
            exportPdfBtn.disabled = false;
            exportPdfBtn.textContent = '📄 Exportar PDF';
        }
    });
    
    // Exportar EPUB
    exportEpubBtn.addEventListener('click', async () => {
        try {
            exportEpubBtn.disabled = true;
            exportEpubBtn.textContent = '⏳ Exportando...';
            
            const response = await fetch('/api/export-epub', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(currentBook)
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                showExportResult('EPUB generado con éxito: ' + data.filename, 'success');
                
                if (data.download_url) {
                    window.location.href = data.download_url;
                }
            } else {
                showExportResult('Error al exportar EPUB', 'error');
            }
        } catch (error) {
            console.error('Error exportando EPUB:', error);
            showExportResult('Error al exportar EPUB: ' + error.message, 'error');
        } finally {
            exportEpubBtn.disabled = false;
            exportEpubBtn.textContent = '📚 Exportar EPUB';
        }
    });
});

// Funciones auxiliares

function showProgress() {
    document.getElementById('progress-section').style.display = 'block';
    document.getElementById('preview-section').style.display = 'none';
}

function hideProgress() {
    document.getElementById('progress-section').style.display = 'none';
}

function updateProgress(percent, text) {
    document.getElementById('progress-fill').style.width = percent + '%';
    document.getElementById('progress-text').textContent = text;
}

async function interpretPrompt(bookData) {
    const response = await fetch('/api/interpret-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(bookData)
    });
    
    const data = await response.json();
    return data.interpretation;
}

async function generateBook(bookData, interpretation) {
    const response = await fetch('/api/generate-book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...bookData, interpretation })
    });
    
    const data = await response.json();
    return data.book;
}

function showPreview(book) {
    const previewSection = document.getElementById('preview-section');
    const bookInfo = document.getElementById('book-info');
    
    // Mostrar información del libro
    bookInfo.innerHTML = `
        <h3>${book.metadata.title}</h3>
        <p><strong>Tipo:</strong> ${book.metadata.bookType}</p>
        <p><strong>Páginas:</strong> ${book.pages.length}</p>
        <p><strong>Estilo:</strong> ${book.metadata.illustrationStyle}</p>
    `;
    
    previewSection.style.display = 'block';
    displayPage(book, 0);
    
    // Scroll a la vista previa
    previewSection.scrollIntoView({ behavior: 'smooth' });
}

function displayPage(book, pageIndex) {
    const previewContent = document.getElementById('preview-content');
    const pageIndicator = document.getElementById('page-indicator');
    const page = book.pages[pageIndex];
    
    // Actualizar indicador
    pageIndicator.textContent = `Página ${pageIndex + 1} de ${book.pages.length}`;
    
    // Mostrar contenido de la página
    let html = '';
    
    if (page.illustration) {
        html += `<div class="page-illustration">${page.illustration}</div>`;
    }
    
    if (page.text) {
        html += `<div class="page-text"><p>${page.text}</p></div>`;
    }
    
    previewContent.innerHTML = html;
    
    // Actualizar botones
    document.getElementById('prev-page-btn').disabled = pageIndex === 0;
    document.getElementById('next-page-btn').disabled = pageIndex === book.pages.length - 1;
}

function showExportResult(message, type) {
    const resultDiv = document.getElementById('export-result');
    resultDiv.textContent = message;
    resultDiv.className = 'export-result show ' + type;
    
    setTimeout(() => {
        resultDiv.classList.remove('show');
    }, 5000);
}

function showHelp() {
    alert(`
📚 Ayuda - Plot & Form

CÓMO USAR:
1. Describe tu libro en el campo de texto
2. Selecciona las opciones (tipo, público, páginas, etc.)
3. Haz clic en "Generar Libro"
4. Espera mientras se genera el contenido
5. Revisa la vista previa
6. Edita páginas si es necesario
7. Exporta a PDF o EPUB

TIPOS DE LIBROS:
• Mandalas: Libros de patrones geométricos para colorear
• Fantasía: Cuentos e historias fantásticas
• Educativo: Libros de enseñanza
• Historia: Narrativas históricas
• Cuentos: Historias cortas

ESTILOS:
• Geométrico: Formas matemáticas y simétricas
• Fractal: Patrones repetitivos
• Abstracto: Arte libre
• Fantasía: Ilustraciones imaginativas
• Histórico: Estilo clásico
    `);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
