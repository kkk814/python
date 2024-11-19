#occurance of element

array = []

def add():
    size = int(input("enter the size of array "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number \n"))
        array.append(num)
    print("\n\n")

add()




aset = set(array)

for item in aset:
    x = array.count(item)
    print(item,':',x,'times')