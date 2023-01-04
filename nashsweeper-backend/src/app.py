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
            # file_url = url_for('uploaded_file', filename=filename)
            # return render_template('FileUpload.html') + '<br><img src=' + file_url + '>'
            return render_template('GoBack.html')
    return render_template('FileUpload.html')


@app.route('/backend/userrank', methods=['GET'])
def get_user_rank():
    user_rank = [
        {'index': 1, 'PlayerID': 'CIEG',
            'TotalStrategies': 64, 'Time': 200},
        {'index': 2, 'PlayerID': 'Linyuan',
            'TotalStrategies': 72, 'Time': 220},
        {'index': 3, 'PlayerID': 'QianZehao',
            'TotalStrategies': 38, 'Time': 230},
        {'index': 4, 'PlayerID': 'Test1',
            'TotalStrategies': 96, 'Time': 240},
        {'index': 5, 'PlayerID': 'Test2',
            'TotalStrategies': 27, 'Time': 250},
        {'index': 6, 'PlayerID': 'Test3',
            'TotalStrategies': 15, 'Time': 260},
        {'index': 7, 'PlayerID': 'Test4',
            'TotalStrategies': 45, 'Time': 270},
        {'index': 8, 'PlayerID': 'Test5',
            'TotalStrategies': 27, 'Time': 280},
        {'index': 9, 'PlayerID': 'Test6',
            'TotalStrategies': 89, 'Time': 290},
        {'index': 10, 'PlayerID': 'Test7',
            'TotalStrategies': 56, 'Time': 300},
        {'index': 11, 'PlayerID': 'Test8',
            'TotalStrategies': 75, 'Time': 310},
        {'index': 12, 'PlayerID': 'Test9',
            'TotalStrategies': 100, 'Time': 320},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},
        {'index': '...', 'PlayerID': '...',
         'TotalStrategies': '...', 'Time': '...'},

    ]
    return user_rank


if __name__ == '__main__':
    print('The file uploader is running at http://localhost:6778/uploadfile')
    app.run(port=6778)
