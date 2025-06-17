names_string = input("Whats are your names?")
names = names_string.split(", ")
import random
num_item = len(names)
random_choice = random.randint(0, num_item-1)
print(f"{names[random_choice]} is going to buy the meal today")

# other code but does not work on website
# names = names_string.split(", ")
# import random
# num_item = len(names)
# random_choice = random.randint(0, num_item-1)
# print(names[random_choice])