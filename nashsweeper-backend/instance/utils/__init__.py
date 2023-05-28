# import os
# from flask import Flask
# # import src.db as db
# import src.UploadPage as UploadPage
# import src.GetUserData as GetUserData
# from src.nashsweeper_core_engine.CoreCalcOptForGame import CoreCalc
# import random


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     # app.config.from_mapping(
#     #     SECRET_KEY='dev',
#     #     DATABASE=os.path.join(app.instance_path, 'nashsweeper.sqlite'),
#     # )

#     # if test_config is None:
#     #     # load the instance config, if it exists, when not testing
#     #     app.config.from_pyfile('config.py', silent=True)
#     # else:
#     #     # load the test config if passed in
#     #     app.config.from_mapping(test_config)

#     # # ensure the instance folder exists
#     # try:
#     #     os.makedirs(app.instance_path)
#     # except OSError:
#     #     pass

#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     @app.route('/GetGamedata')
#     def GetGamedata():
#         NE_num = 0
#         while NE_num == 0:
#             test_strategy_matrix = [random.randint(0, 100) for _ in range(128)]
#             strategy_matrix = test_strategy_matrix
#             regP1, regP2 = CoreCalc.regCalc(strategy_matrix)
#             # calculate the regret value of regP1 and regP2
#             print(regP1)
#             print(regP2)
#             # output the nash equilibrium list and best response of player 1 and player 2
#             NE, BRP1, BRP2 = CoreCalc.BRNElst(regP1, regP2)
#             NE_num = len(NE)
#             print(NE)
#             print(BRP1)
#             print(BRP2)
#         GameData = {
#             'Checkerboard': test_strategy_matrix,
#             'NE': [int(_) for _ in NE],
#             'BRP1': [int(_) for _ in BRP1],
#             'BRP2': [int(_) for _ in BRP2]
#         }
#         # return test_strategy_matrix, NE, BRP1, BRP2
#         return GameData
#     # ------------------------------------------------------------------------------
#     # from . import db
#     # db.init_app(app)
#     # from . import UploadPage
#     app.register_blueprint(UploadPage.bp)
#     # from . import GetUserData
#     app.register_blueprint(GetUserData.bp)

#     return app
