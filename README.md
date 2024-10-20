# Marathi PDF to WORD with OCR

This application converts Marathi PDF documents to WORD format using OCR (Optical Character Recognition) technology.

## Features

- Upload PDF files containing Marathi text
- Select DPI for conversion (100, 150, or 300)
- Progress bar to show conversion status
- Download converted DOCX file

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/marathi-pdf-ocr.git
   cd marathi-pdf-ocr
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR and the Marathi language pack. Make sure the `tesseract_cmd` path in `ocr_script.py` is correct for your system.

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.

3. Upload a PDF file, select the desired DPI, and click "Start Converting".

4. Once the conversion is complete, click the "Download DOCX" button to get your converted file.

## Note

This application is designed specifically for Marathi text OCR. Ensure that your PDF contains primarily Marathi text for the best results.

## License

This project is open-source and available under the MIT License.

## Contact

For any questions or issues, please contact:

Shubham Atkal
- Email: shubhamatkal@gmail.com
- GitHub: [https://github.com/shubhamatkal](https://github.com/shubhamatkal)