#adding two dictionary

from collections import Counter

d1 = {'a':100,'b':200,'c':300}

d2 = {'a':300,'b':200,'d':400}

new_dict = dict(Counter(d1)+Counter(d2))

print("new dictionary is ",new_dict)