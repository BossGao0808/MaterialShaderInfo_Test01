from flask import Blueprint,render_template,jsonify

bp = Blueprint('shaderinfo', __name__, url_prefix='/shaderinfo')

@bp.route('/')
def index():
    return render_template('HomePage.html')

@bp.route('/testcode',methods=['GET','POST'])
def testcode():
    return render_template('basecode.html')


@bp.route('/datatable',methods=['GET','POST'])
def datatable():
    return render_template('datatable.html')


@bp.route('/data',methods=['POST','GET'])
def data():
    aaData = [
    {
        "id":       "astrocosmos",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "testcode",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "astrocosmos",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "testcode",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "astrocosmos",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "testcode",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "astrocosmos",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "testcode",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "astrocosmos",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    },
    {
        "id":       "testcode",
        "code":   "System Architect",
        "srvName":     "$3,120",
        "url": "2011/04/25",
        "description":     "Edinburgh",
        "isDelete":       "5421"
    }
]
    data={'aaData':aaData}

    outdata = {'data': data}

    return jsonify(outdata)
