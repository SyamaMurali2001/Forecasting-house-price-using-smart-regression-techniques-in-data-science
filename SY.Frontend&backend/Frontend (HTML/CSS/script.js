document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get user inputs
    const bedrooms = document.getElementById('bedrooms').value;
    const sqftLiving = document.getElementById('sqft_living').value;
    const sqftLot = document.getElementById('sqft_lot').value;

    // Send data to backend (via API)
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ bedrooms, sqftLiving, sqftLot })
    })
    .then(response => response.json())
    .then(data => {
        // Show the predicted price
        document.getElementById('price-result').textContent = '$' + data.predicted_price.toLocaleString();
    })
    .catch(error => console.error('Error:', error));
});
