with open('file1.txt') as file:
    list1 = [int(item) for item in file.readlines()]
with open('file2.txt') as file:
    list2 = [int(item) for item in file.readlines()]
result = [item for item in list1 if item in list2]
# Write your code above 👆

print(result)


