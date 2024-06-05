import sqlite3
from datetime import datetime

class ExpenseTracker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Expenses
                               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT,
                                category TEXT,
                                amount REAL,
                                description TEXT)''')
        self.conn.commit()

    def add_expense(self, date, category, amount, description):
        self.cursor.execute('''INSERT INTO Expenses (date, category, amount, description)
                               VALUES (?, ?, ?, ?)''', (date, category, amount, description))
        self.conn.commit()

    def view_expenses(self):
        self.cursor.execute('''SELECT * FROM Expenses''')
        expenses = self.cursor.fetchall()
        return expenses

    def update_expense(self, expense_id, date, category, amount, description):
        self.cursor.execute('''UPDATE Expenses SET date=?, category=?, amount=?, description=?
                               WHERE id=?''', (date, category, amount, description, expense_id))
        self.conn.commit()

    def delete_expense(self, expense_id):
        self.cursor.execute('''DELETE FROM Expenses WHERE id=?''', (expense_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

def main():
    db_name = 'expenses.db'
    tracker = ExpenseTracker(db_name)

    while True:
        print("radyab hazine shakhsi")
        print("1. add hazine ")
        print("2. see hazine ")
        print("3.  update hazine")
        print("4. delete hazine")
        print("5. see you later alligator")

        choice = input("chikar konim? ")

        if choice == '1':
            date = input("date of hazine (like this YYYY-MM-DD): ")
            category = input("category: ")
            amount = float(input("cheghadr?: "))
            description = input("har che del tangat mikhahad begoo: ")
            tracker.add_expense(date, category, amount, description)
            print("success add shod haj!")

        elif choice == '2':
            expenses = tracker.view_expenses()
            for expense in expenses:
                print(expense)

        elif choice == '3':
            expense_id = int(input("id hazine ro begoo: "))
            date = input("new date  (like this  YYYY-MM-DD): ")
            category = input("new category: ")
            amount = float(input("cheqadr hazine jadid: "))
            description = input(" har che del tangat jadid mikhahad begoo: ")
            tracker.update_expense(expense_id, date, category, amount, description)
            print("success update shod haj!")

        elif choice == '4':
            expense_id = int(input("id hazine ro bede biad "))
            tracker.delete_expense(expense_id)
            print(" success hazf shod haj! !")

        elif choice == '5':
            break

        else:
            print("migam bein 1 ta 5 -_-")

if __name__ == "__main__":
    main()