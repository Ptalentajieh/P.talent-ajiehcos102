print("Program to calculate Annuity Plan")
pmt = 200
r = 34
n =  2
t = 5
b = ((1 + (r/n))^n*t) - 1
a = pmt*((b)/(r/n))