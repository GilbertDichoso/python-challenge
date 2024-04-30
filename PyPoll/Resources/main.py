import csv
import os

# Initialize variables
total_votes = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#shorten the path
# Get the current directory of the script
current_directory = os.path.dirname(__file__)

# Specify the relative path to the CSV file
csv_file_path = os.path.join(current_directory, 'election_data.csv')

# Read the CSV file
with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)
    
    # Iterate through the data
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1
        
        # Count the votes for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Print the election results to the terminal and export them to a text file
with open('election_results.txt', 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    # Iterate through the candidates
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage of votes each candidate won
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        
        # Determine the winner based on the popular vote
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
    
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write("-------------------------\n")
    
    print("-------------------------")
    print(f"Winner: {winning_candidate}")
    print("-------------------------")

