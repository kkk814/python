#average of number in a list
numbers = []

size = int(input("enter size of the list "))

for _ in range(size):
    num = int(input(f"enter the {_+1}th element in list "))
    num = numbers.append(num)

print(f"your list is {numbers}")

avg = sum(numbers)/len(numbers)

print(f"average of list is {avg}")