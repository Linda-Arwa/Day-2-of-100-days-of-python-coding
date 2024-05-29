# A program that tells us how many days, weeks and months we have if we live until 90 years old.
# It takes your current age as the input and outputs a message with our time left in this format below:
# You have x days , y weeks and z months left.

# Solution

Current_age = input("Enter your current age\n")

#Converting age to an integer
Current_age = int(Current_age)

#Calclating the remaining years
years_left = 90 - Current_age

#Calculating the months
months = years_left * 12
# 12 because a year has 12 months

#Calculating the weeks
weeks = years_left * 52
# 52 becaue a year has 52 weeks

# Calculating the days
days = years_left * 365
# 365 because a year consists of 365 days

print(f"You have {days} days, {weeks} weeks and {months} months left")
