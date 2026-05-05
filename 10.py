print(" == MONTHLY EXPENSE TRACKER == ")
Monthly_salary = float(input("[1/4]: Enter your salary: ₹"))
Travel_expense_monthly = float(input("[2/4]: Enter your monthly travel expense: ₹"))
while Travel_expense_monthly > Monthly_salary:
    print(f"Travel expense cannot exceed monthly salary - {Monthly_salary}")

    Travel_expense_monthly = float(input("[2/4]: Please enter a valid amount: ₹"))
   
Food_expense_monthly = float(input("[3/4]: Enter your monthly food expense: ₹"))
while Food_expense_monthly > Monthly_salary:
    print("Food expense should be less than Monthly salary")

    Food_expense_monthly = float(input("[3/4]: Please enter a valid amount: ₹"))

Savings = float(input("[4/4]: Enter your savings(%): "))
Remaining_balance1 = Monthly_salary - Travel_expense_monthly 
Remaining_balance2 = Remaining_balance1 - Food_expense_monthly 
Savings_amount = (Savings / 100 ) * Remaining_balance2
print(f"Your remaining balance is: ₹{Remaining_balance2}")
print(f"You save: ₹{Savings_amount} monthly")
Remaining_balance3 =  Remaining_balance2 - Savings_amount
print(f"Your remaining balance after savings is: ₹{Remaining_balance3}\n")

print(" == Monthly Summary == \n")
print(f"  Salary:          {Monthly_salary}\n")
print(f"  Travel expense:  {Travel_expense_monthly}\n")
print(f"  Food expense:    {Food_expense_monthly}")

print("  --------------------------------------------")

print(f"  Remaining balance:        {Remaining_balance2}\n")
print(f"  Savings amount:           {Savings_amount}\n")
print(f"  Final balance:            {Remaining_balance3}\n")
# Graph code 
import matplotlib.pyplot as plt 

categories = ["Food", "Travel", "Savings"]
amounts = [Food_expense_monthly, Travel_expense_monthly, Savings_amount]
plt.subplot(2,1,2)
plt.bar(categories,amounts)
plt.title("Monthly summary")

plt.show()

