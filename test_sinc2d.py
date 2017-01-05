from sinc2d import *
import numpy as np

def test_x0():
    x0 = np.sin(45)/45
    assert x0 == sinc2d(0,45)

def test_y0():
    y0 = np.sin(45)/45
    assert y0 == sinc2d(45,0)

def test_corner():
    x0 = 1.0
    assert x0 == sinc2d(0,0)

def test_normal():
    x = 45
    y = 45
    exp = (np.sin(x)/x)*(np.sin(y)/y)
    assert exp == sinc2d(45,45)
