import csv
import pandas as pd 
import matplotlib.pyplot as plt
# Add Expense
def add_expense():
    while True:
        name = input("Enter name: ").strip()
        if name == "":
            print("Name cannot be empty")
        elif not name.replace("", "").isalpha():
            print("Name must contain only letters")
        else:
            break
    valid_categories = ["Food", "Travel", "Gaming", "Bills"]    
    while True:
        category = input("Enter category (Food/Travel/Gaming/Bills): ").strip()
        if category in valid_categories:
            break
        else:
            print("Invalid category. Choose from list")
    while True: 
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
            else:
                break
        except ValueError:
            print("Enter a valid number")
   
    with open (r"D:\kichu\data.csv", "a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name, category, amount])

    print("Expense added successfully!")

# View Data
def view_data ():
    data = pd.read_csv(r"D:\kichu\data.csv")
    print(data)

# Analysis
def dashboard():

    data = pd.read_csv("data.csv")

    if data.empty:
        print("\n❌ No data available\n")
        return

    result = data.groupby("Category")["Amount"].sum()

    total = data["Amount"].sum()
    highest = result.max()
    top_category = result.idxmax()

    print("\n" + "="*40)
    print("        📊 EXPENSE DASHBOARD")
    print("="*40)

    print("\n📌 CATEGORY BREAKDOWN")
    for cat, amt in result.items():
        print(f"  - {cat:<10} : {amt}")

    print("\n📌 SUMMARY")
    print(f"  Total Expense   : {total}")
    print(f"  Top Category    : {top_category} ({highest})")

    print("\n" + "="*40 + "\n")

# Chart
def show_graph():
    data = pd.read_csv(r"D:\kichu\data.csv")
    result = data.groupby("Category")["Amount"].sum()

    plt.pie(result.values, labels=result.index, autopct='%1.1f%%')
    plt.title("Expense distribution")
    plt.show()

# Main Menu 
while True:
    print("\n=== Expense Tracker ===")
    print("[1]. Add Expense")
    print("[2]. View Data")
    print("[3]. Dashboard")
    print("[4]. Show Graph")
    print("[5]. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_data()
    elif choice == "3":
        dashboard()
    elif choice == "4":
        show_graph()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
    
