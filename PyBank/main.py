#imports
import os
import csv

#set path to collect data
my_file = os.path.join("Resources", "budget_data.csv")

# open and read csv file
with open(my_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # read the header row first
    header = next(csv_reader)
    print(csv_reader)
    
    # read through each row of data after the header
   # for row in csv_reader:
        
    
    

