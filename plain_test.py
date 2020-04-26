from sorts.bubble_sort import bubble_sort as sort_fun
from utilities import apply_sort

ret_val = False

# bounds check
apply_sort(sort_fun, [1, 2, 7, 6, 5, 4, 3, 8, 9], ret_val)

# break check
apply_sort(sort_fun, [5, 1, 2, 3, 4], ret_val)

# last-min problem
apply_sort(sort_fun, [2, 3, 4, 5, 1], ret_val)

# empty check
apply_sort(sort_fun, [], ret_val)

# single check
apply_sort(sort_fun, [5], ret_val)

# equality check
apply_sort(sort_fun, [7, 7], ret_val)

# pivot division check
apply_sort(sort_fun, [-5, 5, -9], ret_val)

# additional
apply_sort(sort_fun, [16, 11, 9, 10, 5, 6, 8, 1, 2, 4], ret_val)
