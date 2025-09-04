import json 

class Expense:
    _uniq_id = 1 # unique id for each expense

    def __init__(self, name, amount):
        self.id = Expense._uniq_id
        Expense._uniq_id += 1 # increment id each time new expense added
        self.name = name
        self.amount = amount


    def __str__(self):
        return f"[{self.id}] {self.name}-> Rs.{self.amount}"
              

class ExpenseTracker:
    def __init__(self):
        self.expense = []
        self.filename = 'Personal Expense Tracker/expense_db.json'
        self.__menu()

    def __menu(self):
        print("PERSONAL EXPENSE TRACKER")
        print("""
            1. Add Expense
            2. View Expense
            3. Update Expense
            4. Remove Expense
            5. Any other number to quit
""")
        
        try: 
            user_choice = int(input("Enter your choice (1-4): "))
            match user_choice:
                case 1:
                    print("\t--ADD EXPENSE SECTION--\t")
                    self.add_expense()
                case 2:
                    print("\t--VIEW EXPENSE SECTION--\t")
                    self.show_expense()
                case 3:
                    print("\t--UPDATE EXPENSE SECTION--\t")
                    self.update_expense()
                case 4:
                    print("\t--REMOVE EXPENSE SECTION--\t")
                    self.remove_expense()
                case _ :
                    exit()
        except Exception:
            print(f"Error: Only choose between 1 to 4")
            self.__menu()


    def add_expense(self):
        __name = input("Enter expense name: ")
        __amount = input("Enter expense amount: ")

        data = Expense(__name, __amount) # pass value to Expense class
        self.expense.append(data) # store in self.expense list
        self.save_expense_data() # json file save
        self.__menu()

    def save_expense_data(self):
        data = [{'id': i.id, 'name': i.name, 'amount': i.amount} for i in self.expense]
        with open(self.filename, 'w') as wf:
            json.dump(data,wf, indent=4)

    def remove_expense(self):
        __remove_index = int(input("Enter index you want to remove: "))
        isFound = False
        for exp in self.expense:
            if exp.id == __remove_index:
                self.expense.remove(exp)
                isFound = True
                self.save_expense_data()
                self.__menu()
                break

        if not isFound:
            print(f'No expense found in given {__remove_index}')
        else:
            print(f'ID: {__remove_index} removed successfully')
        
    def update_expense(self):
        __update_index = int(input("Enter index you want to update: "))
        isFound = False
        for exp in self.expense:
            if exp.id == __update_index:
                __new_name = input("Enter updated expense name: ")
                __new_amount = input("Enter updated expense amount: ")
                exp.name = __new_name
                exp.amount = __new_amount
                isFound = True
                self.save_expense_data()
                self.__menu()
                break
        
        if not isFound:
            print(f"No data found in given {__update_index}")
        else:
            print(f"ID:{__update_index} updated successfully")
        
    def show_expense(self):
        with open(self.filename, 'r') as rf:
            data = json.load(rf)
            for d in data:
                print(f"{[d['id']]} {d['name']} -> {d['amount']}")
        
            print()
        self.__menu()

e1 = ExpenseTracker()




