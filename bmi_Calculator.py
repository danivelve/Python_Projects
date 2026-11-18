height = input("enter your height\n")
weight = input("enter your weight\n")
heightInt = float(height)
weight_in_float = float(weight)
bmi = weight_in_float / heightInt ** 2
print(f"your BMI {bmi}")