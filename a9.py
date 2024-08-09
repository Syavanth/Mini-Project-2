def find_minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

min_number = find_minimum(number1, number2)
print(f"The minimum of {number1} and {number2} is {min_number}")
