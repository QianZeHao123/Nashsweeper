import sqlite3


def createDB(DBname, TBname, TBkey):
    # DBname = '../instance/User.db'
    conn = sqlite3.connect(DBname)
    cursor = conn.cursor()
    executeStr = 'CREATE TABLE IF NOT EXISTS '+TBname+' '+TBkey
    cursor.execute('DROP TABLE IF EXISTS '+TBname)
    cursor.execute(executeStr)
    # print(executeStr)
    print('---------------------------------------------------------')
    print('Create database ' + DBname + ', table ' + TBname + ' successfully')
    print('---------------------------------------------------------')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    DBname = '../instance/User.db'
    TBname = 'Record'
    TBkey = '(UserName TEXT, Time INTEGER, STEP INTEGER)'
    createDB(DBname, TBname, TBkey)
