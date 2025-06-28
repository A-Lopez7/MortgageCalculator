import csv
from tabulate import tabulate

# LoanCalculator Project
# What it does: Calculates mortgage monthly payments, interest, principal, and builds amortization schedule
# Still to do: finish generate_schedule, display_table, export_to_csv

def collect_userinput(): #Collets user information which will be used in the class LoanCalculator

    ask_loan = float(input("What is the loan amount?\n"))
    ask_rate = float(input("What is the interest rate\n"))
    ask_term = int(input("What is the term?\n"))
    ask_extra = float(input("Extra monthly payment amount:\n"))

    if int(ask_term) > 30:
        input("Please provide a term less than 30 years")
        if int(ask_term) <= 30:
            pass
        return ask_loan, ask_rate, ask_term, ask_extra
    else:
        return ask_loan, ask_rate, ask_term, ask_extra


class LoanCalculator: #Calculates mortgage monthly payments, interest, principal, and builds amortization schedule
    def __init__(self, original_principle, rate, term, extra):
        self.original_principle = original_principle
        self.rate = rate
        self.term = term
        self.balance = original_principle
        self.monthly_rate = (self.rate/12)/(100)
        self.months = self.term * 12
        self.extra = extra


    def monthly_payment(self):

        if self.rate == 0:

            self.monthly_rate = 0
            self.months = self.term * 12
            self.monthly_amount = self.original_principle / (self.term * 12)
            return self.monthly_amount

        else:
            self.monthly_rate = (self.rate / 12) / 100
            self.months = self.term * 12
            self.monthly_amount = self.original_principle * self.monthly_rate / (1 - (1 + (self.monthly_rate)) ** (-(self.term * 12)))
            return self.monthly_amount


    def interest_payment(self): #Returns the monthly interest payment

        if self.rate == 0:
            self.monthly_rate = 0
            return 0
        elif self.rate != 0:
            return self.balance * self.monthly_rate

    def principal_payment(self): #Returns monthly principal payment
        return self.monthly_amount - self.interest_payment() + self.extra #Equation to calculate monthly principal payment

    def generate_schedule(self):
        self.schedule = []

        self.monthly_amount = self.monthly_payment()

        for month in range(self.months):
            self.interest_payment()
            self.principal_payment()
            self.balance -= round(self.principal_payment(), 2)
            self.schedule.append({"Month": month + 1, "Monthly Payment": self.monthly_payment(), "Principal Payment": self.principal_payment(), "Interest": self.interest_payment(), "Remaining Balance": self.balance})
            if self.balance < 0:
                for item in self.schedule:
                    for key, value in item.items():
                        item["Remaining Balance"] = 0
                    return tabulate(self.schedule, headers="keys", tablefmt="grid")
        return tabulate(self.schedule, headers="keys", tablefmt="grid")

    def export_to_csv(self):
        user_choice = input("Would you like to export this information into a csv file?")

        if user_choice.lower() == "yes":

            with open("MortgagePaymentSchedule.csv", "w", newline='') as amortization:
                self.writer = csv.DictWriter(amortization, fieldnames=["Month", "Monthly Payment", "Principal Payment", "Interest", "Remaining Balance"])
                self.writer.writeheader()
                self.writer.writerows(self.schedule)
            return "File has been successfully exported!"
        else:
            return "Thank you for using the mortgage app!\n"





ask_loan, ask_rate, ask_term, ask_extra = collect_userinput()
mortgage_app = LoanCalculator(ask_loan, ask_rate, ask_term, ask_extra)
print(mortgage_app.generate_schedule(), mortgage_app.export_to_csv())



