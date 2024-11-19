def quick(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    item_big = []
    item_small = []

    for item in sequence:
        if item > pivot:
            item_big.append(item)
        else:
            item_small.append(item)

    return quick(item_small) + [pivot] + quick(item_big)


print(quick([12,56,34,1,2,7,56,78,32,21,54,8,6]))