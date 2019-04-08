#!/usr/local/bin/python3
#-*- encoding=utf-8 -*-
import pytest
import sys
sys.path.append(".")
from two_sum import two_sum
from two_sum import two_sum_fast as two_sum

def test_two_sum_1():
    test_list = [2, 7, 11, 15]
    test_target = 9

    assert two_sum(test_list, test_target) == [0, 1]


def test_two_sum_2():
    test_list = [1]
    target = 1 

    assert two_sum(test_list, target) == [None, None]


def test_two_sum_3():
    test_list = [1, 2]
    target = 4

    assert two_sum(test_list, target) == [None, None]
