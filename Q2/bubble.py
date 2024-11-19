def bubble(lst):
    index_length = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,index_length):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst

print(bubble([2,7,3,1,6,8,9,3,4,10,33,11,12,41,10]))