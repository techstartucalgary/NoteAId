import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_file

UPLOAD_FOLDER = 'C:/Users/Mansoor/Documents/GitHub/NoteAId'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

 #define a flask route
def upload_file(): #uploading image
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#In this case, if a person goes to /return-files/,
# and clicks the download button, they will get an image returned.

#return a pdf file
def return_files_tut():
	try:
		return send_file('/var/www/PythonProgramming/PythonProgramming/static/ohhey.pdf', attachment_filename='ohhey.pdf')
	except Exception as e:
		return str(e)
