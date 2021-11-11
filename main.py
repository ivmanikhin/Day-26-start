# with open('file1.txt') as file:
#     list1 = [int(item) for item in file.readlines()]
# with open('file2.txt') as file:
#     list2 = [int(item) for item in file.readlines()]
# result = [item for item in list1 if item in list2]
# # Write your code above 👆
#
# print(result)
from random import randint

names = ['Angela', 'Jack', 'Nick', 'Sally', 'Molly', 'Steve', 'Alex']

scores = {'Angela': 48466, 'Jack': 38775, 'Nick': 96570, 'Sally': 35578, 'Molly': 94529, 'Steve': 42846, 'Alex': 31953}
print(scores)

passed = {name: score for (name, score) in scores.items() if score > 90000}
print(passed)
