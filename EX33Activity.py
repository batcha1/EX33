# Aly Batch
# 10.11.19
# While Loops

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append (i)

    i = i + 1
    print("Number now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
