print('Pay Check Calculator\n')

# Store the hours worked and the hourly pay rate in variables.
hours_worked = float(input('Hours Worked:\t\t'))
hourly_pay = float(input('Hourly Pay Rate:\t'))

# Calculate and display the gross pay based on the hours worked and the pay rate from earlier.
gross_pay = hours_worked * hourly_pay
print(f'\nGross Pay:\t\t{gross_pay}')

# Request the user's tax rate and calculate the tax amount on their paycheck, storing both in variables.
tax_rate = round(float(input('Tax Rate:\t\t').replace('%','')), 2)
tax_amount = round(gross_pay * (tax_rate / 100), 2)

# Display the amount of tax taken out of the user's paycheck and their net pay.
print(f'Tax Amount:\t\t{tax_amount}')
print(f'Take Home Pay:\t\t{round((gross_pay - tax_amount), 2)}')
