"""
This module is for creating a simple plot using non-standard library 
matplotlib. We will use matplotlib to create a simple plot of days of the week and 
simulation temperatures during those days.

Ensure matplotlib is installed prior to running script: 
`pip install matplotlib`
"""

# Import library/module
import matplotlib.pyplot as plt

# Days of the week
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

# Simulated Tempuratures for each day
temps = [22, 21, 34, 24, 20, 15, 25]

# Create a plot
plt.plot(days, temps, marker='o', linestyle='-', color='black')

# Create labels for x and y axis and Title
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (\u00B0C)')
plt.title('Weekly Temperature')

# Show the Grid
plt.grid(True)

# Display the plot
plt.show()