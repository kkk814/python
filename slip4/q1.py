#min max in set

my_set = set()

def add():
    size = int(input("enter the size of set "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number "))
        my_set.add(num)

def maximum(s):
    max_value = max(s)
    print(f"\nmax value in set is {max_value}")

def minimum(s):
    min_value = min(s)
    print(f"\nmin value in set is {min_value}")


add()
maximum(my_set)
minimum(my_set)
