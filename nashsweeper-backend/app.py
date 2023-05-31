from flask import Flask
from src import GetUserData
from src import GetGameData
from src.utils import DBprocess
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

app.register_blueprint(GetUserData.bp)
app.register_blueprint(GetGameData.bp)

if __name__ == '__main__':

    print("\033[31m Initialize Database \033[0m")
    user_Record = DBprocess.createDB(
        './instance/User.db', 'Record', '(UserName INTEGER, Time INTEGER, STEP INTEGER)')
    app.run(debug=True)
