document.getElementById('miBoton').addEventListener('click', function() {
    fetch('http://localhost:5000/api/data')
        .then(response => response.json())
        .then(data => alert(data.mensaje))
        .catch(error => console.error('Error:', error));
});