# Body mass index (BMI)

# Get wight
wight = float(input('Enter your wight (kg)  '))

# Get height
height = float(input('Enter your height (m)  '))

# Check if enter by centimetre
if height > 100:
    height = height / 100

# Calculate bmi (with round up to 2 digits)
BMI = round(wight / (height ** 2), 2)

print('your bmi is ', BMI)

# Print state
if BMI <= 18.49:
    print('You are Underweight')
elif 24.99 >= BMI >= 18.5:
    print('You are in Neural weight')
elif 29.99 >= BMI >= 25:
    print('You are Over Wight')
elif 30 <= BMI:
    print('You are Fat!')
