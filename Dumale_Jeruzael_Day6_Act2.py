from GrossSalary import *
from NetSalary import *
from SalaryDeductions import *

name = input("Name: ")
hour = int(input("Hours of work: "))
loan = float(input("Loan: "))
hi = float(input("Health Insurance: "))

gs = getGrossSalary(hour)
deductions = getSalaryDeductions(gs, loan, hi)
ns = showNetSalary(gs, deductions)

txt = f"""

Name: {name}
Hours of work: {hour}
Loan: Php {loan}
Insurance: Php {hi}

Total Deduction: Php {deductions}

Net salary: Php {ns}

"""

print(txt)
