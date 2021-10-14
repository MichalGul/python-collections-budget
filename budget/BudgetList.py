from . import Expense
import matplotlib.pyplot as plt


class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def __len__(self):
        return len(self.expenses) + len(self.overages)

    # create budget list iterator
    def __iter__(self):
        self.iter_e = iter(self.expenses)
        self.iter_o = iter(self.overages)
        return self
    # define next methods to itarate over BudgetList
    def __next__(self):
        try:
            return self.iter_e.__next__()
        except StopIteration as stop:
            print("Over budget")
            return self.iter_o.__next__()

    def append(self, item):
        if self.sum_expenses + item < self.budget:
            self.expenses.append(item)
            self.sum_expenses += item
        else:
            self.overages.append(item)
            self.sum_overages += item


def main():
    myBudgetList = BudgetList(30000)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/monefy-2021-10-11_06-11-44.csv')
    print(expenses.categories)
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
    print('The count of all expenses: ' + str(len(myBudgetList)))

    for entry in myBudgetList:
        print("budget entry", entry)

    #create plot foe expenses
    fig, ax = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages, myBudgetList.budget]
    ax.bar(labels, values, color=['green', 'red', 'blue'])
    ax.set_title("Your total expenses vs. total budget")
    plt.show()

if __name__ == "__main__":
    main()


