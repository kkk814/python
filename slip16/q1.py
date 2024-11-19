#list of tuples number square reverse list

my_list = []

def add():
    size = int(input("enter the size of array "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number \n"))
        my_list.append(num)
    print("\n\n")

    tuple_list = [(num,num**2) for num in my_list]

    print("list of tuples",tuple_list)

    print("reverse of list is ",my_list[::-1])


add()