#fibonacci sequence

def fibonacci(n):
    a = 0
    b = 1

    l = [0,1]

    for i in range(2,n):

        c = a + b
        a = b
        b = c
        l.append(c)
    return l

num = int(input("enter the number "))
print(fibonacci(num))