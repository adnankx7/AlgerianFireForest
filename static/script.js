document.getElementById('predictionForm').addEventListener('submit', function() {
    const button = document.getElementById('predictBtn');
    button.innerText = 'Predicting...';
    button.disabled = true;
});
