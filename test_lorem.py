from lorem_text import lorem
from numpy import number

# adjust this to determine slowness.
# slowness starts around 1500 for me
number_lines_output = 10000

# content of test_sample.py
def func(x):
    for i in range(number_lines_output):
       print(lorem.paragraph())
    return x + 1


def test_fail():
    assert func(3) == 5 
    assert func(4) == 4

def test_success():
    assert func(3) == 4
    assert func(4) == 5
