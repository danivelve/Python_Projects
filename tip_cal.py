print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
percentage_tip = 1 + tip / 100
bill = total_bill * percentage_tip
number_split_bill = int(input("How many people to split the bill? "))
bill_per_person = round((bill / number_split_bill),2)
print("Each persosn sshould pay: %s" %(bill_per_person))
print(f"Each persosn should pay: {bill_per_person}")
