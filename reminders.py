# File to aid in the tracking of Reminders
# Need functions to add reminders, delete reminders, ask for upcoming reminders and any reminders today

from datetime import date
from unittest import case

# Expenses file Location
location = "text_files/reminders.txt"
dictionary = {}

#Converts the month from Numerical Input into String Name
def convert_month(month_number):
    if month_number == "01":
        return "January"
    elif month_number == "02":
        return "February"
    elif month_number == "03":
        return "March"
    elif month_number == "04":
        return "April"
    elif month_number == "05":
        return "May"
    elif month_number == "06":
        return "June"
    elif month_number == "07":
        return "July"
    elif month_number == "08":
        return "August"
    elif month_number == "09":
        return "September"
    elif month_number == "10":
        return "October"
    elif month_number == "11":
        return "November"
    elif month_number == "12":
        return "December"
def format_file():
    #Formats the File into a dictionary of {DATE : REMINDER}
    with open(location,'r') as file:
        f = file.readlines()
        for line in f:
            if line.strip():
                curr = line.strip().replace('\n', ' ').split(":")
                dictionary[curr[0]] = curr[1]
    return dictionary

def add_reminder(date, reminder):
    with open(location,'a') as file:
        file.write("\n")
        file.write(date+": "+reminder)
def delete_reminder(r):
    reminders = format_file()
    try:
        del reminders[r]
    except KeyError:
        print("No Value with that name in Expenses")

    with open(location, 'w') as file:
        for date, rem in reminders.items():
            file.write(date + ":" + rem + "\n")
def reminders_today():
    today = date.today()
    t = str(today.day)
    reminders = format_file()
    output = []
    for d in reminders.keys():
        curr = d.split("-")
        x = curr[0]
        if t == x:
            output.append(reminders[d])
        else:
            pass
    if len(output) == 0:
        return "There are no reminders set for today"
    else:
        return output
def reminders_month(month):
    reminders = format_file()
    output = []
    for date in reminders.keys():
        curr = date.split("-")
        m = curr[1]
        strMonth = convert_month(m)
        if strMonth == month:
            output.append(reminders[date])
        else:
            pass
    return output


print(reminders_today())
