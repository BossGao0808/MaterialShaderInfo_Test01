from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import csv
from savefile.getsavepath import ROOT_PATH, genfilepath
import os
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel, ShaderInfoModel
from datetime import datetime
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('upload', __name__, url_prefix='/upload')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if request.files['filename']:
            print(request.form['Describe'])
            filepath = genfilepath(request.form['ProjectName'], request.form['time'])
            uploaded_file = request.files['filename']  # This line uses the same variable and worked fine
            uploaded_file.save(filepath)
            checkshaderifo = ShaderInfoModel.query.filter_by(filepath=filepath).first()
            if checkshaderifo:
                checkshaderifo.Describe += '  ||| new commit on' + str(datetime.now()) + str(request.form['Describe'])
                db.session.commit()
            else:
                ShaderInfo = ShaderInfoModel(Project=request.form['ProjectName'],
                                             add_time=request.form['time'],
                                             filepath=filepath,
                                             Describe=request.form['Describe']
                                             )
                db.session.add(ShaderInfo)
                db.session.commit()
            return redirect(url_for('shaderinfo.datatable'))
        else:
            return render_template('upload.html')
    return render_template('upload.html')


@bp.route('/OutDatatest', methods=['POST', 'GET'])
def datatest():
    thisdatetime = request.args.get('datetime')
    if thisdatetime:
        aaData = []
        thisdata = []
        rowindex = 0
        ThisShaderInfo= ShaderInfoModel.query.filter_by(add_time=thisdatetime).first()
        filepath = ThisShaderInfo.filepath
        with open(filepath) as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                thisdata.append(row)

        if thisdata:
            thisdata.pop(0)

        for row in thisdata:
            thisrowdata = {'id': row[0],
                           'MaterialName': row[2],
                           'QualityLevel': row[3],
                           'ShaderName': row[4],
                           'WorkRegisters': row[6],
                           'UniformRegisters': row[7],
                           '16-bit arithmetic': row[9],
                           'Total Instruction: FMA': row[10],
                           'Total Instruction: CVT': row[11],
                           'Total Instruction: SFU': row[12]
                           }
            aaData.append(thisrowdata)
            # print(thisrowdata)
            rowindex += 1

        data = {'aaData': aaData}

        outdata = {'data': data}

        render_template('datatable.html')
        return outdata
    else:
        # thisrowdata={}
        aaData = []
        thisdata = []
        rowindex = 0

        ThisShaderInfo = ShaderInfoModel.query.filter_by(Project='Project_Name_2')
        filepath = ThisShaderInfo[-1].filepath
        with open(filepath) as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                thisdata.append(row)

        if thisdata:
            thisdata.pop(0)

        for row in thisdata:
            thisrowdata = {'id': row[0],
                           'MaterialName': row[2],
                           'QualityLevel': row[3],
                           'ShaderName': row[4],
                           'WorkRegisters': row[6],
                           'UniformRegisters': row[7],
                           '16-bit arithmetic': row[9],
                           'Total Instruction: FMA': row[10],
                           'Total Instruction: CVT': row[11],
                           'Total Instruction: SFU': row[12]
                           }
            aaData.append(thisrowdata)
            # print(thisrowdata)
            rowindex += 1

        data = {'aaData': aaData}

        outdata = {'data': data}

        render_template('datatable.html')
        return outdata


@bp.route('/OutColumns', methods=['POST', 'GET'])
def OutColumns():
    aaData = {'id': 1,
              'MaterialName': 2,
              'QualityLevel': 2,
              'ShaderName': 2,
              'WorkRegisters': 2,
              'UniformRegisters': 2,
              '16-bit arithmetic': 2,
              'Total Instruction: FMA': 2,
              'Total Instruction: CVT': 2,
              'Total Instruction: SFU': 2
              }

    aoColumns = [
        {
            'data': "id"
        },
        {
            'data': "MaterialName"
        },
        {
            'data': "QualityLevel"
        },
        {
            'data': "ShaderName"
        },
        {
            'data': "WorkRegisters"
        },
        {
            'data': "UniformRegisters"
        },
        {
            'data': "16-bit arithmetic"
        },
        {
            'data': "Total Instruction: FMA"
        },
        {
            'data': "Total Instruction: CVT"
        },
        {
            'data': "Total Instruction: SFU"
        }
    ]

    data = {'aoColumns': aoColumns, 'aaData': aaData}

    outdata = {'data': data}

    return data


@bp.route('/ButtonList', methods=['POST', 'GET'])
def ButtonList():
    ButtonList = []
    ShaderInfoList = ShaderInfoModel.query.filter_by(Project='Project_Name_2')
    for Info in ShaderInfoList:
        ButtonName = str(Info.add_time)
        ThisButton = '<button type="button" class="btn btn-primary" value="' + ButtonName+'">' + ButtonName + '</button>'
        print(ThisButton)
        ButtonList.append(ThisButton)

    return ButtonList

#
# @bp.route('/', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         if request.files['filename']:
#
#             filepath = genfilepath(request.form['ProjectName'],request.form['time'])
#             uploaded_file = request.files['filename']  # This line uses the same variable and worked fine
#             uploaded_file.save(filepath)
#             with open(filepath) as file:
#                 csv_file = csv.reader(file)
#                 for row in csv_file:
#                     thisdata.append(row)
#                     # print(row)
#             # return render_template('upload.html', data=data)
#             return redirect(url_for('shaderinfo.datatable'))
#         else:
#             return render_template('upload.html')
#     return render_template('upload.html')
#
