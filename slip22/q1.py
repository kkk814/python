#repeated item in tuple

from collections import Counter

def rep_item(input_tuple):
    cnt = Counter(input_tuple)
    dup_item = [item for item,count in cnt.items() if count > 1]
    return dup_item

my_tuple = (1,2,2,2,3,2,5,6,6,7,8,9,0,9,8,8)

print("repeated items are",rep_item(my_tuple))