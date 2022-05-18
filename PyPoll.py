# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Starting variable at 0 to find total votes for entire election
total_votes=0

# Empty list to find amount of candidates
candidate_options=[]

# Empty dictionary to find votes for each candidate
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
     # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:

        ## print every ballot
        # print(row)

        #add 1 to total_votes with each row
        total_votes+=1

        #get candidate name from each row
        candidate_name=row[2]

        #check if name isn't already included -- if not included then add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
        
        #Add one each time that name shows up
        candidate_votes[candidate_name]+=1

#Save the results to the txt file
with open(file_to_save,'w') as txt_file:
    election_results=(
        f"\n"
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results,end='')
    txt_file.write(election_results)

    # # print statement saying each candidate and how many votes they recieved
    # for candidate_name in candidate_options:
    #     print(f"Candidate {candidate_name} recieved {candidate_votes[candidate_name]:,} votes.")


    # get percentage of votes for each candidate in candidate_options
    for candidate_name in candidate_options:
        #set variable to gather vote amounts from the dictionary
        votes=candidate_votes[candidate_name]
        #takes votes/total*100
        vote_percentage=(votes/total_votes)*100
        # #print each candidate and how much % of the votes they recieved
        # print(f"{candidate_name} recieved {vote_percentage:.2f}% of the votes.")

        #print statement-- [Candidate]: [Percentage Earned] and [Vote Count]
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})")
        candidate_results=(
            f"{candidate_name}: {vote_percentage:.2f}% ({votes})\n"
        )

        print(candidate_results)
        txt_file.write(candidate_results)

        #finding winning values for candidate, count, and percentage
        #doesn't it only need one of these two conditions to be true??
        if (vote_percentage>winning_percentage) and (votes>winning_count):
            winning_candidate=candidate_name
            winning_count=votes
            winning_percentage=vote_percentage


    # # my winning message
    # print(f"{winning_candidate} won the election with {winning_count:,} votes.\n{winning_candidate} recieved {winning_percentage:.2f}% of the votes.")

    # their winning message
    winning_summary=(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"-------------------------\n"
    )
    #print(winning_summary)

    txt_file.write(winning_summary)