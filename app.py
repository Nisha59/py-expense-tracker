from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

    
# Expense class to store expense data
class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

     

# ExpenseTracker class to manage the expenses
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            
    def view_expenses(self):
        return self.expenses

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

# Create an instance of ExpenseTracker
tracker = ExpenseTracker()

# Route to display the home page with the list of expenses and total
@app.route('/')
def index():
    total = tracker.total_expenses()
    expenses = tracker.view_expenses()
    return render_template('index.html', expenses=expenses, total=total)

# Route to add a new expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    date = request.form['date']
    description = request.form['description']
    amount = float(request.form['amount'])
    expense = Expense(date, description, amount)
    tracker.add_expense(expense)
    return redirect(url_for('index'))

@app.route('/remove_expense/<int:index>', methods=['POST'])
def remove_expense(index):
    tracker.remove_expense(index)
    return redirect(url_for('index'))


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
