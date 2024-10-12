# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program


total_sales = float(input('Enter your total sales: '))

def county_tax():
    c_tax = .025
    total_tax = total_sales*c_tax
    return total_tax

def state_tax():
    s_tax = .05
    total_tax = total_sales * s_tax
    return total_tax

def main():
    print('County sales tax: ', county_tax())
    print('State sales tax: ', state_tax())
    print('total sales tax: ', county_tax()+state_tax())

main()