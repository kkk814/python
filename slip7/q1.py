#reverse the array

array = []
r_array = []

def add():
    size = int(input("enter the size of array "))
    for i in range(size):
        num = int(input(f"enter the {i+1}th number \n"))
        array.append(num)
    print("normal array is ",array)
    print("\n\n")

def reverse(arr):
    return arr[::-1]
    

add()
r = reverse(array)
print(f"array after reverse operation is {r}")