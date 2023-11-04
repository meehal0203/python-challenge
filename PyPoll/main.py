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
        
    


        # complete list of candidates who received votes &
        # tally up votes to each candidate
        if  can_name in can_votes:
            can_votes[can_name] += 1
        else:
            # find candidates name and add name to list
            can_votes[can_name] = 1

        
        
    
    for can_name, votes in can_votes.items():
        
        # use 'brute force' to  determine winner

        if votes > winner_vote:
            winner_vote = votes
            winner = can_name       
            
        # print(f"{can_name}: {percent_votes_each:.2f}% ({votes})")   
        

        # your final script should both print the analysis to
        #  the terminal and export a text file with the results.

        # print results to terminal
    print("Election Results")
    print("...........................")
    print(f"Total Votes: {total_votes}")
    print("...........................")
    for can_name, votes in can_votes.items():
        percent_votes_each = (votes / total_votes) * 100
        print(f"{can_name}: {percent_votes_each:.2f}% ({votes})") 
    
    print("...........................")
    print(f"Winner:{winner}")
    print("............................")

    # print results to analysis text file
    output_file = open("PyPoll Analysis.txt", "w")
    output_file.write("Election Results\n")
    output_file.write("...........................\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("...........................\n")
    # calc and write %
    for can_name, votes in can_votes.items():
        percent_votes_each = (votes / total_votes) * 100
        output_file.write(f"{can_name}: {percent_votes_each:.2f}% ({votes})\n") 
    
    output_file.write("...........................\n")
    output_file.write(f"Winner:{winner}\n")
    output_file.write("............................\n")

    # close output file
    output_file.close()
