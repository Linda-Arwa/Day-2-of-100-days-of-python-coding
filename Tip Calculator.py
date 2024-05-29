# A program that calculates the bill each person pays after adding a tip to it.abs

# Solution

print("Welcome to the bill calculator")

bill = input("What is the total bill in Uganda Shillings?\n")

bill = float(bill)

tip = input("what percentage tip would you like to give? 10, 12 or 15? Just kindly put the number, exclude the percentage sign\n")

tip = float(tip)

tip = (tip/100) * bill

# Calculating the new bill
new_bill = bill + tip

# People splitting the bill
people = input("How many people split the bill?\n")

people = int(people)

payment = new_bill / people

payment = float(payment)

payment = round(payment , 2)

print(f"Each person should pay: Ugx {payment}")



