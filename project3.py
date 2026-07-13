import csv

class FileIsEmptyError(Exception):
    pass

print("Welcome to your Expense Tracker.\n")

details = []
# Categories: (Food, Transport, Bills, Entertainment, etc.)

def save_expense(filename, expense_details):
    columns = ["title", "category", "amount", "date"]
    with open(filename, "w", newline="") as detail:
            content = csv.DictWriter(detail, fieldnames=columns)

            content.writeheader()
            content.writerows(expense_details)

def load_expense(filename):
    expense_details = []
    try:
        with open(filename, "r") as e_file:
            all_expenses = csv.DictReader(e_file)
            for expense in all_expenses:
                expense_details.append(expense)
            return expense_details
    except FileNotFoundError:
        print("The file needed does not exist")

def add_expense(filename, expense_details):
    e_title = input("Enter your expense title: ").capitalize().strip()
    category = input("What category is the expense? ").capitalize().strip()
    amount = float(input("How much was spent: "))
    date = input("Enter the date (use this format dd-mm-yyy): ").strip()

    try:
        if amount < 0:
            print("Wrong Amount. Your amount spent must not be less then 0")
        else:
            new_expense = {"title": e_title, "category": category, "amount": amount, "date": date}
        expense_details.append(new_expense)
        save_expense(filename, expense_details)
        print("\nYour expense has been successfully added.")

    except ValueError:
        print("Kindly input the amount in decimal number.")

    
def view_expense(filename):
    try:
        expenses = load_expense(filename)

        print("-"*76)
        print(f"|{'Index':<10}|{'Title':<15}|{'Category':<15}|{'Amount':<15}|{'Date':<15}|")
        print("-"*76)
        if len(expenses) > 0:
            for index, expense in enumerate(expenses, start=1):
                print(f"|{index:<10}|{expense['title']:<15}|{expense['category']:<15}|{expense['amount']:<15}|{expense['date']:<15}|")
        print("-"*76)
            
    except FileNotFoundError: 
        print("The required folder is not in the directory.")
    except FileIsEmptyError: 
        print("There are no expenses currently stored in the file. Add some expenses to view.")

def calculate(filename):
    num_calc =[]
    all_expenses = load_expense(filename)

    for expense in all_expenses:
        num_calc.append(float(expense["amount"]))

    total_expense = sum(num_calc)
    print(f"\nYour total expense is: {total_expense}")

def delete(filename):
    all_expenses = load_expense(filename)
    del_title = input("Enter the expense title you want to delete: ").capitalize().strip()

    for expense in all_expenses:
        if expense["title"] == del_title:
            all_expenses.remove(expense)
            save_expense(filename, expense_details=all_expenses)
            print("The expense has been deleted successfully.")
            return
    print("The expense inputted does not exit in the record. ")

def search(filename):
    cat = input("Enter the category of the expense you're searching for: ").capitalize().strip()
    try:
        all_expenses = load_expense(filename)
        same_cat = []
        for e in all_expenses:
            if e["category"] == cat:
                same_cat.append(e)

        if same_cat:
            for each_cat in same_cat:
                print(f"\nThe expense for the {each_cat['category']} category is ${each_cat['amount']} spent on {each_cat['date']}.")
        else:        
            print("\nThe expense you're searching does not exist in the record. ")
        
    except FileIsEmptyError:
        print("You have to upload your expenses first before you can search.")


while True:
    print("-"*76)
    ops = input("What operation would you like to perform? " 
    "\n\nChoose any of the following('add','view','calculate','delete','search','exit): ").lower().strip()

    if ops == "add":
        add_expense("expenses.csv", details)
    elif ops == "view":
        view_expense("expenses.csv")
    elif ops == "calculate":
        calculate("expenses.csv")
    elif ops == "delete":
        delete("expenses.csv")
    elif ops == "search":
        search("expenses.csv")
    elif ops == "exit":
        print("You're done with your expense update.")
        break
    else:
        print("Your input does not match any of teh required input.")
        break