#sum of elements in a list

my_list = []

def add():
    size = int(input("enter the size of array "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number \n"))
        my_list.append(num)
    print("\n\n")

def sum_list(l):
    addition = 0
    for i in range(len(l)):
        addition += my_list[i]
    print(f"sum of the elements in list is :{addition}")
    

add()
sum_list(my_list)