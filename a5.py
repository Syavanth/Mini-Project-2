def palindrome_or_not(num):
    original = num
    reverse = 0

    while num > 0  :
        last = num % 10 
        reverse = reverse*10 + last
        num = num//10

    return original == reverse

number = int(input("enter a number:"))

if palindrome_or_not(number):
    print(number,"is a palindrome")
else:
    print(number,"is not a palindrome")
