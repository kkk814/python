pos = -1

def search(lst,n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False

arr = [5,8,4,6,9,2]

n = 4

if search(arr,n):
    print(f"found at {pos}")
else:
    print("not found")