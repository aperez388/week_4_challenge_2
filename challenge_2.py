# Anabel Perez, Ruby Solis-Chavez
from math import *
name = input("What is your name?")
soldThisMonth = float(input("How much have you sold this month?"))
commissions = (soldThisMonth*13/100)
print("Your name is " + name + " and you're entitled to $" + str(round(commissions, 2)) + " in commissions.")