from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('data/monefy-2021-10-11_06-11-44.csv')

print(expenses)

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top6 = spending_counter.most_common(6)
categories, count = zip(*top6)

print(categories)
print(count)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title("# Expenses in category")
plt.show()


