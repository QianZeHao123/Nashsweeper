import sqlite3


def createUserRecDB(DBpath):
    TBname = 'Record'
    TBkey = '(UserName TEXT, Time INTEGER, STEP INTEGER)'
    conn = sqlite3.connect(DBpath)
    cursor = conn.cursor()
    executeStr = 'CREATE TABLE IF NOT EXISTS '+TBname+' '+TBkey
    cursor.execute('DROP TABLE IF EXISTS '+TBname)
    cursor.execute(executeStr)
    # print(executeStr)
    print('\n# --------------------------------------------------------- #')
    print('Create database ' + '"' + DBpath + '"' + ', table ' +
          '"' + TBname + '"' + ' successfully')
    print('# --------------------------------------------------------- #')
    conn.commit()
    conn.close()


def insertDataUserRec(DBpath, data):
    TBname = 'Record'
    conn = sqlite3.connect(DBpath)
    cursor = conn.cursor()
    executeStr = 'INSERT INTO ' + TBname + \
        ' (UserName, Time, STEP) VALUES (?, ?, ?)'
    cursor.execute(executeStr, data)
    print('\n# --------------------------------------------------------- #')
    print('Insert into DB table "Record" successfully, value: '+str(data))
    print('# --------------------------------------------------------- #')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    DBpath = '../instance/User.db'
    # TBname = 'Record'
    # TBkey = '(UserName TEXT, Time INTEGER, STEP INTEGER)'
    createUserRecDB(DBpath)

    data = ('Qian Zehao', 1, 2)
    insertDataUserRec(DBpath, data)
    data = ('Qian LinYuan', 3, 4)
    insertDataUserRec(DBpath, data)
