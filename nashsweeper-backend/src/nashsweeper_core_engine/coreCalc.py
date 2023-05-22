# =================================================================
# Nashsweeper Core Computing Engine
# Using numpy, sqlite3 and itertools
# =================================================================
from itertools import product
# import numpy
import sqlite3
# =================================================================

# this part is used to generate id_lst.
# User X has n strategies, and his strategy list index is from 0 to n-1.


def atom_lst_gen(n):
    lst = [_ for _ in range(n)]
    return lst


def users_strategy_lst_gen(UserStrategyNum):
    users_strategy_lst = []
    for _ in UserStrategyNum:
        users_strategy_lst.append(atom_lst_gen(_))
    return users_strategy_lst

# generate strategy_combination by using iterator


def strategy_combination_lst_gen(users_strategy_lst):
    strategy_combination = product(*users_strategy_lst)
    strategy_combination = list(strategy_combination)
    return strategy_combination


def id_lst_gen(strategy_combination):
    id_lst = []
    for strategy in strategy_combination:
        strategy = "_".join(map(str, strategy))
        id_lst.append(strategy)
    return id_lst
# =================================================================


# =================================================================
# this part is related to database
# If here exists N gamers, it will generate a column for each user to store their payoff.
def valst_gen(N):
    valst_pre = []
    for _ in range(N):
        str_atom = 'Payoff' + str(_) + ' ' + 'NUMBER'
        valst_pre.append(str_atom)
    valst = ", ".join(valst_pre)
    return valst


class SQLLiteProcess(object):
    def __init__(self, N, Dataset):
        self.N = N
        self.Dataset = Dataset
    # create the database, id, Payoff1, Payoff2,..., PayoffN

    def create_database(DBname, TBname, N):
        DBname += '.db'
        valst = valst_gen(N)
        id_info = 'id TEXT PRIMARY KEY,'
        conn = sqlite3.connect(DBname)
        cursor = conn.cursor()
        executeStr = 'CREATE TABLE IF NOT EXISTS ' + \
            TBname + '(' + id_info + valst + ')'
        cursor.execute(executeStr)
        conn.commit()
        conn.close()
    # insert data(id, Payoff1, Payoff2,..., PayoffN) into database

    def insert_data(DBname, TBname, N, Dataset):
        valst_pre = []
        for _ in range(N):
            str_atom = 'Payoff' + str(_) + ' '
            valst_pre.append(str_atom)
        valst = ", ".join(valst_pre)
        insertTab = 'id, ' + valst
        DBname += '.db'
        val_pre = tuple(['?' for i in range(N+1)])
        val = ', '.join(val_pre)
        conn = sqlite3.connect(DBname)
        cursor = conn.cursor()
        executeStr = 'INSERT INTO'+' ' + TBname + \
            ' ' + '(' + insertTab + ')' + ' ' + \
            'VALUES' + ' ' + '(' + val + ')'
        cursor.executemany(executeStr, Dataset)
        conn.commit()
        conn.close()

    def search_data(DBname, TBname, keyword, id):
        DBname += '.db'
        conn = sqlite3.connect(DBname)
        cursor = conn.cursor()
        executeStr = 'SELECT' + ' ' + keyword + ' ' + 'FROM' + ' ' + TBname + \
            ' ' + 'WHERE' + ' ' + 'id' + '=' + '?'
        cursor.execute(executeStr, (id,))
        result = cursor.fetchall()
        conn.close()
        return result[0][0]
# =================================================================


# =================================================================
# Regret Value Calculation
# =================================================================

if __name__ == "__main__":
    Dataset = [
        ('0_0_0', 1, 2, 3),
        ('0_0_1', 4, 5, 6),
        ('0_1_0', 12, 42, 34),
        ('0_1_1', 34, 22, 27),
        ('1_0_0', 42, 56, 23),
        ('1_0_1', 93, 26, 6),
        ('1_1_0', 23, 68, 54),
        ('1_1_1', 57, 23, 11)
    ]
    # SQLLiteProcess.create_database('TestDB', 'TestTB', 3)
    # SQLLiteProcess.insert_data('TestDB', 'TestTB', 3, Dataset)
    print(SQLLiteProcess.search_data('TestDB', 'TestTB', 'Payoff1', '0_0_0'))
    # print(SQLLiteProcess.search_data('TestDB', 'TestTB', '0_1_0'))

    # test_strategy_matrix = [[76, 97], [72, 67], [25, 84],
    # [73, 46], [93, 20], [12, 44], [68, 93], [20, 87], [43, 24],
    # [68, 44], [62, 97], [72, 66], [96, 16], [42, 3], [14, 44],
    # [51, 37], [63, 40], [76, 86], [43, 66], [13, 63],
    # [6, 92], [15, 15], [68, 19], [69, 77], [49, 90], [29, 43],
    # [75, 93], [18, 70], [0, 31], [99, 96], [5, 71], [4, 5],
    # [50, 68], [69, 52], [22, 59], [57, 37], [60, 5], [1, 93],
    # [55, 64], [45, 51], [46, 18], [87, 12], [32, 0], [37, 85],
    # [43, 3], [70, 93], [53, 62], [26, 18], [80, 8], [85, 13],
    # [54, 80], [37, 43], [23, 11], [91, 48], [85, 57], [53, 25],
    # [71, 90], [35, 57], [87, 98], [57, 32], [41, 25], [28, 94], [100, 14], [68, 53]]

    # test_strategy_matrix_array = numpy.array(
    #     test_strategy_matrix).reshape(8, 8, 2)

    # data_input_size = list(test_strategy_matrix_array.shape)
    # UserStrategyNum = data_input_size[:-1]
    # N = data_input_size[-1]

    # users_strategy_lst = users_strategy_lst_gen(UserStrategyNum)
    # strategy_combination = strategy_combination_lst_gen(users_strategy_lst)
    # id_lst = id_lst_gen(strategy_combination)
    # # print(id_lst)

    # DatabaseData = []
    # for _ in range(len(id_lst)):
    #     tupChild = (id_lst[_], test_strategy_matrix[_]
    #                 [0], test_strategy_matrix[_][1])
    #     DatabaseData.append(tupChild)

    # print(DatabaseData)

    # create_database('testDB', 'testTB', N)
    # insert_data('testDB', 'testTB', DatabaseData)
    # create_database('TestDB', 'TestTB', 6)
