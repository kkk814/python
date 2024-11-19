#dictionary of the square of the given number

def sq_dict(n):
    square_dict = {x: x * x for x in range(1,n+1)}
    return square_dict

num = int(input("enter the number "))
print(sq_dict(num))