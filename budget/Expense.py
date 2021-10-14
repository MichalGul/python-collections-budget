import csv
from datetime import datetime


class Expense():
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%d.%m.%Y')
        self.vendor = vendor
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"{str(self.category)} - {str(self.amount)}"

class Expenses():
    def __init__(self):
        self.list = []
        self.sum = 0
        self.categories = set()

    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self, filename):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', )
            for row in csvreader:
                if '-' not in row[3]:
                    continue
                # print(row[3])
                # print(float((row[3][2:])))
                amount = float((row[3][1:]).replace(',', '.'))
                # print(amount)
                self.list.append(Expense(row[0], row[1], row[2], amount))
                self.categories.add(row[2])
                self.sum += amount

    def categorize_for_loop(self):
        necessary_expenses = set()
        food_expenses = set()
        unnecessary_expenses = set()
        for i in self.list:
            if i.category in ("Rachunki", "Dom", "Samochód", "Drogerie", "Zdrowie", 'Sport'):
                necessary_expenses.add(i)
            elif i.category in ("Zakupy Żabka", "Zakupy Duże", "Pieczywo", "Warzywa", 'Jedzenie na mieście') :
                food_expenses.add(i)
            else:
                unnecessary_expenses.add(i)

        return [necessary_expenses, food_expenses, unnecessary_expenses]

    def categorize_set_comprehension(self):
        necessary_expenses = {x for x in self.list if x.category in ("Rachunki",
                                                                     "Dom",
                                                                     "Samochód", "Drogerie", "Zdrowie", 'Sport', "Corsinka"
                                                                     )}
        food_expenses = {x for x in self.list if
                         x.category in ("Zakupy Żabka", "Zakupy Duże", "Pieczywo", "Warzywa", 'Jedzenie na mieście')}
        unnecessary_expenses = set(self.list) - necessary_expenses - food_expenses

        return [necessary_expenses, food_expenses, unnecessary_expenses]
