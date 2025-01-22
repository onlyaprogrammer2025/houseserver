from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder gde ćeš čuvati slike
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Endpoint za upload slike
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({"message": "File uploaded successfully", "path": file_path}), 200

# Pokreni server na 0.0.0.0 da bude dostupan sa drugih uređaja na istoj mreži
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
