#
# Name Luke Guild
# Date 9/8/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
state_tax = 0.05
county_tax = 0.025
# Constants for the state and county tax rates

# Get the amount of the purchase.
purchase_amount = int(input('Enter purchase amount: '))
# Calculate the state sales tax.
total_state_tax = state_tax * purchase_amount
# Calculate the county sales tax.
total_county_tax = county_tax * purchase_amount
# Calculate the total tax.
total_tax = total_state_tax + total_county_tax
# Calculate the total of the sale.
total_sale_cost = total_tax + purchase_amount
# Print information about the sale.
print(f'The amount of purchase is ${purchase_amount:.2f}.')
print(f'The state tax is ${total_state_tax:.2f}.')
print(f'The county tax is ${total_county_tax:.2f}.')
print(f'The total tax is ${total_tax:.2f}.')
print(f'The total cost of purchase is ${total_sale_cost:.2f}.')