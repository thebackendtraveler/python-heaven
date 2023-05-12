#!python3

def hourly_pay(hours, rate):
    return hours * rate

def monthly_pay(years_experience, pay_notch):
   return years_experience * pay_notch

import calculatepay

hourly = calculatepay.hourly_pay(40,10)
monthly = calculatepay.monthly_pay(10,50)

print("Hourly worker pay: ", hourly)
print("Salary worker pay:  ", monthly)

import calculatepay as pay

hourly = pay.hourly_pay(40,10)   # use pay instead of calculatepay
monthly = pay.monthly_pay(10,50)

print("Hourly worker pay: ", hourly)
print("Salary worker pay:  ", monthly)

from calculatepay import hourly_pay as pay

hourly = pay(40,10)   # use pay is now used like a local method name

print("Hourly worker pay: ", hourly)

from calculatepay import hourly_pay, monthly_pay # imports specific functions
from calculatepay import * # imports all functions


