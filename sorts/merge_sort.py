def merge(left, right):
    res = []

    while len(left) > 0 and len(right) > 0:
        # <= - for stability
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res.extend(left)
    res.extend(right)

    return res


# TODO: sort on passed array?
def merge_sort(a):
    if len(a) < 2:
        return a

    mid = len(a) // 2
    
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    res = merge(left, right)

    return res


