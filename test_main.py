"""
Test goes here
"""
from mylib import add,treat

def test_func():
    assert add(2,8) == 10
    print("You are adding correctly")


def test_func2():
    return treat('Sam','Samantha')

if __name__ == "__main__":
    assert test_func() == 2
  
  