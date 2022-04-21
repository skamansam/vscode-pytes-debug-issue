from lorem_text import lorem


# content of test_sample.py
def func(x):
    # slowness starts around 1500
    for i in range(10000):
       print(lorem.paragraph())
    return x + 1


def test_fail():
    assert func(3) == 5 
    assert func(4) == 4

def test_success():
    assert func(3) == 4
    assert func(4) == 5
