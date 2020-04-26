# TODO: refactor
def fmt(a, lb, rb):
    b = a[:]
    b.insert(rb + 1, '|')
    b.insert(lb, '|')
    s = ' '.join(str(b).split(', ')).replace('\'', '')
    return s


def shaker_sort(a):
    fwd = True
    lb, rb = 0, len(a) - 1
    while lb < rb:
        # print('->' if fwd else '<-')
        # print(fmt(a, lb, rb))

        swapped = True
        if fwd:
            for i in range(lb, rb):
                if a[i] > a[i + 1]:
                    swapped = False
                    a[i], a[i + 1] = a[i + 1], a[i]
                    rb = i
        else:
            for i in range(rb, lb, -1):
                if a[i] < a[i - 1]:
                    swapped = False
                    a[i], a[i - 1] = a[i - 1], a[i]
                    lb = i

        # print(fmt(a, lb, rb))

        if swapped:
            # print('no swap => sorted')
            return

        fwd = not fwd

    # print('single number in bounds => sorted')

