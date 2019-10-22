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

# write output to screen
print()
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:  {row_count}")
print(f"Total:  ${total}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})")
print(f"Greatest Decrease in Profits:  {greatest_decrease_date}  (${greatest_decrease})")

# write output to a file
outpath = os.path.join("Resources", "budget_results.csv")

with open(outpath, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-------------------------------"])
    writer.writerow([f"Total Months:  {row_count}"])
    writer.writerow([f"Total:  ${total}"])
    writer.writerow([f"Average Change:  ${average_change}"])
    writer.writerow([f"Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})"])
    writer.writerow([f"Greatest Decrease in Profits:  {greatest_decrease_date}  (${greatest_decrease})"])

