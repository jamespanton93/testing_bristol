from mean import *

def test_ints():
    input = [1,2,3,4,5]
    calc_val = mean(input)
    exp_val = 3
    assert calc_val == exp_val

def test_float():
    input = [1.0, 2.0, 3.0, 4.0, 5.0]
    calc_val = mean(input) 
    exp_val = 3
    assert calc_val == exp_val

def test_negative():
    input = [1, -2, 3, -4, 5]
    calc_val = mean(input)              
    exp_val = 0.6
    assert calc_val == exp_val
