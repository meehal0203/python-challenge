#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#imports

import os
import csv

#set path to collect data
my_file = os.path.join("..","Resources", "budget_data.csv")

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

    # read through each row of data after the header
    for row in csv_reader:
        # find number of months in dataset
        monthly_count += 1
       
        print(monthly_count)
        # total net amount profit and loss
        total_vol += int(row[1])
        print(total_vol)
    
    

