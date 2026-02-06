// Plot & Form Web Interface JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Interpret Prompt
    document.getElementById('interpret-btn').addEventListener('click', async function() {
        const prompt = document.getElementById('prompt-input').value;
        const resultDiv = document.getElementById('interpretation-result');
        
        if (!prompt.trim()) {
            alert('Please enter a creative prompt');
            return;
        }
        
        try {
            const response = await fetch('/api/interpret', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt: prompt })
            });
            
            const data = await response.json();
            resultDiv.innerHTML = `<strong>Interpretation:</strong> ${data.interpretation}`;
            resultDiv.classList.add('show');
        } catch (error) {
            resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
            resultDiv.classList.add('show');
        }
    });
    
    // Generate Visual
    document.getElementById('generate-visual-btn').addEventListener('click', async function() {
        const visualType = document.getElementById('visual-type').value;
        const resultDiv = document.getElementById('visual-result');
        
        try {
            const response = await fetch('/api/generate-visual', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ type: visualType, params: {} })
            });
            
            const data = await response.json();
            resultDiv.innerHTML = `<strong>Generated:</strong> ${data.type} (placeholder)`;
            resultDiv.classList.add('show');
        } catch (error) {
            resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
            resultDiv.classList.add('show');
        }
    });
    
    // Export to PDF
    document.getElementById('export-pdf-btn').addEventListener('click', async function() {
        const resultDiv = document.getElementById('export-result');
        
        try {
            const response = await fetch('/api/export', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ format: 'pdf', content: {} })
            });
            
            const data = await response.json();
            resultDiv.innerHTML = `<strong>Status:</strong> ${data.message}`;
            resultDiv.classList.add('show');
        } catch (error) {
            resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
            resultDiv.classList.add('show');
        }
    });
});
