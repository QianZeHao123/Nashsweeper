from flask import Blueprint
import os
from flask import request, send_from_directory
from werkzeug.utils import secure_filename
from flask import render_template

ALLOWED_EXTENSIONS = set(['csv', 'xlsx', 'pdf', 'txt'])

bp = Blueprint('UploadPage', __name__, url_prefix='/UploadPage')
UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) + '/DataUpload'
# bp.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@bp.route('/uploadfile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # file_url = url_for('uploaded_file', filename=filename)
            # return render_template('FileUpload.html') + '<br><img src=' + file_url + '>'
            return render_template('GoBack.html')
    return render_template('FileUpload.html')
