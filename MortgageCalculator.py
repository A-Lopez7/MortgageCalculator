import csv
from tabulate import tabulate

# LoanCalculator Project
# What it does: Calculates mortgage monthly payments, interest, principal, and builds amortization schedule
# Still to do: finish generate_schedule, display_table, export_to_csv

def collect_userinput(): #Collets user information which will be used in the class LoanCalculator
    ask_loan = float(input("What is the loan amount?\n"))
    ask_rate = float(input("What is the interest rate\n"))
    ask_term = int(input("What is the term?\n"))
    return ask_loan, ask_rate, ask_term

class LoanCalculator: #Calculates mortgage monthly payments, interest, principal, and builds amortization schedule

    def __init__(self, original_principle, rate, term):
        self.original_principle = original_principle
        self.rate = rate
        self.term = term
        self.balance = original_principle
        self.monthly_rate = (self.rate/12)/(100)
        self.months = self.term * 12


    def monthly_payment(self): #Calculates monthly payment
        self.monthly_amount = round(self.balance * self.monthly_rate / (1 - ((1 + (self.monthly_rate)) ** -(self.term * 12))), 2) #Equation to calculate monthly payment
        return f'Your monthly payment is {self.monthly_amount}'

    def interest_payment(self): #Returns the monthly interest payment
        return self.balance * self.monthly_rate
        #return f'Your interest payment is {self.interest_amount}'

    def principal_payment(self): #Returns monthly principal payment
        return self.monthly_amount - self.interest_payment() #Equation to calculate monthly principal payment

    def generate_schedule(self):
        pass

    def display_table(schedule):
        pass

    def export_to_csv(self):
        pass

ask_loan, ask_rate, ask_term = collect_userinput()
test = LoanCalculator(ask_loan, ask_rate, ask_term)
print(test.monthly_payment(),test.principal_payment(), test.interest_payment())