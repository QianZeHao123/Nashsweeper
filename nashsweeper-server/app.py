from flask import Flask
from src import GetUserData
from src import GetGameData
from src.Backendnitialization import Initialization
from src import addUserRec

from flask_cors import CORS

app = Flask(__name__)
# Allow flask to cross domains
CORS(app)


# @app.route('/api/addUserRec')
# def getUserRecord():
#     UserName = request.args.get('UserName')
#     Time = request.args.get('Time')
#     STEP = request.args.get('STEP')
#     print(UserName)
#     print(Time)
#     print(int(STEP)+1)
#     return 'Hello '+UserName


app.register_blueprint(GetUserData.bp)
app.register_blueprint(GetGameData.bp)
app.register_blueprint(addUserRec.bp)

if __name__ == '__main__':
    # Backend program initialization
    Initialization()
    app.run(debug=True, host="0.0.0.0")
