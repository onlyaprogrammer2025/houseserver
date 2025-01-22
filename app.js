document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('image');
    formData.append('image', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('message').innerText = `File uploaded successfully! File saved at: ${result.path}`;
        } else {
            document.getElementById('message').innerText = 'Failed to upload file';
        }
    } catch (error) {
        document.getElementById('message').innerText = `Error: ${error.message}`;
    }
});
