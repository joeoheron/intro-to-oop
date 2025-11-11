print('Tip Calculator\n')

# Request the meal cost and desired tip percent from the user and store both in variables.
meal_cost = float(input('Cost of meal:\t'))
tip_percent = float(input('Tip percent:\t'))

# Calculate and store the tip amount in a variable.
tip_amount = round(meal_cost * (tip_percent / 100), 2)

# Display the tip amount and calculate and display the total meal cost to the user.
print(f'\nTip amount:\t{tip_amount}')
print(f'Total amount:\t{round(meal_cost + tip_amount, 2)}')
