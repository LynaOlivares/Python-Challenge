# Read .csv file, analyze election day poll data

# Modules
import os
import csv

# Open file for read
datapath = os.path.join("Resources", "election_data.csv")

with open(datapath, "r", newline = "") as datafile:
    # print(datatfile)
    # lines = datafile.read()
    # print(lines)
    datareader = csv.reader(datafile, delimiter=",")
    data_header = next(datareader)
    #print(f"Header:  {data_header}")
    
    #initalize variables
    row_count = 0
    # total = 0
    # change_count = 0
    # change_total = 0
    # greatest_increase = 0
    # greatest_decrease = 0
    
    for rows in datareader:
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

print()
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:  {row_count}")
print(f"Total:  ${total}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})")
print(f"Greatest Decrease in Profits:  {greatest_decrease_date}  (${greatest_decrease})")

