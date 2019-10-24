# Read .csv file, analyze election day poll data

# Modules
import os
import csv

# Open file for read
datapath = os.path.join("Resources", "election_data.csv")

with open(datapath, "r", newline = "") as datafile:

    datareader = csv.reader(datafile, delimiter=",")
    data_header = next(datareader)
    data_list = list(datareader)

    #initalize variables
candidates = []
total_votes = len(data_list)    
    
for dlist in data_list:
    if dlist[2] not in candidates:
        candidates.append(dlist[2])

# #testing - remove before turning in
print(f"vote count:  {total_votes}")
print(candidates)

for name in candidates:
    votes = sum(1 for i in data_list if i[2] == name) 
    percent = round((votes / total_votes) * 100, 2)

    print(f"candiate name:  {name} percent:  {percent} candidate count:  {votes}")    
        # candidate_count = (candidate_count+1 for slist in data_list if slist[2] == name)
#     # percent = round((candidate_count / vote_count) * 100, 2)
#     # candidate_info.append(name, percent, candidate_count)

# print()
# print("Financial Analysis")
# print("-------------------------------")
# print(f"Total Months:  {row_count}")
# print(f"Total:  ${total}")
# print(f"Average Change:  ${average_change}")
# print(f"Greatest Increase in Profits:  {greatest_increase_date}  (${greatest_increase})")
# print(f"Greatest Decrease in Profits:  {greatest_decrease_date}  (${greatest_decrease})")

