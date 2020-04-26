from math import log2


def print_heap(a, k):
    if a:
        print('{}{}'.format(' ' * 4 * int(log2(k + 1)), a[k]))

    if 2 * k + 1 < len(a):
        print_heap(a, 2 * k + 1)

        if 2 * k + 2 < len(a):
            print_heap(a, 2 * k + 2)


def sift_down(a, i, n):
    while 2 * i + 1 < n:
        ch_i = 2 * i + 1

        if ch_i + 1 < n and a[ch_i + 1] > a[ch_i]:
            ch_i += 1

        if a[i] >= a[ch_i]:
            break

        a[i], a[ch_i] = a[ch_i], a[i]
        i = ch_i


def heap_sort(a):
    for i in range(len(a) // 2 - 1, -1, -1):
        sift_down(a, i, len(a))

    # print('heap:')
    # print_heap(a, 0)

    for n in range(len(a) - 1, 0, -1):
        a[0], a[n] = a[n], a[0]
        # print('swap %s and %s:' % (a[0], a[n]))
        # print_heap(a, 0)

        sift_down(a, 0, n)
        # print('after down:')
        # print_heap(a, 0)

