import csv
from datetime import datetime

CSV_NAME = './expenses.csv'

def addExpense():
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))~

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(CSV_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully.")

def viewExpenses():
    print("Date\t\t\tCategory\tDescription\tAmount")
    try:
        with open(CSV_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def generateReport():
    expenses = {}
    try:
        with open(CSV_NAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, category, description, amount = row
                month = date[:7] 
                amount = float(amount)
                if month not in expenses:
                    expenses[month] = 0
                expenses[month] += amount
        
        print("Month\t\tTotal Expense")
        for month, total in expenses.items():
            print(f"{month}\t{total}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            addExpense()
        elif choice == '2':
            viewExpenses()
        elif choice == '3':
            generateReport()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
