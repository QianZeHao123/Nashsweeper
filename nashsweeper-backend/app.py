from flask import Flask
from src import GetUserData
from src import GetGameData
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

app.register_blueprint(GetUserData.bp)
app.register_blueprint(GetGameData.bp)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True)
