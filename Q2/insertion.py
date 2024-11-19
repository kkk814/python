def insertion(lst):
    index_length = range(1,len(lst))
    for i in index_length:
        value_to_sort = lst[i]

        while lst[i-1] > value_to_sort and i>0:
            lst[i],lst[i-1] = lst[i-1],lst[i]
            i = i - 1

    return lst


print(insertion([22,1,2,56,78,64,2,32,12,36,53,21]))