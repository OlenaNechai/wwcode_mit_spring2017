# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:22:17 2017

@author: Olena

"""
'''
You are now going to try to find the best rate of savings
to achieve a down payment on a $1M house in 36 months.
Since hitting this exactly is a challenge, we simply want your 
savings to be within $100 of the required down payment.
1.Your semiannual raise is .07 (7%) 
2.Your investments have an annual return of 0.04 (4%) 
3.The down payment is 0.25 (25%) of the cost of the house 
4.The cost of the house that you are saving for is $1M.
'''
def savings36(portion_saved, current_savings, annual_salary, semi_annual_raise):
    month = int(0)
    annual_salary += semi_annual_raise * annual_salary
    monthly_salary = float(annual_salary)/float(12.0)
    
    while month < 36:
        current_savings += (monthly_salary*portion_saved) + (current_savings*r)/12
        month += 1
        if month%6 == 0:
            annual_salary += semi_annual_raise * annual_salary;
            monthly_salary = float(annual_salary)/float(12.0)
        
    return current_savings

annual_salary = float(input('Please enter the starting annual salary: '))

semi_annual_raise = float(0.07)
portion_down_payment = float(1000000*0.25)
current_savings = float(0)
r = float(0.04)

epsilon = 100
num_guesses = 0
low = 0
high = 1.0
savings_rate = (high + low)/2.0
savings = savings36(savings_rate, current_savings, annual_salary, semi_annual_raise)      

if savings + 100 <= portion_down_payment: 
    print('It is not possible to pay the down payment in three years.')

while abs(savings - portion_down_payment) >= epsilon:
    if savings < portion_down_payment:
        low = savings_rate
    else:
        high = savings_rate
    savings_rate = (high + low)/2.0
    num_guesses += 1
    savings = savings36(savings_rate, current_savings, annual_salary, semi_annual_raise)
    
print('Steps in bisection search:', num_guesses)
print('Best savings rate: ', round(savings_rate, 4))