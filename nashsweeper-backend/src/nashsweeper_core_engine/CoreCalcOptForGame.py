# =================================================================
# Nashsweeper Core Solver Optimized for Nashweeper Game
# =================================================================
import numpy


class CoreCalc(object):
    def __init__(self, strategy_matrix):
        self.strategy_matrix = strategy_matrix

    def regCalc(strategy_matrix):
        strategy_matrix = numpy.array(strategy_matrix).reshape(64, 2)
    # print(strategy_matrix)
        strategy_matrix = numpy.hsplit(strategy_matrix, 2)
        # print(p1[0])
        '''
        [[ 4 15 62  0  3 87 32 49]
        [37 19 25  1  0 57 86 18]
        [17 11 44 60 90 84 32  0]
        [31 58 12 55 96  0 95 65]
        [30 18 65 16 36 98 45 24]
        [34  0 55 36 53 29 47 43]
        [ 0  2 33 36 73  8 15 16]
        [ 9 52  0 16 55 71  0  1]]
        '''
        P1 = strategy_matrix[0].reshape(8, 8)
        P2 = strategy_matrix[1].reshape(8, 8)
        # The best strategy of P1 is column.
        P1max = numpy.max(P1, axis=0)
        # The best strategy of P2 is row.
        P2max = numpy.max(P2, axis=1).reshape(8, 1)
        # calculate the regret values
        # based on the numpy broadcast mechanism
        regP1 = P1max-P1
        regP2 = P2max-P2
        # regP1 = regP1.reshape(64)
        # a = numpy.where(regP1 == 0)
        # b = list(a[0])
        # print(b)
        return regP1, regP2

    def BRNElst(regP1, regP2):
        regP1 = regP1.reshape(64)
        P1zero = numpy.where(regP1 == 0)
        P1zero = list(P1zero[0])
        regP2 = regP2.reshape(64)
        P2zero = numpy.where(regP2 == 0)
        P2zero = list(P2zero[0])
        NE = [_ for _ in P1zero if _ in P2zero]
        BRP1 = [_ for _ in P1zero if _ not in NE]
        BRP2 = [_ for _ in P2zero if _ not in NE]
        return NE, BRP1, BRP2
