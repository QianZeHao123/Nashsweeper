from TestData import test_strategy_matrix
import sys
import numpy
# print(test_strategy_matrix)
sys.path.append('..')


if __name__ == '__main__':

    from coreCalc import users_strategy_lst_gen, strategy_combination_lst_gen, id_lst_gen
    from coreCalc import SQLLiteProcess

    test_strategy_matrix = [[76, 97], [72, 67], [25, 84], [73, 46], [93, 20], [12, 44], [68, 93], [20, 87], [43, 24], [68, 44], [62, 97], [72, 66], [96, 16], [42, 3], [14, 44], [51, 37], [63, 40], [76, 86], [43, 66], [13, 63], [6, 92], [15, 15], [68, 19], [69, 77], [49, 90], [29, 43], [75, 93], [18, 70], [0, 31], [99, 96], [5, 71], [
        4, 5], [50, 68], [69, 52], [22, 59], [57, 37], [60, 5], [1, 93], [55, 64], [45, 51], [46, 18], [87, 12], [32, 0], [37, 85], [43, 3], [70, 93], [53, 62], [26, 18], [80, 8], [85, 13], [54, 80], [37, 43], [23, 11], [91, 48], [85, 57], [53, 25], [71, 90], [35, 57], [87, 98], [57, 32], [41, 25], [28, 94], [100, 14], [68, 53]]

    # import test_strategy_matrix data
    # from TestData import test_strategy_matrix

    test_strategy_matrix_array = numpy.array(
        test_strategy_matrix).reshape(8, 8, 2)

    data_input_size = list(test_strategy_matrix_array.shape)
    UserStrategyNum = data_input_size[:-1]
    N = data_input_size[-1]
    print('N = ' + str(N))

    users_strategy_lst = users_strategy_lst_gen(UserStrategyNum)
    strategy_combination = strategy_combination_lst_gen(users_strategy_lst)
    id_lst = id_lst_gen(strategy_combination)
    # print(id_lst)

    DatabaseData = []
    for _ in range(len(id_lst)):
        tupChild = (id_lst[_], test_strategy_matrix[_]
                    [0], test_strategy_matrix[_][1])
        DatabaseData.append(tupChild)

    print(DatabaseData)

    SQLLiteProcess.create_database('testDB', 'testTB', N)
    SQLLiteProcess.insert_data('testDB', 'testTB', N, DatabaseData)

    