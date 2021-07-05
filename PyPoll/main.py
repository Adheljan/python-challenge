import os
import csv

electioncsvpath = os.path.join('Resources', 'election_data.csv')

total = 0
khan = 0
correy = 0
li = 0
otooley = 0

with open(electioncsvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        total += 1
        if (row[2] == "Khan"):
            khan += 1
        elif (row[2] == "Correy"):
            correy += 1
        elif (row[2] == "Li"):
            li += 1
        else:
            otooley += 1
            
    kahn_percent = khan / total
    correy_percent = correy / total
    li_percent = li / total
    otooley_percent = otooley / total
    
    winner = max(khan, correy, li, otooley)

    if winner == khan:
        name_of_winner = "Khan"
    elif winner == correy:
        name_of_winner = "Correy"
    elif winner == li:
        name_of_winner = "Li"
    else:
        name_of_winner = "O'Tooley" 

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total}")
print(f"---------------------------")
print(f"Kahn: {kahn_percent:.3%}({khan})")
print(f"Correy: {correy_percent:.3%}({correy})")
print(f"Li: {li_percent:.3%}({li})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley})")
print(f"---------------------------")
print(f"Winner: {name_of_winner}")
print(f"---------------------------")

output_file = os.path.join('analysis', 'election_data.text')

with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {name_of_winner}\n")
    txtfile.write(f"---------------------------\n")