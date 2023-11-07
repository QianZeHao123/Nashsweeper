import sys
sys.path.append('..')

if __name__ == '__main__':
    from coreCalc import valst_gen
    valst = valst_gen(3)
    print(valst)
