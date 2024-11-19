pos = -1

def binary(lst,n):

    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (upper + lower) // 2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                lower = mid
            else:
                upper = mid

elements = [12,45,23,67,89,34,1,2,56,22,11,106,9]
elements.sort()
print(f"sorted list is {elements}")

n = 23

if binary(elements,n):
    print(f"element is at {pos}")
else:
    print("not found")