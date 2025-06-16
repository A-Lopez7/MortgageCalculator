import csv
from tabulate import tabulate

intro_response = input("Hi! Welcome to Simple Mortgage Calculator. Would you like to calculator your monthly mortgage payment? Yes or No\n")

def loan_calculator(org_princinple, rate, term):
    schedule = []

    if rate == 0:
        monthly_rate = 0
        months = term * 12
        balance = org_princinple
        monthly_payment = balance/(term*12)
    else:
        monthly_rate = (rate / 12) / (100)  # Converts mortgage interest rate into a monthly decimal
        months = term * 12  # Converts the choosen annual term dates into months
        balance = org_princinple
        monthly_payment = balance * monthly_rate / (1 - (1 + (monthly_rate)) ** (-(term * 12)))

    for month in range(months):
        interest = balance * monthly_rate #Calculates monthly interest 
        principal = monthly_payment - interest #Calculates minthly principal
        balance -= round(principal, 2) #Calculates end of month mortgage balance and rounds to the nearest hundredth
        schedule.append({"Month" : month + 1, "Monthly Payment": monthly_payment, "Principal Payment": principal, "Interest": interest, "Remaining Balance": balance}) #Adds a dictionary inside of a list


    if schedule[-1]["Remaining Balance"] <= 100:
        schedule[-1]["Remaining Balance"] = 0
    else:
        pass

    return schedule

def amort_table(list):

    with open("amortizationtable.csv", "w", newline="") as amortization:
        writer = csv.DictWriter(amortization, fieldnames=["Month", "Monthly Payment", "Principal Payment", "Interest", "Remaining Balance"])
        writer.writeheader()
        writer.writerows(list)

    return list

loan_amount = input("What is the loan amount?")
interest_rate = input("What is the interest rate?")
term_length = input("What is the term?")

if intro_response.lower() == "yes":
    ask_user = loan_calculator(float(loan_amount), float(interest_rate), int(term_length))
    print("Here's an amortization table with your monthly payment along with a break down of your monthly principal vs. interest payment\n:", tabulate((ask_user), headers="keys", tablefmt="fancy_grid"))

elif intro_response.lower() == "no":
    exit()


 