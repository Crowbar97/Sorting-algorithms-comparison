def find_min(a, i):
    k = i
    for j in range(i + 1, len(a)):
        if a[j] < a[k]:
            k = j
    return k


# not stable version
def selection_sort(a):
    for i in range(len(a) - 1):
        k = find_min(a, i)
        a[i], a[k] = a[k], a[i]

