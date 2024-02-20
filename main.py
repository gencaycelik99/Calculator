def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2


number1 = int(input("Enter 1th number : "))
number2 = int(input("Enter 2nd number : "))

choice = input("\n1-) Addition\n2-) Subtraction\nYour Choice : ")

if choice == "1":
    result = addition(number1, number2)
    print(f"{number1} + {number2} = {result}")

elif choice == "2":
    result = subtraction(number1, number2)
    print(f"{number1} - {number2} = {result}")

