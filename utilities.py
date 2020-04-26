from random import randint


def fun_name(fun):
    return str(fun).split()[1]


def generate_array(array_size, lb, rb):
    return [randint(lb, rb) for _ in range(array_size)]


def apply_sort(sort_fun, a, ret_val=False):
    print('-' * 50)
    print('INITIAL: %s' % a)

    if ret_val:
        a = sort_fun(a)
    else:
        sort_fun(a)

    print('SORTED: %s' % a)

