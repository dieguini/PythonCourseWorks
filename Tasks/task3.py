"""
Loan payment calculator
"""

# Get the details of the loan from the user: How much money do you owe, in dollars?​
from calendar import month


loan_input = input('How much money do you owe, in dollars?\n')
# Convert input to float​
money_owed = float(loan_input)
# Get the annual percentage rate: what us the annual percentage rate?​
apr_input = input('what us the annual percentage rate?\n')
apr = float(apr_input)
# Get the monthly payment: what will your monthly payment be, in dollars?​
monthly_payment_input = input('what will your monthly payment be, in dollars?\n​')
payment = float(monthly_payment_input)
# Get  months to calculate results: how many months do you want to see the results for?​
months_input = input('how many months do you want to see the results for?\n')
months = int(months_input)
# Repeat the calculation for all the months the user  wants to see results for​
for month_count in range(1,months+1):
    print('\nMonth',month_count)
# Divide annual percentage rate by 100 to make it a percent, then divide by 12 to get the monthly insterest rate
#   monthly_rate = apr/100/12
    monthly_rate = apr / 100 / 12
# add in  interest
#   interest_paid = money_owed * monthly_rate
    interest_paid = money_owed * monthly_rate
#   money_owed = money_owed + interest_paid
    money_owed = money_owed + interest_paid
# Make payment
    money_owed = money_owed - payment
# Print the results 
    print("Paid", round(payment,2), "of which", interest_paid, "was interest")
    print("Now, I owe", round(money_owed,2))


# add control to check if money_owed - payment < 0 then print messages and break repetition
# round the dollar amount to two decimals   
    if money_owed - payment < 0:
        print("the last payment is", round(money_owed,2))
        break
    else:
        print("You pay off the loan in", month_count, "months")