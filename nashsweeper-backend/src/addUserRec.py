from flask import Blueprint
from flask import request
from .utils.DBprocess import insertDataUserRec

bp = Blueprint('addUserRec', __name__, url_prefix='/api/AddUserRec')


@bp.route('/')
def getUserRecord():
    UserName = request.args.get('UserName')
    Time = request.args.get('Time')
    Time = int(Time)
    STEP = request.args.get('STEP')
    STEP = int(STEP)
    # Time = request.args.get('Time')
    # STEP = request.args.get('STEP')
    # return 'Hello '+UserName
    data = (UserName, Time, STEP)
    DBpath = './instance/User.db'
    insertDataUserRec(DBpath, data)
    return 'Successfully insert data'
