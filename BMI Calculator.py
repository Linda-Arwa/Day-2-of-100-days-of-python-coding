# A program  that calculates the Body Mass Index (BMI) from a user's weight and height.
# BMI = Weight(Kg)/height*height(m**2)
# Convert the result to a whole number

# Solution

weight = input("Enter your weight in Kgs\n")
height = input("Enter your height in metres\n")

print(type(weight))
print(type(height))

weight = float(weight)
height = float(height)

BMI = (weight) / (height*height)

BMI = int(BMI)

print("Your Body Mass Index is" + " " + str(BMI))
