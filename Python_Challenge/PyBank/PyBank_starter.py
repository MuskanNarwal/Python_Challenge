# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_loss = 0
net_change_list = []
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""

# Open and read the CSV
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    previous_profit_loss = float(first_row[1])  # Store the first row's profit/loss
    total_net += previous_profit_loss  # Add the first row to total_net
    total_months += 1  # Track the first row as a month

    # Process each row of data
    for row in reader:
        # Track the total months
        total_months += 1

        # Track the total net profit/loss
        current_profit_loss = float(row[1])
        total_net += current_profit_loss

        # Calculate the net change
        net_change = current_profit_loss - previous_profit_loss
        net_change_list.append(net_change)

        # Track the greatest increase in profits
        if net_change > greatest_increase:
            greatest_increase = net_change
            increase_month = row[0]

        # Track the greatest decrease in profits
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            decrease_month = row[0]

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Print the output
print(f"Total Months: {total_months}")
print(f"Total Net Amount: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n"
    )
    txt_file.write(output)
