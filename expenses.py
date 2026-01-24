# File to aid in the tracking of Expenses
# Functions needed: Read/Write File, Add Expense, Delete Expense, Total Spending
# Total Spending should also return how much spare money per month the user has

# Expenses file Location
location = "text_files/expenses.txt"
dictionary = {}

def format_file():
    with open(location,'r') as file:
        f = file.readlines()
        for line in f:
            if line.strip():
                curr = line.replace('Â£', '').strip().replace('\n', ' ').replace(":", "").split(" ")
                dictionary[curr[0]] = curr[1]
    return dictionary

def add_expense(name, cost):
    with open(location,'a') as file:
        file.write("\n")
        file.write(name+": Â£"+cost)

def delete_expense(name):
    expenses = format_file()
    try:
        del expenses[name]
    except KeyError:
        print("No Value with that name in Expenses")

    with open(location,'w') as file:
        for key, value in expenses.items():
            file.write(key+": Â£"+value+"\n")

def total_remaining():
    expenses = format_file()
    remaining = float(expenses['Monthly_income'])
    print("Beginning Total Remaining", remaining)
    for x in expenses.values():
        curr = float(x)
        if curr == remaining:
            pass
        else:
            remaining -= curr
    print("Total remaining", remaining)
#if __name__ == '__main__':
