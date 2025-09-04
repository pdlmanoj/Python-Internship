import json
import os
class Expense: 

    uniq_id = 1

    def __init__(self, name, amount, exp_id = None):
        # to load existing data from file
        if exp_id is not None:
            self.id = exp_id
        else:
            self.id = Expense.uniq_id
            Expense.uniq_id += 1
        
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return f"[{self.id}] {self.name}: Rs{self.amount}"

class ExpenseTracker:

    def __init__(self, filename = 'Personal Expense Tracker/new.json'):
        self.filename = filename
        self.expenses = []
        self.load_expense_data() # loading existing expense data
    
    def load_expense_data(self):
        if not os.path.exists(self.filename):
            # if file not exist 
            self.expenses = [] # making sure it's empty
            return 
        # if file exist

        with open(self.filename, 'r') as rf:
            try:
                datas = json.load(rf)
                self.expenses = [] # making sure no data

                for data in datas:
                    self.expenses.append(Expense(data['name'], data['amount'],data['id']))
                # To ensure unique ID continues correctly, not again from 1
                if self.expenses:
                    max_id = max(data.id for data in self.expenses)
                    Expense.uniq_id = max_id + 1
            except json.JSONDecodeError: # if empty, or invalid JSON 
                self.expenses = []
    
    def save_expense_data(self):
        data = [{"id": i.id, "name": i.name, "amount": i.amount} for i in self.expenses]
        with open(self.filename, 'w') as wf:
            json.dump(data, wf, indent=4)
    
    def add_expense(self, name, amount):
        expense = Expense(name,amount)
        self.expenses.append(expense)
        self.save_expense_data()
        print(f"New Expense Added: {expense}")

    def update_expense(self, exp_id, new_name, new_amount):
        for data in self.expenses:
            if data.id == exp_id:
                data.name = new_name
                data.amount = new_amount
                self.save_expense_data()
                print(f"Updated expense ID: {exp_id}")
                return
        print(f"No expense found with ID: {exp_id}")


    def show_expenses(self):

        if not self.expenses:
            print("EMPTY!!")
            return
        for data in self.expenses:
            print(data)


    def remove_expense(self):
        user_choice = int(input('Enter Task ID: '))

        for data in self.expenses:
            if data.id == user_choice:
                self.expenses.remove(data)
                self.save_expense_data()
                print(f"Expense ID: {user_choice} deleted successfully")
                return
        else:
            print(f"NO expense data found with ID: {user_choice}")
        





#### TESTING#####

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense('watch', 20000)
    tracker.add_expense('iphone', 2000000)
    tracker.add_expense('book', 2000)
    tracker.show_expenses()
    tracker.add_expense('bag', 2000)
    tracker.update_expense(1, 'kcha', 444444)
    tracker.show_expenses()
    tracker.remove_expense()
    tracker.show_expenses()