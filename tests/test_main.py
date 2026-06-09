import sys; sys.path.insert(0,'..')
from solutions.main import *

def test_max_sum_k():
    assert max_sum_k([2,1,5,1,3,2],3) == 9
    assert max_sum_k([1,4,2,9,7,3,8],3) == 20

def test_longest_unique():
    assert longest_unique("abcabcbb") == 3
    assert longest_unique("bbbbb") == 1
    assert longest_unique("pwwkew") == 3
    assert longest_unique("") == 0

def test_find_anagrams():
    assert find_anagrams("cbaebabacd","abc") == [0,6]
    assert find_anagrams("baa","aa") == [1]

def test_longest_k_distinct():
    assert longest_k_distinct("eceba",2) == 3
    assert longest_k_distinct("aa",1) == 2

def test_max_ones_flip():
    assert max_ones_after_flip([1,1,0,0,1,1,1],2) == 6
    assert max_ones_after_flip([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3) == 10

def test_sliding_max():
    assert sliding_window_max([1,3,-1,-3,5,3,6,7],3) == [3,3,5,5,6,7]
