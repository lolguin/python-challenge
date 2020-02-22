import os
import csv
import operator

#define dictionaries and lists
voter_dict = {}
voter_percentage = []
candidates = []
summary = []
sorted_summary = []

#set total equal to 0
total_votes = 0

#set filename
filename = 'houston_election_data.csv'

#set csv path
csvpath = os.path.join('..', 'Input', filename)

#open csv file with encoding
with open(csvpath, encoding = 'utf-8') as csvfile:

    #read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    #set csv header
    csvheader = next(csvreader)

    #loop through csv file, incrementing total votes, and populate voter dictionary 
    for row in csvreader:
        total_votes += 1
        
        if row[0] not in voter_dict.keys():
            voter_dict[row[0]] = 1
        else:
            voter_dict[row[0]] += 1

#populate candidate list and voter percentage list 
for key, value in voter_dict.items():
    candidates.append(key)
    voter_percentage.append(format(value/total_votes, ".2%"))
    
#create summary list
summary = list(zip(candidates, voter_percentage,voter_dict.values()))

#sort summary list
sorted_summary = sorted(summary, key = lambda x: x[2], reverse = True)

#define first and second place
first_place = sorted_summary[0][0]
second_place = sorted_summary[1][0]


# Print Summary Section
print("Houston Mayoral Election Results")

print("--------------------------------")

print("Total Cast Votes: " + str(total_votes))

print("--------------------------------")

for i in range(len(sorted_summary)):
    print(sorted_summary[i][0] + ": " + str(sorted_summary[i][1]) + " (" + str(sorted_summary[i][2]) + ")")
    
print("--------------------------------")
print("1st Advancing Candidate: " + first_place)
print("2nd Advancing Candidate: " + second_place)
print("--------------------------------")

# Specify the file to write to
output_path = os.path.join("..", "Output", "candidate_summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = '') as datafile:

    # Initialize csv.writer
    csvwriter = csv.writer(datafile)

    # Write the first row (column headers)
    csvwriter.writerow(["Candidate", "Vote %", "Vote Count"])

    # Write the remaining rows
    csvwriter.writerows(sorted_summary)






