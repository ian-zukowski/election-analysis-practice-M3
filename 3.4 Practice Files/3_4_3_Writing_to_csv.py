import csv
import os

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the results and *read* the file
# with open(file_to_load,'r') as election_data:

# #To-do: Perform analysis
#     print(election_data)

# #Close the file
# election_data.close()



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as outfile:
    # Write some data to outfile
    outfile.write("Counties in the Election\n-------------------------\n")
    outfile.write("Arapahoe\nDenver\nJefferson")
    # Close the file
    outfile.close