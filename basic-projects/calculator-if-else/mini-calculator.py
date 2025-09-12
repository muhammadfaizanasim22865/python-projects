# Mini calculator using if-else and elif statement

first = float(input('Enter your 1st number: '))
operator = input('Enter your operator (+, -, *, /, //, %, **): ')
second = float(input('Enter your 2nd number: '))

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    if second != 0:
        print(first / second)
    else:
        print("Error: Division by zero is not allowed")
elif operator == '//':
    if second != 0:
        print(first // second)
    else:
        print("Error: Floor division by zero is not allowed")
elif operator == '%':
    if second != 0:
        print(first % second)
    else:
        print("Error: Modulus by zero is not allowed")
elif operator == '**':
    print(first ** second)
else:
    print('Invalid operation')




