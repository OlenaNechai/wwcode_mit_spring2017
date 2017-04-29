# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:06:53 2017

@author: Olena
"""

annual_salary = float(input('Please enter the starting annual salary: '))
portion_saved = float(input('Please enter the portion of salary to be saved, as a decimal: '))
total_cost = float(input('Please enter the cost of your dream home: '))
semi_annual_raise = float(input('Please enter the semi-annual raise, as a decimal: '))

portion_down_payment = float(total_cost*0.25)
current_savings = float(0)
r = float(0.04)
monthly_salary = float(annual_salary)/float(12.0)
month = int(0)

while current_savings < portion_down_payment:
    current_savings += (monthly_salary*portion_saved) + (current_savings*r)/12
    month += 1
    if month%6 == 0:
        annual_salary += semi_annual_raise * annual_salary;
        monthly_salary = float(annual_salary)/float(12.0)
    
    
print('Number of months: ', month)