print("Welcome to a rollercoaster ride!")
height = int(input("Whats your height in cm?\n "))
bill = 0

if height >= 120:
    print("you can ride on the rollercoaster")
    age = int(input("whats your age"))
    if age < 12:
        bill = 5
        print("you ll pay $5")
    elif age <= 18:
        bill = 7
        print("you will pay $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("you pay 0$")
    else:
        bill = 12
        print("you will pay $12")
   
    
    want_photo = str(input("type in 'Y' for yes and 'N' for No"))
    if want_photo == "Y":
     bill += 3     
       
else:
    print("Sorry, you can not ride on the rollercoaster")
print(f"total bill is {bill}")


        