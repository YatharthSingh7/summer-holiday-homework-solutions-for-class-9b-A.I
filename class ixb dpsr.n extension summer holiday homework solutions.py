# program 1
# print('YATHARTH','SINGH','IX','B','DPS','R.N','EXTENSION',sep='@',end='#')
# program 2
# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
'''celsius =  int(input("enter temperature in celsius  : "))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))'''
# program 3
'''p= float(input('enter principal'))
r= float(input('enter rate '))
t= float(input('enter time in months '))
T= t/12
si= (p*r*T)/100
print ('simple intrest is ',si)'''
#program 4
'''r = float(input('enter the radius'))
p = 3.14159265358979323846
a=(r*r*p)
print('the area of a circle with is',a)'''
#program 5
'''r = float(input('enter the radius'))
p = 3.14159265358979323846
h= float(input('enter the height'))
v= (p*r*r*h)
print('volume of cylinder is ',v)'''
#program 6
'''def convert_cm_to_feet_inches(height_cm):
    # Convert centimeters to inches
    height_inches = height_cm / 2.54

    # Convert inches to feet and remaining inches
    height_feet = int(height_inches // 12)
    height_remaining_inches = int(height_inches % 12)

    return height_feet, height_remaining_inches


# Ask for user input
height_cm = float(input("Enter your height in centimeters: "))

# Convert height to feet and inches
feet, inches = convert_cm_to_feet_inches(height_cm)

# Display the result
print("Your height is {} feet {} inches.".format(feet, inches)'''
#program 7
def calculate_triangle_area(base, height):
    # Calculate the area of the triangle
   ''' area = 0.5 * base * height
    return area

# Ask for user input
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
triangle_area = calculate_triangle_area(base, height)

# Display the result
print("The area of the triangle is:", triangle_area)'''
# program 8
'''def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def modulus(a, b):
    return a % b
def floor_divide(a, b):
    return a // b
print("Enter two integers:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Floor Division (//)")
choice = int(input("Enter your choice (1-6): "))
if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
elif choice == 5:
    print("Result:", modulus(num1, num2))
elif choice == 6:
    print("Result:", floor_divide(num1, num2))
else:
    print("Invalid choice! Please enter a number between 1 and 6.")'''
# Program 9
'''X= int(input('enter a number'))
if(X%2==0):
 print('Even ')
else:
    print('Odd')'''
num1=float(input("Number 1 : "))
num2=float(input("Number 2 : "))
if num1>num2:
    print("Number1 is greater than Number2")
elif num1<num2:
    print("Number1 is less than Number2")
else:
    print("Number1 is equal to Number2")


