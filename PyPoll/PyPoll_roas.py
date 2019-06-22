'''
PyPoll instruction:
    - The total number of votes cast
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The winner of the election based on popular vote.
'''
 # Import libraries
import os
import csv # Module for reading CSV files

input_path = "/Users/roas/Projects_Git/Python_Challenge/Resources"
output_path = "/Users/roas/Projects_Git/Python_Challenge/Resources/PyPollWinner.txt"

#Open the path with csv library
csvpath = os.path.join(input_path, 'election_data.csv')

inicial = 1
candidates = {}
count = 0
value=0

#Read the file, row by row
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

# Read the file
    voting_info = [votes for votes in csvreader] #Gives a list with the whole vote info
    count_votes = len(voting_info) #Total of votes

#Counts the votes per candidate
    for vote in voting_info:
        if vote[2] in candidates: #checks if tha candidate already in the list
            counter = candidates[vote[2]]
            counter += 1
            candidates[vote[2]] = counter # adds the count
        else:
            candidates[vote[2]] = 1 #begins the key in the dictionary


#Percentage of votes candidates 

    percent = []
    winner = 0
    for elements in candidates:
        candidate_vote = candidates[elements]
        percent.append((candidate_vote/count_votes) * 100)
        if candidate_vote > winner:
            winner = candidate_vote
            candidatewinner = elements

#Prints with format in Terminal
    print('{0:^25}  {1:^25}  {2:^25}'.format('','PyPoll: Election Result',''))
    print("-"*80)
    print('{0:^25}  {1:^25}  {2:^25}'.format('Total: %s'%count_votes,'Winner is: %s'%candidatewinner,''))
    print("-"*80)
    print('{0:<25} | {1:<25} | {2:<25}'.format('Candidates','Total Votes','Percentage'))
    x = 0
    for elements in candidates:
        print('{0:^25} | {1:>25} | {2:>25.4}%'.format(elements,candidates[elements],percent[x]))
        x+=1

#Prints in file
    file = open(output_path,"w+")
    file.write('{0:^25}  {1:^25}  {2:^25}'.format('','PyPoll: Election Result','\n'))
    file.write("-"*80)
    file.write('{0:^25}  {1:^25}  {2:^25}'.format('\nTotal: %s'%count_votes,'Winner is: %s'%candidatewinner,''))
    file.write("-"*80)
    file.write('{0:<25} | {1:<25} | {2:<25}'.format('\nCandidates','Total Votes','Percentage'))
    x = 0
    for elements in candidates:
        file.write('{0:^35} | {1:>25} | {2:>30.4}%'.format("\n%s"%elements,candidates[elements],percent[x]))
        x+=1
    file.close()