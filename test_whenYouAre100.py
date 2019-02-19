import pytest
from hypothesis import given, settings
import hypothesis.strategies as st
from hypothesis.database import ExampleDatabase
from whenYouAre100 import *

@given(st.integers(min_value=0,max_value=101))
#@settings(database=ExampleDatabase('***'))
def test_forhundred(i):
    person = Person('Sha', i)
    assert person.whenyouturnhundred() == 2019 + (100-i)

def test_forhundred():
    person = Person('Sha',100)
    assert person.whenyouturnhundred() == 2019

def test_forzero():
    person = Person('Sha',0)
    assert person.whenyouturnhundred() == 2119

def test_forgreaterthanhundred():
    person = Person('Sha',101)
    assert person.whenyouturnhundred() == 2018

def test_somenumber():
    person = Person('Sha',50)
    assert person.whenyouturnhundred() == 2069
