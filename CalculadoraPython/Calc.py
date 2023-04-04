#Teste de edição e versionamento remoto
# Add math lib so i can use sqrt operation
import math

# Printing the operations options for the users
print("Select the operation you want to perform:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Square root")
print("6 - Percentage")

# Asking for user to choose the operation
option = input("Enter your choice (1/2/3/4/5/6): ")

# If user option is sqrt, ask to input the respective value
if option == '5':
    num = float(input("Enter a number: "))
    result = math.sqrt(num)

# If user option is %, ask to input the total value and the % they want to calculate
elif option == '6':
    num1 = float(input("Enter the total value: "))
    num2 = float(input("Enter the percentage (without the % symbol): "))
    result = (num1 / 100) * num2

# If user option is one of the basic operations, then ask the user to type 2 values they want to calculate
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == '1':
        result = num1 + num2
    elif option == '2':
        result = num1 - num2
    elif option == '3':
        result = num1 * num2
    elif option == '4':
        result = num1 / num2
    # In case of user types a wrong value...
    else:
        print("Invalid option")
        exit()

# Printing the results
print("Result: ", result)
