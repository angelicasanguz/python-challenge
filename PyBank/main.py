# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
from statistics import mean 

profit=0
months = []
list_avg=[]
list_profit=[]
list_loss=[]
monthly_changes =[]
losses = 0
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        list_profit.append(int(row[1]))

    print("\nFinancial Analysis")
    print("-----------------------------------")
#The total number of months included in the dataset
    print("Total Month: %d" % len(months))
#The net total amount of "Profit/Losses" over the entire period
    print("Total: $%d" % sum(list_profit))
 #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(len(list_profit)-1):
        monthly_changes.append(list_profit[i+1]-list_profit[i])
    print("Average Change: $%.2f" % mean(monthly_changes))

#The greatest increase in profits (date and amount) over the entire period
index = monthly_changes.index(max(monthly_changes))
print("Greatest Increase in Profits: %s $%s" % (months[index+1], max(monthly_changes)))

#The greatest decrease in profits (date and amount) over the entire period
index = monthly_changes.index(min(monthly_changes))
print("Greatest Increase in Profits: %s $%s" % (months[index+1], min(monthly_changes)))

