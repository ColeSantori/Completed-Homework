import csv
from pathlib import Path

load_csv = Path("Resources/budget_data.csv")
output_csv = Path("analysis/budget_analysis.txt")

# initialize parameters
total_months = 0
month_of_change = []
net_change_list = []
highest_increase = ["", 0]
lowest_decrease = ["", 9999999999999999999]
total_net = 0

# Read and convert the csv 
with open(load_csv) as financial_data:
    reader = csv.reader(financial_data)

    
    header = next(reader)

    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the highest increase
        if net_change > highest_increase[1]:
            highest_increase[0] = row[0]
            highest_increase[1] = net_change

        # Calculate the lowest_decrease
        if net_change < lowest_decrease[1]:
            lowest_decrease[0] = row[0]
            lowest_decrease[1] = net_change

# Calculate the Average Change
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)

# Print the results
with open(output_csv, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average  Change: ${net_monthly_avg}\n")
    txt_file.write(f"Greatest Increase in Profits: {highest_increase[0]} (${highest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {lowest_decrease[0]} (${lowest_decrease[1]})\n")