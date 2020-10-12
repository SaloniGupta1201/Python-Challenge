
"""This file analyzes election data in csv files with the following format:
voter_id    county    candidate"""

#import os and csv files
import os
import csv

# Initialize variables and create lists to store values
candidates_list = []
num_votes = 0
vote_counts_list = []

#Path to collect data from the Resources folder
pypolldata_csv = os.path.join("PyPoll",'Resources',
'Unit 3 - Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

# Read in the CSV file
with open(pypolldata_csv,newline="") as csvfile:

    #split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skip the header
    first_row = next(csvreader,None)

    #go line by line and process each vote
    for first_row in csvreader:

        #add to calculate total number of votes
        num_votes = num_votes + 1

        #candidate voted for
        candidate = first_row[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates_list:
            candidate_index = candidates_list.index(candidate)
            vote_counts_list[candidate_index] = vote_counts_list[candidate_index] + 1
        #else create new spot in candidate list for candidate and add 1 to vote counts list for that record
        else:
            candidates_list.append(candidate)
            vote_counts_list.append(1)
#create percentages list to store value of each candidate percentage of votes
percentages = []
#initialize max votes with values in vote counts list
max_votes = vote_counts_list[0]
#to store the position/index of max vote count holder
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates_list)):
    vote_percentage = format(vote_counts_list[count]/num_votes*100,'.3f')
    percentages.append(vote_percentage)
    if vote_counts_list[count] > max_votes:
        max_votes = vote_counts_list[count]
        print(max_votes)
        max_index = count
winner = candidates_list[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
print("--------------------------")
#print results for each candidate in the format: Candidate_name: Votes% (Total number of votes)
for count in range(len(candidates_list)):
    print(f"{candidates_list[count]}: {percentages[count]}% ({vote_counts_list[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Path to print the results to analysis folder
write_file = os.path.join("PyPoll",'analysis', 'pypoll_analysis.txt')

#open write file
output_file = open(write_file, mode = 'w')

#print analysis to file
output_file.write("Election Results\n")
output_file.write("--------------------------\n")
output_file.write(f"Total Votes: {num_votes}\n")
output_file.write("--------------------------\n")
#print results for each candidate in the format: Candidate_name: Votes% (Total number of votes)
for count in range(len(candidates_list)):
    output_file.write(f"{candidates_list[count]}: {percentages[count]}% ({vote_counts_list[count]})\n")
output_file.write("---------------------------\n")
output_file.write(f"Winner: {winner}\n")
output_file.write("---------------------------\n")

