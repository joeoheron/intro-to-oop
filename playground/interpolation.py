first_name = input('What\'s your first name?\n')
last_name = input('What\'s your last name?\n')

x = float(input('Choose an "x" value to perform a calculation\n'))
calculation = input('What calculation would you like to perform?\n')
y = float(input('Choose an amount you\'d like to add to "x"\n'))

result_text = f'Hi {first_name}, the result of your calculation is'

if calculation == '+' or calculation == 'add':
    print(result_text, round(x + y, 2))
elif calculation == '-' or calculation == 'subtract':
    print(result_text, round(x - y, 2))
elif calculation == 'multiply' or calculation == '*' or calculation == 'x':
    print(result_text, round(x * y, 2))
elif calculation == '/' or calculation == 'divide':
    print(result_text, round(x / y, 2))
else:
    print(f'Hi {first_name}, you haven\'t entered an appropriate calculation.')