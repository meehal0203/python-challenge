# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


#imports
import os
import csv

#set path to collect data
my_poll = os.path.join("python-challenge","PyPoll", "Resources", "election_data.csv")

with open(my_poll) as csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # read header row
    header = next(csvreader)
    
    # declare variables
    total_votes = [] #total votes
    can_total = [] #total votes per candidate
    can_name = [] #candidate name
    percent_votes_each = [] #each candidate vote percentage
    winner_vote = [] # max amount of votes
    ballot_id = [] #id number
    county = [] #place of vote

    # set conditions
    total_votes = 0
    winner_vote = 0
    can_total = 0
    
    
    #read in data by row, column
        
    for row in csv_reader:
        total_votes += 1
        can_name = row[2]
