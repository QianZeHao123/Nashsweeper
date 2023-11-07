from TestData import test_strategy_matrix
import sys
import numpy
# print(test_strategy_matrix)
sys.path.append('..')


if __name__ == '__main__':

    from coreCalc import users_strategy_lst_gen, strategy_combination_lst_gen, id_lst_gen
    from coreCalc import SQLLiteProcess
    # import test_strategy_matrix data
    from TestData import test_strategy_matrix

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
