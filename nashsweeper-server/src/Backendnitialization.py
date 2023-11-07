from .utils import DBprocess


def Initialization():
    print('Backend program initialization')
    print('Initialize user database')
    DBpath = './instance/User.db'
    DBprocess.createUserRecDB(DBpath)
