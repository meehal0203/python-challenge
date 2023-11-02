# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


#imports
import os
import csv

#set path to collect data
my_poll = os.path.join("Resources", "election_data.csv")

with open(my_poll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # read header row
    header = next(csvreader)
    print(header)

    # # # declare variables
    total_votes = 0 #total votes
    can_votes = {} #total votes per candidate
    can_options = [] #candidate name
    winner_vote = 0 # max amount of votes
    winner_name = " "
    
    
    #read in data by row
     # total number of votes cast   
    for row in csvreader:
        total_votes += 1
        can_name = row[2]
    
    # complete list of candidates who received votes
    # find candidates name and add name to list
        if can_name not in can_options:
            can_votes[can_name] = 0
            can_options += [can_name]
        
        # tally up votes to each candidate
        can_votes[can_name] += 1
        print(can_votes)
         #find winner


        # candidates = list(can_votes.keys())

        # winner_name = candidates[winner_vote]

        

    # calculate percentage each candidate received
    percent_votes_each = can_votes / total_votes * 100
    print(percent_votes_each)
