#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, 
# and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#imports
# allow us to create file paths across operating systems
# allows us to read CSV files
import os
import csv

#set path to collect data
CSV_PATH = os.path.join("Resources","budget_data.csv")


# print("I'm here:", os.getcwd())
# print(__file__)
# print(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# print("Now I'm here:", os.getcwd())
# open and read csv file
 #set variables
monthly_count = 0
month_of_change = []
profit_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_change = 0


with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # read the header row first
    header = next(csv_reader)
    # print(header)
    
    first_row = next(csv_reader)
    monthly_count += 1
    total_change += int(first_row[1])
    previous_net = int(first_row[1])
    

    # read through each row of data after the header
    for row in csv_reader:
        # find number of months in dataset
        
        monthly_count += 1
        total_change += int(row[1])
        
        current_change = int(row[1]) - previous_net
        previous_net = int(row[1])

        profit_change += [current_change]
        month_of_change += [row[0]]

        
       
        # Calculate the greatest increase
        if current_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_change
        # Calculate the greatest decrease
        if current_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_change
   

  
# average changes
average_change = sum(profit_change) / len(profit_change)


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {monthly_count}\n"
    f"Total: ${total_change}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Print the output (to terminal)
print(output)  