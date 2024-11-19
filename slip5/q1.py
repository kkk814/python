#array of n elements

array = []

def add():
    size = int(input("enter the size of array "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number \n"))
        array.append(num)
    print("\n\n")

def display(a):
    for i in range(len(a)):
        print(f"index is {i} element is {a[i]}\n")


add()
display(array)

