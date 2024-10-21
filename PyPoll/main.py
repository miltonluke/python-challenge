# -*- coding: UTF-8 -*-
#"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_names = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winner = ""
max_votes = 0
results = []

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
            
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]
        
            # Add candidate to the list if not already present
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1
            candidate_names.append(candidate)  # Get the candidate's name
        else:  
            # If the candidate is already in the dictionary, increment their vote count
            candidate_votes[candidate] += 1   

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_names:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
        # Determine the winner
        if votes > max_votes:
            max_votes = votes
            winner = candidate

# Generate and print the winning candidate summary
summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
# Print each candidate's vote count and percentage
for result in results:
    summary += f"{result}\n"

# Save the winning candidate summary to the text file
summary += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)

# Print the results
print(summary)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(summary)     