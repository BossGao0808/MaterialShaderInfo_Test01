import random
import string

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import os
import csv
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
from datetime import datetime
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('upload', __name__, url_prefix='/upload')

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

thisdata = []


@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files['filename']:
            uploaded_file = request.files['filename']  # This line uses the same variable and worked fine
            filepath = os.path.join(ROOT_PATH, uploaded_file.filename)
            uploaded_file.save(filepath)
            with open(filepath) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    thisdata.append(row)
                    # print(row)
            # return render_template('upload.html', data=data)
            return redirect(url_for('shaderinfo.datatable'))
        else:
            return render_template('upload.html')
    return render_template('upload.html')


# @bp.route('/OutData',methods=['POST','GET'])
# def data():
#
#
#     aaData=thisdata
#
#     data={'aaData':aaData}
#
#     outdata = {'data': data}
#
#     return jsonify(outdata)


@bp.route('/OutDatatest', methods=['POST', 'GET'])
def datatest():
    # thisrowdata={}
    aaData = []
    if thisdata:
        thisdata.pop(0)

    rowindex = 0
    for row in thisdata:
        thisrowdata = {'id': row[0],
                       'MaterialName': row[2],
                       'QualityLevel':row[3],
                       'ShaderName':row[4],
                       'WorkRegisters':row[6],
                       'UniformRegisters':row[7],
                       '16-bit arithmetic':row[9],
                       'Total Instruction: FMA':row[10],
                       'Total Instruction: CVT':row[11],
                       'Total Instruction: SFU':row[12]
                       }
        aaData.append(thisrowdata)
        print(thisrowdata)
        rowindex += 1

    data = {'aaData': aaData}

    outdata = {'data': data}

    return outdata
