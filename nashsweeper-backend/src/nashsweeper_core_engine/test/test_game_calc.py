import sys
import random
# import numpy
sys.path.append('..')

if __name__ == '__main__':
    from CoreCalcOptForGame import CoreCalc
    # import TestData
    # from TestData import test_strategy_matrix
    # generate a list of 128 numbers, each of which is from 0 to 100
    test_strategy_matrix = [random.randint(0, 100) for _ in range(128)]
    strategy_matrix = test_strategy_matrix
    regP1, regP2 = CoreCalc.regCalc(strategy_matrix)
    # calculate the regret value of regP1 and regP2
    print(regP1)
    print(regP2)
    # output the nash equilibrium list and best response of player 1 and player 2
    NE, BRP1, BRP2 = CoreCalc.BRNElst(regP1, regP2)
    print(NE)
    print(BRP1)
    print(BRP2)
