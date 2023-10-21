# Remember to import from the lab11 file and pytest
import pytest
import random 
import statistics
import lab11
from operator import add, mul 
import math 


# Write your test code here for Q1 and Q2

def test_product():
    pass

def test_summation():
    pass

def test_accumulate():
    pass

def test_product_short():
    pass

def test_summation_short():
    pass

# Q3
#####################################

def test_square():
    """Write your code here"""


def test_sqrt():
    """Write your code here"""


def test_mean():
    """Write your code here"""


def test_median():
    """Write your code here"""


def test_mode():
    """Write your code here"""
    with pytest.raises(ValueError):
        mode('not a list')
        mode(1)   
        mode(1.234) 
    assert mode([1,2, 3, 4, 5, 6]) == 3


def test_std_dev():
    """Write your code here"""


def test_stat_analysis():
    """Write your code here"""


# OPTIONAL
#####################################

def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
