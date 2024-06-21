import pytest
from main import summ

def test_1():
    assert summ(4, 5) == 9

def test_2():
    assert summ(5, 5) == 10
