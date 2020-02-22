import os
import csv
import operator
from statistics import mean

#define file name
filename = 'budget_data.csv'

#set total months and earnings to 0
total_months = 0
total_earnings = 0

#create lists and dictionaries
earnings = []
earnings_delta = []
dates = []
summary_dict = {}

#define csv path
csvpath = os.path.join('Input', filename)

#open csv file with encoding
with open(csvpath, encoding = 'utf-8') as csvfile:

    #read csv file
    csvreader = csv.reader(csvfile, delimiter = ',')

    #set csv header
    csvheader = next(csvreader)

    #loop through csv reader, incrementing total months, append to earnings and dates lists
    for row in csvreader:
        total_months += 1
        earnings.append(row[0])
        dates.append(row[1])

    #loop through earnings list
    for i in range(len(earnings)):
        
        #increment total earnings
        total_earnings += int(earnings[i])
        
        #if not first record, calculate earnings delta and append to list
        if i != 0:
            earnings_delta.append(int(earnings[i]) - int(earnings[i-1]))

#calculate max, min, and avg changes
max_change = round(max(earnings_delta),0)
min_change = round(min(earnings_delta),0)
avg_change = round(mean(earnings_delta),2)

#Insert null value into earnings list to match date indexes
earnings_delta.insert(0,0)

#create summary dictionary based on earnings delta and dates
summary_dict = dict(zip(earnings_delta, dates))

#print summary
print("Financial Analysis")
print("------------------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(round(total_earnings,0)))
print("Average Change: " + "$" + str(avg_change))
print("Greatest Increase in Profits: " + summary_dict[max_change] + " ($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + summary_dict[min_change] + " ($" + str(min_change) +")")

# Specify the file to write to
output_path = os.path.join( "Output", "finance_summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = "") as datafile:

    # Initialize csv.writer
    csvwriter = csv.writer(datafile)

    # Write the remaining rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------------------"])
    csvwriter.writerow(["Total Months: " + str(total_months)])
    csvwriter.writerow(["Average Change: " + "$" + str(avg_change)])
    csvwriter.writerow(["Greatest Increase in Profits: " + summary_dict[max_change] + " ($" + str(max_change) + ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + summary_dict[min_change] + " ($" + str(min_change) +")"])
