def merge(left, right):
    res = []

    while left and right:
        # <= - for stability
        res.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    res.extend(left + right)

    return res


# TODO: make buffer array init?
# TODO: sort on passed array?
def merge_sort(a):
    if len(a) < 2:
        return a

    mid = len(a) // 2
    
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    return merge(left, right)


