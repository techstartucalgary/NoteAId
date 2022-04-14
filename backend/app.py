import os
import io
import fitz
import time
from flask import Flask, request, redirect, send_file, send_from_directory
from werkzeug.utils import secure_filename
from pdfGenerator import generate_pdf
from summarizer import summarize
from cloudVision import detect_text


app = Flask(__name__)

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'pdf'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "<p>Server is running!</p>"


@app.route('/summarize_images', methods=['POST'])
def upload():
    summarization_level = request.args.get(
        'summ_level', default="normal", type=str)

    if 'files[]' not in request.files:
        print("'files[]' parameter not set")
        return redirect(request.url)

    files = request.files.getlist("files[]")
    texts = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            text = detect_text(filename)
            texts.append(text)
            os.remove(filename)
        else:
            print('Not a valid file')
            redirect(request.url)

    raw_text = " ".join(texts)
    summary = summarize(raw_text, summarization_level)
    out_file_path = "output/" + time.strftime("%Y%m%d%H%M%S") + ".pdf"
    generate_pdf(summary, out_file_path)

    # return send_file(
    #     io.BytesIO(pdf_bytes),
    #     mimetype='application/pdf',
    #     as_attachment=True,
    #     attachment_filename='summary.pdf'
    # )
    res = {"uri": "/" + out_file_path}
    return res
    

@app.route('/summarize_pdf', methods=['POST'])
def upload_pdf():
    summarization_level = request.args.get(
        'summ_level', default="normal", type=str)

    if 'file' not in request.files:
        print("'file' parameter not set")
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        print('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        input_file = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, input_file))

        i = 1
        texts = []
        doc = fitz.open(input_file)
        for page in doc:
            # Minimum 300 DPI for accurate text detection
            pix = page.get_pixmap(dpi=300)
            image_path = f'page{i}.png'
            pix.save(image_path)

            text = detect_text(image_path)
            texts.append(text)
            os.remove(image_path)
            i += 1

        doc.close()
        del doc
        os.remove(input_file)

        raw_text = " ".join(texts)
        summary = summarize(raw_text, summarization_level)
        out_file_path = "output/" + time.strftime("%Y%m%d%H%M%S") + ".pdf"
        generate_pdf(summary, out_file_path)

        res = {"uri": "/" + out_file_path}
        return res


@app.route('/output/<path:path>')
def download_file(path):
    return send_from_directory('output', path)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
