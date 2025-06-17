height = float(input("WHat is your height\n"))
weight = int(input("What is your weight\n"))
bmi = weight / (height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, your re underweight")
elif bmi <= 25:
    print("normal weight")
elif bmi <=30:
    print("slightly overage")
elif bmi <= 35:
    print("obese")
else:
    print("clinically obese")
    
    
    
    
