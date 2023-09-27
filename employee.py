"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = ""
        self.commission = ""

        self.total = 0
    
    def set_salary(self, salary):
        self.salary = salary

    def set_commission(self, commission):
        self.commission = commission

    def calculate_total(self):
        if self.salary:
            self.total = self.salary.salary
        
        if self.salary and self.commission:
            self.total += self.commission.bonus

    def get_pay(self):
        return self.total

    def __str__(self):
        return f"{self.name} works on {str(self.salary)}{str(self.commission)}. Their total pay is {self.total}."

class MonthlySalary:
    def __init__(self, salary):
        self.salary =  salary
    
    def __str__(self):
        return f"a monthly salary of {self.salary}"

class ContractSalary:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate =  rate
        self.salary = self.hours * self.rate
    
    def __str__(self):
        return f"a contract of {self.hours} hours at {self.rate}/hour"

class BonusCommission:
    def __init__(self, bonus):
        self.bonus =  bonus
    
    def __str__(self):
        return f" and receives a bonus commission of {self.bonus}"

class ContractCommission:
    def __init__(self, contracts, rate):
        self.contracts = contracts
        self.rate =  rate
        self.bonus = self.contracts * self.rate

    def __str__(self):
        return f" and receives a commission for {self.contracts} contract(s) at {self.rate}/contract"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_salary(MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_salary(ContractSalary(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_salary(MonthlySalary(3000))
renee.set_commission(ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_salary(ContractSalary(150, 25))
jan.set_commission(ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_salary(MonthlySalary(2000))
robbie.set_commission(BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_salary(ContractSalary(120, 30))
ariel.set_commission(BonusCommission(600))

employees = []
employees.append(billie)
employees.append(charlie)
employees.append(renee)
employees.append(jan)
employees.append(robbie)
employees.append(ariel)

for employee in employees:
    employee.calculate_total()
    # print(str(employee))
    # print(employee.get_pay())
