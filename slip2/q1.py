#duplicate or unique

numbers = []

print("enter the numbers ")

for i in range(6):
    num = int(input(f"enter the {i+1}th number "))
    numbers.append(num)

if len(numbers) != len(set(numbers)):
    print("DUPLICATES")
else:
    print("unique")