from fib import *

def test_fib_4():
    fib4 = 1 + 1 + 2 + 3 + 5 
    assert fib4 == fib(4)

def test_fib_1():
    fib1 = 1 
    assert fib1 == fib(1)

def test_fib_0():
    fib0 = 1
    assert fib0 == fib(0)
