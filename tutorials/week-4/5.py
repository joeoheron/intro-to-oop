print('Travel Time Calculator\n')

# Prompt the user for the amount of miles they are going and their speed in MPH.
miles = int(input('Enter miles:\t\t'))
miles_per_hour = int(input('Enter miles per hour:\t'))

# Calculate the amount of hours with integer division, find the remaining minutes with module division, and store those values as variables.
hours = miles // miles_per_hour
minutes = miles % miles_per_hour

# Display the amount of time it will take the user to travel their specified distance at their specified speed.
print(f'\nEstimated travel time\nHours:\t\t\t{hours}\nMinutes:\t\t{minutes}')
