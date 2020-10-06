import os
import csv

# Path to collect data from the Resources folder
pybankdata_csv = os.path.join("PyBank",'Resources', 'Unit 3 - Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
# Path to print the results to analysis folder
pybankdata_txt = os.path.join("PyBank",'analysis', 'pybank_analysis.txt')

# Initialize your values to variables with 0
month = 0
total = 0
greatest_profit = 0
greatest_loss = 0
net_change_list = []

# Read in the CSV file

with open(pybankdata_csv, 'r') as csvfile:

    # Split the data on commas

    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    # Read the header row first (skip this step if there is no header)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    month += 1
    total += int(first_row[1])

    # Read each row of data after the header

    for row in csvreader:
        month += 1
        total += int(row[1])
        net_change = int(row[1]) - previous_row
        previous_row = int(row[1])
        net_change_list = net_change_list + [net_change]
        average = sum(net_change_list)/len(net_change_list)
        
        if net_change > int(greatest_profit):
            greatest_profit = net_change
            highest_month = str(row[0])
        if net_change < int(greatest_loss):
            greatest_loss = net_change
            lowest_month = str(row[0])

# Print out the analysis to the terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {highest_month} (${greatest_profit})")
print(f"Greatest Decrease in Lossess: {lowest_month} (${greatest_loss})")

# Write in the txt file

with open(pybankdata_txt, 'w') as output_file: 
    output_file.write("Financial Analysis\n") 
    output_file.write("---------------------------\n")
    output_file.write(f"Total Months: {month}\n")
    output_file.write(f"Total: ${total}\n")
    output_file.write(f"Average Change: ${average}\n")
    output_file.write(f"Greatest Increase in Profits: {highest_month} (${greatest_profit})\n")
    output_file.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_loss})\n")
