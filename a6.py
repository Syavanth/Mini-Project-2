def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    original_num = num
    
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_digits
        num = num // 10
    
    return original_num == sum_of_powers

number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
