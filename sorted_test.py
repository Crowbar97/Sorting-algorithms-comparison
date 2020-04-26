from utilities import fun_name, generate_array


def test_sorted(a, b):
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            return False, i
    return True, None


def test_sort_fun(sort_fun, ret_val=False,
                  test_count=int(1e2),
                  array_size=int(1e2), unique_count=int(1e2),
                  rnd_params=False,
                  array_size_min=int(0), array_size_max=int(1e2),
                  unique_count_min=int(0), unique_count_max=int(1e2)):

    print('SORTED TEST:\nSORT FUN: %s' % fun_name(sort_fun))

    print('TEST COUNT: %s' % test_count)

    if rnd_params:
        print('RANDOM ARRAY SIZE AND UNIQUE COUNT')
    else:
        print('ARRAY SIZE: %s' % array_size)
        print('UNIQUE COUNT: %s' % unique_count)

    correct = True
    for i in range(test_count):
        if rnd_params:
            array_size = randint(array_size_min, array_size_max)
            unique_count = randint(unique_count_min, unique_count_max)
        lb = -(unique_count // 2) + (unique_count % 2 == 0)
        rb = unique_count // 2

        a = generate_array(array_size, lb, rb)
        b = a[:]

        if ret_val:
            a = sort_fun(a)
        else:
            sort_fun(a)

        succ, ind = test_sorted(a, b)

        if not succ:
            print('Error on a[%s] = %s and a[%s] = %s nums:'
                  % (ind, a[ind], ind + 1, a[ind + 1]))
            print('Initial:\n%s' % b)
            print('Sorted:\n%s' % a)
            correct = False
        else:
            # print('OK')
            # print('Initial:\n%s' % b)
            # print('Sorted:\n%s' % a)
            pass
    
    if correct:
        print('ALL TEST PASSED SUCCESSFULLY!')

