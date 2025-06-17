name1 = input()
name2 = input()
print("The Love Calculator is calculating your score...")
combine_names = name1 + name2
lower_names = combine_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e
score = str(first_digit) + str(second_digit)
score_int = int(str(first_digit)) + int(str(second_digit))
if (score_int < 10) or (score_int > 90):
  print(f"Your score is {score}, you go together like coke and mentos. ")
elif (score_int >= 40) and (score_int <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")








