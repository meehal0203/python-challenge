#imports
import os
import csv

#set path to collect data
my_file = os.path.join("python-challenge","PyBank", "Resources", "budget_data.csv")

with open(my_file) As csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    
    

