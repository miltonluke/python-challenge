# -*- coding: UTF-8 -*-
#"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csvPath = os.path.join('Resources','budget_data.csv')  # Input file path
file_to_output = os.path.join('analysis','budget_analysis.txt')  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_net = 0
month_of_change = []
net_change_list = []
greatest_net_increase = ["",0]
greatest_net_decrease = ["", 0]

# Open and read the csv
with open(csvPath, encoding="UTF-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')


    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    startingProfitLoss = 1088983    

    # Track the total and net change
   
    # Process each row of data
    for row in reader:       
   
        # Track the total
        total_months += 1
        total_net = total_net + int(row[1])    

        # Track the net change
        netchange = int(row[1]) - previous_net

        previous_net = int(row[1])

        net_change_list = net_change_list + [netchange]

        month_of_change = month_of_change +[row[0]]       

        # Calculate the greatest increase in profits (month and amount)
        if (netchange > greatest_net_increase[1]):
            greatest_net_increase[0] = row[0]
            greatest_net_increase[1] = netchange

        # Calculate the greatest decrease in losses (month and amount)
        if (netchange < greatest_net_decrease[1]):
            greatest_net_decrease[0] = row[0]
            greatest_net_decrease[1] = netchange


# Calculate the average net change across the months
net_avg = (sum(net_change_list) - startingProfitLoss) / (len(month_of_change)-1)

# Generate the output summary
output_summary = (
    f"Financial Analysis\n" 
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_net_increase[0]} (${greatest_net_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_net_decrease[0]} (${greatest_net_decrease[1]})"
)


# Print the output
print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)
