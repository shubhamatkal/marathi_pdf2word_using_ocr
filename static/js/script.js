document.getElementById('uploadForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    var formData = new FormData(this);
    var xhr = new XMLHttpRequest();
    var progressBar = document.getElementById('progressBar');
    var convertBtn = document.getElementById('convertBtn');
    
    xhr.open('POST', '/convert', true);
    
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                document.getElementById('result').style.display = 'block';
                document.getElementById('downloadLink').href = '/download/' + response.file;
            } else {
                alert('Error: ' + response.error);
            }
        } else {
            alert('An error occurred during the conversion process.');
        }
        progressBar.style.display = 'none';
        convertBtn.disabled = false;
    };
    
    progressBar.style.display = 'block';
    convertBtn.disabled = true;
    xhr.send(formData);
});