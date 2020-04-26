from sorts.bubble_sort import bubble_sort
from sorts.shaker_sort import shaker_sort
from sorts.comb_sort import comb_sort
from sorts.insertion_sort import insertion_sort
from sorts.selection_sort import selection_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.heap_sort import heap_sort

from sorted_test import test_sort_fun


# SORT FUN TESTING
def test_sort_funs():
    # test_sort_fun(bubble_sort)
    # test_sort_fun(shaker_sort)
    # test_sort_fun(comb_sort)
    # test_sort_fun(insertion_sort)
    # test_sort_fun(selection_sort)
    # test_sort_fun(merge_sort, True)
    test_sort_fun(quick_sort)
    # test_sort_fun(heap_sort)


test_sort_funs()

