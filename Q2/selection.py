def selection(lst):
    index_length = range(0,len(lst)-1)

    for i in index_length:
        min_value = i

        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j

        if min_value != i:
            lst[min_value],lst[i] = lst[i],lst[min_value]


    return lst

print(selection([2,77,4,56,21,34,78,65,32,12,11,4,8,57]))