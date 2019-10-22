# Read .csv file and analyze financial records

# Modules
import os
import csv

# Open file
budgetpath = os.path.join("Resources", "budget_data.csv")

with open(budgetpath, "r", newline = "") as budgetfile:
    # print(budgetfile)
    # lines = budgetfile.read()
    # print(lines)
    budgetreader = csv.reader(budgetfile, delimiter=",")
    budget_header = next(budgetreader)
    #print(f"Header:  {budget_header}")

    row_count = 0
    total = 0
    previous_increase = 0
    previous_decrease = 0

    for rows in budgetreader:
        row_count = row_count + 1
        total = total + int(rows[1])
        
        if int(rows[1]) > previous_increase:
            previous_increase = int(rows[1])
            increase_date = rows[0]

        if int(rows[1]) < previous_decrease:
            previous_decrease = int(rows[1])
            decrease_date = rows[0]

print(f"Total Months:  {row_count}")
print(f"Total:  {total}")
print(f"Average Change: $ {total/row_count}")
print(f"Greatest Increase in Profits:  {increase_date}  ( {previous_increase} )")
print(f"Greatest Decrease in Profits:  {decrease_date}  ( {previous_decrease} )")
