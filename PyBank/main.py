#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#imports
# allow us to create file paths across operating systems
# allows us to read CSV files
import os
import csv

#set path to collect data
my_file = os.path.join("budget_data.csv")

# open and read csv file
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # read the header row first
    header = next(csv_reader)
    print(header)
    
    #set variables
    monthly_count = 0
    total_vol = 0
    profit_change = 0
    great_increase = 0
    great_decrease = 0
    great_inc_date = " "
    great_dec_date = " "
    profit_loss = 0
    previous_profit_loss = 0
    date = []
    

    # read through each row of data after the header
    for row in csv_reader:
        # find number of months in dataset
        monthly_count += 1
       
       # print(monthly_count)

        # total net amount profit and loss
        total_vol += int(row[1])
        # print(total_vol)

        # find changes in P&L, month to month
        # loop through each month, subtract new month from previous
        for i in range(len(profit_loss)-1):
           profit_change = profit_loss[i+1] - previous_profit_loss[i]
           profit_change.append()

        #find max profit increase month to month
        # date  and amount
        great_increase = max(profit_change)
        great_inc_date = 
    
        #find max profit decrease month to month
        # date  and amount
        great_decrease = min(profit_change)
        great_dec_date = 


        # your final script should both print the analysis to
        #  the terminal and export a text file with the results.
       
