def loan_calculator(rate, org_prin, term):
    monthly_rate = (rate/12)/(100) #Converts mortgage interest rate into a monthly decimal 
    months = term  * 12 # Converts the choosen annual term dates into months
    balance = org_prin 
    monthly_payment = balance * monthly_rate/(1 - (1 + (monthly_rate))**(-(term * 12)))
    schedule = []
     
    for month in range(months):
        interest = balance * monthly_rate #Calculates monthly interest 
        principal = monthly_payment - interest #Calculates minthly principal
        balance -= principal #Calculates end of month mortgage balance
        schedule.append({"Month" : month + 1, "Principal Payment": principal, "Interest": interest, "Remaining Balance": balance}) #Adds a dictionary inside of a list 
    return schedule 
    
print(loan_calculator(int(input("What is the interest rate?")), int(input("What is the loan amount?")), int(input("What is the term?"))))
