import os
import csv

budgetcsvpath = os.path.join('Resources', 'budget_data.csv')

months = 0
net_change_in_profit = 0
change_in_month = []
month_count = []
increase_in_profit = 0
greatest_increase = 0
decrease_in_profit = 0
greatest_decrease = 0

with open(budgetcsvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)
    
    previous_row = int(row[1])
    months += 1
    net_change_in_profit += int(row[1])
    increase_in_profit = int(row[1])
    greatest_increase = row[0]
    
    for row in csvreader:
        
        months += 1
        net_change_in_profit += int(row[1])
        revenue_change = int(row[1]) - previous_row
        change_in_month.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        if int(row[1]) > increase_in_profit:
            increase_in_profit = int(row[1])
            greatest_increase = row[0]
            
        if int(row[1]) < decrease_in_profit:
            decrease_in_profit = int(row[1])
            greatest_decrease = row[0]  
        
    average_change = sum(change_in_month)/ len(change_in_month)
    
    highest = max(change_in_month)
    lowest = min(change_in_month)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_change_in_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease}, (${lowest})")

output_file = os.path.join('analysis', 'budget_data.text')

with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${net_change_in_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease}, (${lowest})\n")