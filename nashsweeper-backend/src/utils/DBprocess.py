import sqlite3


# def createDB(DBname, TBname, TBkey):
#     # DBname = '../instance/User.db'
#     conn = sqlite3.connect(DBname)
#     cursor = conn.cursor()
#     executeStr = 'CREATE TABLE IF NOT EXISTS '+TBname+' '+TBkey
#     cursor.execute('DROP TABLE IF EXISTS '+TBname)
#     cursor.execute(executeStr)
#     # print(executeStr)
#     print('---------------------------------------------------------')
#     print('Create database ' + DBname + ', table ' + TBname + ' successfully')
#     print('---------------------------------------------------------')
#     conn.commit()
#     conn.close()


# def insertData(DBname, TBname, data):
#     conn = sqlite3.connect(DBname)
#     cursor = conn.cursor()
#     executeStr = 'INSERT INTO'+' '+TBname+' values(?,?,?);'
#     cursor.execute(executeStr, data)
#     print('Insert Data to table' + TBname + ' successfully')
#     conn.commit()
#     conn.close()

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
