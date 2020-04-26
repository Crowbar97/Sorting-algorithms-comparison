from math import sqrt, exp


phi = (1 + sqrt(5)) / 2
fct = 1 / (1 - exp(-phi))


def comb_sort(a):
    d = len(a)
    swapped = True

    while swapped:
        d = int(d / fct)

        if d <= 1:
            d = 1
            swapped = False

        for i in range(len(a) - d):
            if a[i] > a[i + d]:
                a[i], a[i + d] = a[i + d], a[i]
                swapped = True

        # print('d = %s: %s' % (d, a))

