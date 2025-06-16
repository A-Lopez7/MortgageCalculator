import csv
from tabulate import tabulate

def loan_calculator(rate, org_prin, term):
    monthly_rate = (rate/12)/(100) #Converts mortgage interest rate into a monthly decimal 
    months = term  * 12 # Converts the choosen annual term dates into months
    balance = org_prin 
    monthly_payment = balance * monthly_rate/(1 - (1 + (monthly_rate))**(-(term * 12)))
    schedule = []
     
    for month in range(months):
        interest = balance * monthly_rate #Calculates monthly interest 
        principal = monthly_payment - interest #Calculates minthly principal
        balance -= round(principal, 2) #Calculates end of month mortgage balance and rounds to the nearest hundredth
        schedule.append({"Month" : month + 1, "Principal Payment": principal, "Interest": interest, "Remaining Balance": balance}) #Adds a dictionary inside of a list
        amort_list = schedule #stores the dictionary

    return amort_list

def amort_table(list):

    with open("amort_table.csv", "w", newline="") as amortization:
        writer = csv.DictWriter(amortization, fieldnames=["Month", "Principal Payment", "Interest", "Remaining Balance"])
        writer.writeheader()
        writer.writerows(list)

    return list

ask_user = loan_calculator(float(input("What is the interest rate?")), float(input("What is the loan amount?")), int(input("What is the term?")))
print(tabulate((ask_user), headers="keys", tablefmt="fancy_grid"))
