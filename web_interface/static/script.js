// Plot & Form - JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const interpretBtn = document.getElementById('interpret-btn');
    const generateMandalaBtn = document.getElementById('generate-mandala');
    const generateIllustrationBtn = document.getElementById('generate-illustration');
    const exportPdfBtn = document.getElementById('export-pdf');
    const resultsSection = document.getElementById('results');
    
    interpretBtn.addEventListener('click', function() {
        const prompt = document.getElementById('prompt').value;
        
        if (!prompt.trim()) {
            alert('Please enter a creative prompt');
            return;
        }
        
        fetch('/api/interpret', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: prompt })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayPlotElements(data.plot_elements);
                resultsSection.style.display = 'block';
            }
        })
        .catch(error => console.error('Error:', error));
    });
    
    generateMandalaBtn.addEventListener('click', function() {
        fetch('/api/generate-visual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type: 'mandala' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayVisual(data.visual_data);
            }
        })
        .catch(error => console.error('Error:', error));
    });
    
    generateIllustrationBtn.addEventListener('click', function() {
        fetch('/api/generate-visual', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type: 'illustration' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayVisual(data.visual_data);
            }
        })
        .catch(error => console.error('Error:', error));
    });
    
    exportPdfBtn.addEventListener('click', function() {
        fetch('/api/export', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ format: 'pdf' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    });
    
    function displayPlotElements(elements) {
        const container = document.getElementById('plot-elements');
        container.innerHTML = `
            <p><strong>Theme:</strong> ${elements.theme}</p>
            <p><strong>Setting:</strong> ${elements.setting}</p>
            <p><strong>Characters:</strong> ${elements.characters.length > 0 ? elements.characters.join(', ') : 'None extracted yet'}</p>
        `;
    }
    
    function displayVisual(visual) {
        const container = document.getElementById('visual-output');
        container.innerHTML = `
            <p><strong>Type:</strong> ${visual.type}</p>
            <p><em>Visual generation will be implemented in future versions</em></p>
        `;
    }
});
