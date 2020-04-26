# TODO: refactor
def fmt(a, rb):
    b = a[:]
    b.insert(rb + 1, '|')
    s = ' '.join(str(b).split(', ')).replace('\'', '')
    return s


def bubble_sort(a):
    for rb in range(len(a) - 1, 0, -1):
        # print('->')
        # print('rb = %s: %s' % (rb, fmt(a, rb)))

        swapped = False

        for i in range(rb):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # print('rb = %s: %s' % (rb, fmt(a, rb)))

        if not swapped:
            # print('no swap => sorted (rb = %s)' % rb)
            return

    # print('single number left => sorted')


