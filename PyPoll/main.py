#imports
import os
import csv

#set path to collect data
my_poll = os.path.join("python-challenge","PyPoll", "Resources", "election_data.csv")

with open(my_poll) As csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
