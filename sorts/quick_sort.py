def lomuto_partition(a, lb, rb):
    pivot = a[rb]
    i = lb
    for j in range(lb, rb):
        if a[j] <= pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[rb], a[i] = a[i], a[rb]
    return i


def quick_sort_lomuto(a, lb, rb):
    if lb < rb:
        p = lomuto_partition(a, lb, rb)
        quick_sort_lomuto(a, lb, p - 1)
        quick_sort_lomuto(a, p + 1, rb)


def hoare_partition(a, lb, rb):
    pivot = a[(lb + rb) // 2]
    i, j = lb - 1, rb + 1
    while True:

        i += 1
        while a[i] < pivot:
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


def quick_sort_hoare(a, lb, rb):
    if lb < rb:
        p = hoare_partition(a, lb, rb)
        quick_sort_hoare(a, lb, p)
        quick_sort_hoare(a, p + 1, rb)


def quick_sort(a, partition='hoare'):
    if partition == 'hoare':
        # print('hoare!')
        quick_sort_hoare(a, 0, len(a) - 1)
    else:
        # print('lomuto!')
        quick_sort_lomuto(a, 0, len(a) - 1)


