from pyapp.data import Data
from pyapp.calc import func

def test_calc1():
    d1 = Data(1)
    d2 = Data(2)
    d3 = func(d1, d2)
    assert d3.value == 3
