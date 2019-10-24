# Read .csv file, analyze election day poll data

# Modules
import os
import csv

# Open file for read, create file list for re-reading
datapath = os.path.join("Resources", "election_data.csv")

with open(datapath, "r", newline = "") as datafile:

    datareader = csv.reader(datafile, delimiter=",")
    data_header = next(datareader)
    data_list = list(datareader)

#initial processing
candidates = []
election_report = []

total_votes = len(data_list)    

election_report.append("-------------------------------")
election_report.append("Election Results")
election_report.append("-------------------------------")
election_report.append(f"Total Votes:  {total_votes}")
election_report.append("-------------------------------")

# read list to gather candidate vote information
previous_votes = 0

for dlist in data_list:
    if dlist[2] not in candidates:
        candidates.append(dlist[2])

for name in candidates:
    votes = sum(1 for i in data_list if i[2] == name) 
    percent = round((votes / total_votes) * 100, 3)

    if votes > previous_votes:
        winner = name
        previous_votes = votes

    election_report.append(f"{name}:   {percent}%   ({votes})")
  
# list ending results
election_report.append("-------------------------------")
election_report.append(f"Winner:  {winner}")
election_report.append("-------------------------------")

# open output file and write results

outpath = os.path.join("Resources", "poll_results.csv")

with open(outpath, "w", newline="") as outfile:
    writer = csv.writer(outfile)

    print()
    for row in election_report:
        writer.writerow([row])
        print(row)

#end of process