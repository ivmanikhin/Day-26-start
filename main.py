# with open('file1.txt') as file:
#     list1 = [int(item) for item in file.readlines()]
# with open('file2.txt') as file:
#     list2 = [int(item) for item in file.readlines()]
# result = [item for item in list1 if item in list2]
# # Write your code above 👆
#
# print(result)
from random import randint

# names = ['Angela', 'Jack', 'Nick', 'Sally', 'Molly', 'Steve', 'Alex']
#
# scores = {'Angela': 48466, 'Jack': 38775, 'Nick': 96570, 'Sally': 35578, 'Molly': 94529, 'Steve': 42846, 'Alex': 31953}
# print(scores)
#
# passed = {name: score for (name, score) in scores.items() if score > 90000}
# print(passed)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# words = {word: len(word) for word in sentence.split()}
# result = words
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: round(temp_c * 1.8 + 32, 2) for (day, temp_c) in weather_c.items()}


print(weather_f)