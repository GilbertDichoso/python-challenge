import csv
import os

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


# Get the current directory of the script
current_directory = os.path.dirname(__file__)

# Specify the relative path to the CSV file
csv_file_path = os.path.join(current_directory, 'budget_data.csv')

# Read the CSV file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    # Skip the header row
    next(csvreader)
    
    # Iterate through the data
    for row in csvreader:
        # Calculate total number of months
        total_months += 1
        
        # Calculate net total amount of profits/losses
        net_total += int(row[1])
        
        # Calculate change in profits/losses
        if total_months > 1:
            profit_change = int(row[1]) - previous_profit_loss
            profit_changes.append(profit_change)
            
            # Find greatest increase in profits
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_change
            
            # Find greatest decrease in profits
            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change
        
        previous_profit_loss = int(row[1])

# Calculate average change in profits/losses
average_change = sum(profit_changes) / len(profit_changes)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Prepare the output text
output_text = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Write the results to a text file
with open('financial_analysis.txt', 'w') as txtfile:
    txtfile.write(output_text)


