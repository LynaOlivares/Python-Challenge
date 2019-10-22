# Read .csv file, analyze profit/loss financial records

# Modules
import os
import csv

# Open file for read
budgetpath = os.path.join("Resources", "budget_data.csv")

with open(budgetpath, "r", newline = "") as budgetfile:
    # print(budgetfile)
    # lines = budgetfile.read()
    # print(lines)
    budgetreader = csv.reader(budgetfile, delimiter=",")
    budget_header = next(budgetreader)
    #print(f"Header:  {budget_header}")
    
    #initalize variables
    row_count = 0
    total = 0
    change_count = 0
    change_total = 0
    greatest_increase = 0
    greatest_decrease = 0
    
    for rows in budgetreader:
        row_count = row_count + 1
        total = total + int(rows[1])
        
        if row_count == 1:
            previous_row_total = int(rows[1])
        else:
            change_count = change_count + 1
            change_amount = int(rows[1]) - previous_row_total
            change_total = change_total + change_amount

            if change_amount > greatest_increase:
                greatest_increase = change_amount
                greatest_increase_date = rows[0]

            if change_amount < greatest_decrease:
                greatest_decrease = change_amount
                greatest_decrease_date = rows[0]
            
            previous_row_total = int(rows[1])

average_change = round((change_total / change_count), 2)

# output lines

outline1 = ["Financial Analysis"]
outline2 = ["-------------------------------"]
outline3 = [f"Total Months:  {row_count}"]
outline4 = [f"Total:  ${total}"]
outline5 = [f"Average Change:  ${average_change}"]
outline6 = [f"Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})"]
outline7 = [f"Greatest Decrease in Profits:  {greatest_decrease_date}  (${greatest_decrease})"]

# write output to a file
outpath = os.path.join("Resources", "budget_results.csv")

with open(outpath, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(outline1)
    writer.writerow(outline2)
    writer.writerow(outline3)
    writer.writerow(outline4)
    writer.writerow(outline5)
    writer.writerow(outline6)
    writer.writerow(outline7)

# print output to a screen
print()
print(outline1)
print(outline2)
print(outline3)
print(outline4)
print(outline5)
print(outline6)
print(outline7)