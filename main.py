"""
1. Multiplied number

Ask user to enter three numbers. If first number is > 10 write sum of second and third number to the console. If first number is <=10 write it directly to the console.
"""

num1 = int(input("Please enter number 1:\n\t"))
num2 = int(input("Please enter number 2:\n\t"))
num3 = int(input("Please enter number 3:\n\t"))

if num1 > 10:
    print("\n- The sum of the 2nd and 3rd numbers is {}.".format(num2 + num3))
else:
    print(f"\n- The first number is {num1}.")

# -------------------------------------------