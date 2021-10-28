import math

en = input("Employee Name: ")
noHours = int(input("Enter number of Hours: "))
sss = int(input("SSS contribution: "))
ph = int(input("Phil Health: "))
hl = int(input("Housing Loan: "))
ratePerH = 500.0
gs = noHours*ratePerH

print("="*10,"PAYSLIP","="*10)
print("="*5,"EMPLOYEE INFORMATION","="*5)

info = f""" 
Employee Name: {en}
Rendered Hours: {noHours}
Rate per Hour: 500
Gross Salary: {gs}

"""
print(info)

tax = gs*0.1
td = sss+ph+hl+tax
ns = gs-td
print("="*10,"DEDUCTIONS","="*10)
dd = f""" 
SSS: {sss}
PhilHealth: {ph}
Other Loan: {hl}
Tax: {tax}
Total Deduction: {str(td)}

NET Salary: PHP {str(ns)}
"""
print(dd)
