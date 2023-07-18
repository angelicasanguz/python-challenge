# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

candidates = []
candidateVote=[]
total_votes=[]
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
       total_votes.append(int(row[0]))
       candidates.append(row[2])       
    uniqueCandidates =[]

    #extract unique candidates    
    for i in range(0, len(candidates)-1) :
        if candidates[i] not in uniqueCandidates :
            uniqueCandidates.append(candidates[i])  
    print("\nElection Results")
    print("-----------------------------------")
    #The total number of votes cast
    print("Total Votos: %d" % len(total_votes))
    print("-----------------------------------")

    #From my unique candidate list count how many times apear to get Votes
    for i in range(0, len(uniqueCandidates)) :
        tmpVotes = 0
        prcnt = 0.0
        for j in range(0, len(candidates)) :
            if uniqueCandidates[i] == candidates[j] :
    #The total number of votes each candidate won
                tmpVotes +=1
    #The percentage of votes each candidate won
                prcnt = (tmpVotes /len(total_votes)*100)
        candidateVote.append((uniqueCandidates[i],tmpVotes, prcnt))
        print("%s: %.3f %% (%d) Votes" % (uniqueCandidates[i], prcnt, tmpVotes))
    print("-----------------------------------")
    
    #The winner of the election based on popular vote
    for i in range(0, len(candidateVote)-1) :
        winner = ""
        current =candidateVote[i]
        next =candidateVote[i+1]
        if int(current[1]) > int(next[1]) :
            winner = current[0]
        else :
            winner = next[0]
    print("Winner: %s" % winner)
    print("-----------------------------------")    