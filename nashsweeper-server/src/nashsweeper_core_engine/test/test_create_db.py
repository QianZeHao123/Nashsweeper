import sys
sys.path.append('..')

if __name__ == '__main__':
    from coreCalc import SQLLiteProcess
    N = 6
    SQLLiteProcess.create_database('TestDB', 'TestTBB', N)
