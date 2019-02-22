# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:16:47 2019

@author: Dan
"""
import csv
import os
#Initialize all variables
rec_count = 0
voter_data = 0
voter_ID = ''
voter_county = ''
voter_candidate = ''
max_candidate = 0
winner = ''
list_of_votes = []
candidate_list = []
num_of_candidates = 0
candidate_votes = []
candidate_count = 0
#open the file
csvpath = 'PyPoll_Data.csv'

#while there continue to be records in the file
with open(csvpath, newline='') as csvfile:
    
#read and count a record and 
    record = csv.reader(csvfile, delimiter=',')
    csv_header = next(record)
#    line_data = record.split(',')
    for rec in record:
        rec_count += 1
        voter_ID = rec[0]
        voter_county = rec[1]
        voter_candidate = rec[2]
        candidate_votes.append(voter_candidate)
        if voter_candidate not in candidate_list:
            candidate_list.append(voter_candidate)
            num_of_candidates += 1
        list_of_votes.append(voter_candidate)

file_out = open('PY_Poll_Data.txt', 'wt')
print("-------------------------------")
print("Election results:")
print("-------------------------------")
print("Total Votes: ", rec_count)
print("-------------------------------")

print("-------------------------------", file = file_out)
print("Election results:", file = file_out)
print("-------------------------------", file = file_out)
print("Total Votes: ", rec_count, file = file_out)
print("-------------------------------", file = file_out)

sorted_candidates = sorted(candidate_list)
#print("Sorted candidates: ", sorted_candidates)
#print("list_of_votes: ", list_of_votes)
for x in sorted_candidates:    
    for y in list_of_votes:    
        if x == y: 
            candidate_count += 1  
            if candidate_count > max_candidate:
                winner = x
                max_candidate += 1            
    print(x, "%0.2f" %(candidate_count * 100/rec_count), "(", candidate_count, "votes )")
    print(x, "%0.2f" %(candidate_count * 100/rec_count), "(", candidate_count, "votes )", file = file_out)
    candidate_count = 0
print("-------------------------------")
print("Winner: ", winner, "!!!")
print("-------------------------------")

print("-------------------------------", file = file_out)
print("Winner: ", winner, "!!!", file = file_out)
print("-------------------------------", file = file_out)

file_out.close()

#Loop to get sum of chnages, and find max & min changes
