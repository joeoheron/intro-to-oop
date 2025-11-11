print('Price Comparison\n')

# Store the large and small sizes as variables.
large_size = 64
small_size = 32

# Request the price of the large and small sizes from the user and store those prices in variables.
large_detergent_price = float(input('Price of 64 oz size:\t'))
small_detergent_price = float(input('Price of 32 oz size:\t'))

# Display the price per ounce for the user.
print(f'\nPrice per oz (64 oz):\t{round(large_detergent_price / large_size, 2)}')
print(f'Price per oz (32 oz):\t{round(small_detergent_price / small_size, 2)}')
