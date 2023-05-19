# =================================================================
# Nashsweeper Core Computing Engine
# Using numpy, sqlite3 and itertools
# =================================================================

from itertools import product
import numpy
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
def create_database(DBname, TBname, valst):
    conn = sqlite3.connect(DBname)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS UserStrategy(
                id TEXT PRIMARY KEY,
                strategy TEXT)''')
    conn.commit()
    conn.close()
# =================================================================

'''
if __name__ == "__main__":
    test_strategy_matrix = [[76, 97], [72, 67], [25, 84], [73, 46], [93, 20], [12, 44], [68, 93], [20, 87], [43, 24],
                            [68, 44], [62, 97], [72, 66], [96, 16], [42, 3], [14, 44], [
                                51, 37], [63, 40], [76, 86], [43, 66], [13, 63],
                            [6, 92], [15, 15], [68, 19], [69, 77], [49, 90], [29, 43], [
                                75, 93], [18, 70], [0, 31], [99, 96], [5, 71], [4, 5],
                            [50, 68], [69, 52], [22, 59], [57, 37], [60, 5], [1, 93], [
        55, 64], [45, 51], [46, 18], [87, 12], [32, 0], [37, 85],
        [43, 3], [70, 93], [53, 62], [26, 18], [80, 8], [85, 13], [
        54, 80], [37, 43], [23, 11], [91, 48], [85, 57], [53, 25],
        [71, 90], [35, 57], [87, 98], [57, 32], [41, 25], [28, 94], [100, 14], [68, 53]]

    test_strategy_matrix = numpy.array(test_strategy_matrix).reshape(8, 8, 2)
    # print(test_strategy_matrix)
    data_input_size = list(test_strategy_matrix.shape)
    UserStrategyNum = data_input_size[:-1]
    N = data_input_size[-1]

    users_strategy_lst = users_strategy_lst_gen(UserStrategyNum)
    strategy_combination = strategy_combination_lst_gen(users_strategy_lst)
    id_lst = id_lst_gen(strategy_combination)
    print(id_lst)
    print(N)
'''
# the following code is used to test unit
