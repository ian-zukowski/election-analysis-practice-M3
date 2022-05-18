# my_votes=int(input("How many votes did you recieve?"))
# total_votes=int(input("How many votes were in the election?"))
# percentage_votes=(my_votes/total_votes)*100
# print("I recieved "+str(percentage_votes)+"% of the total votes.")

# # # input two pieces then output using percentage division formula in f.string
# my_votes=int(input("How many votes did you recieve?"))
# total_votes=int(input("How many votes were in the election?"))
# print(f"I recieved {my_votes/total_votes*100}% of the total votes.")


# # # reference values in a dictionary in f.string
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# # same idea, but multiline f.strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes} votes in the election."
    f"You recieved {candidate_votes/total_votes*100}% of the votes in the election.")

print(message_to_candidate)