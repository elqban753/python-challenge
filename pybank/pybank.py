#set up mdodules and CSV file reader
import os
import csv

cwd = os.getcwd()    
csvpath = os.path.join(".","budget_data.csv")



with open(csvpath, newline= "") as budget_data_file:
    csvreader = csv.reader(budget_data_file, delimiter=",")
    csv_header = next(csvreader)

    output_file = open("financial_data.txt", "w")

    print("--------------------------------------")
    print("Financial Analysis")   
    print("--------------------------------------")
 
    output_file.write("--")
    output_file.write("Financial Analysis")   
    output_file.write("---")

    month = 0
    total = 0
    greatest_profit = 0
    greatest_loss = 0
    
    for row in csvreader:
        month = month + 1
        total = total + int(row[1])
        if int(row[1]) > int(greatest_profit):
            greatest_profit = int(row[1])
            highest_month = str(row[0])
        elif int(row[1]) < int(greatest_loss):
            greatest_loss = int(row[1])
            lowest_month = str(row[0])
              
            
    
print(f"Total Months: {month}")
print(f"Total: ${total}")

output_file.write(f"Total Months: {month}")
output_file.write(f"Total: ${total}")


average = round(total / month, 2)

print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {highest_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_loss})")

output_file.write(f"Average Change: ${average}")
output_file.write(f"Greatest Increase in Profits: {highest_month} (${greatest_profit})")
output_file.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_loss})")
