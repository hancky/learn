from functionX import *

def test_calSumInt():
    assert(calSum(10,20) == 310)
    #print("\nthis is {} test case".format(__name__))

def test_calSumFloat():
    assert (calSum(11.0, 11.2) == 23.2)

def test_calSumNagetive():
    assert (calSum(100,-200) == -100)