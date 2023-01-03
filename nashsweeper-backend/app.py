# -*- coding: utf-8 -*-
import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask import render_template

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'pdf', 'txt'])

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['UPLOAD_FOLDER'] = 'DataUpload'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            # return render_template('FileUpload.html') + '<br><img src=' + file_url + '>'
            return render_template('GoBack.html')
    return render_template('FileUpload.html')


if __name__ == '__main__':
    print('The file uploader is running at http://localhost:6778/uploadfile')
    app.run(port=6778)
