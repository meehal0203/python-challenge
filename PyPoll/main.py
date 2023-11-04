# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


#imports

# allow us to create file paths across operating systems
# allows us to read CSV files
import os
import csv

#set path to collect data
CSVPATH = os.path.join("Resources","election_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# # # declare variables
total_votes = 0 #total votes
can_votes = {} #total votes per candidate
can_options = [] 
winner_vote = 0 # max amount of votes
winner = " "
can_name = []
votes = 0

with open(CSVPATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")


    # read header row
    header = next(csvreader)
    #print(header)
    

    
    #read in data by row
    # total number of votes cast   
    for row in csvreader:
        total_votes += 1
        can_name = row[2]
        #print(total_votes)
    


        # complete list of candidates who received votes
        # find candidates name and add name to list
        if  can_name in can_votes:
            can_votes[can_name] += 1
        else:
            can_votes[can_name] = 1

    
     
     
        # if can_name not in can_options:
        #     can_votes[can_name] = 0
        #     can_options += [can_name]
        #     # print(can_options)

        #     # tally up votes to each candidate
        #     total_can_votes = can_votes[can_name] += 1
        
            # print(can_votes)
        
        # calculate percentage each candidate received
            # percent_votes_each = can_votes[can_name]/total_votes * 100
            # print(percent_votes_each)
    for can_name, votes in can_votes.items():
    #     percent_votes_each = (votes / total_votes) * 100
    #     print(f"{can_name}: {percent_votes_each:.2f}% ({votes})")      
        
        # use 'brute force' to  determin winner

        if votes > winner_vote:
            winner_vote = votes
            winner = can_name       
            
        # print(f"{can_name}: {percent_votes_each:.2f}% ({votes})")   
         # election winner based on popular vote
        # list out keys and values separately
        # key_list = list(can_votes.keys())
        # val_list = list(can_votes.values())
        # max_votes = max(val_list)

        #  # print key with val max_votes
        # winner_name = val_list.index(max_votes)
        # max_votes = winner_name
        # print(key_list[position])

        # your final script should both print the analysis to
        #  the terminal and export a text file with the results.

        # print results
    print("Election Results")
    print("...........................")
    print(f"Total Votes: {total_votes}")
    print("...........................")
    for can_name, votes in can_votes.items():
        percent_votes_each = (votes / total_votes) * 100
        print(f"{can_name}: {percent_votes_each:.2f}% ({votes})") 
    #print(f"{can_name}: {percent_votes_each:.2f}% {can_votes}")
    # print(f"{can_name}: {percent_votes_each:.2f}% 
        #  ({votes})")
    #for can_name, votes in can_votes.items():
       # print(f"{can_name:} {percent_votes_each:.2f} {can_votes:}")
    print("...........................")
    print(f"Winner:{winner}")
    print("............................")