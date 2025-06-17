print("Welcome to the tip calculator ")
bill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill"))
tip = int(input("what pecentage of tip would you like to give? 10, 12, or 15 "))
tip_percentage = tip/100
total_tip_percentage = bill * (1+ tip_percentage)
individual_bill = total_tip_percentage / people
final_amount =round(individual_bill, 2)
print(f"Each person should pay :{final_amount}")