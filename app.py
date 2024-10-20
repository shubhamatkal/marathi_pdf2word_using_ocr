import os
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from ocr_script import pdf_to_word_devanagari

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        dpi = int(request.form.get('dpi', 150))
        output_folder = app.config['OUTPUT_FOLDER']
        
        try:
            output_file = pdf_to_word_devanagari(file_path, output_folder, dpi)
            return jsonify({'success': True, 'file': output_file})
        except Exception as e:
            return jsonify({'error': str(e)})

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    app.run(debug=True)