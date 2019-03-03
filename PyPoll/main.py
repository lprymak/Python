import csv
import os

# Read file - actual file input begins on line 82
def loadFile(filename):

    print(os.getcwd())
    pth = os.path.join(filename)
    with open(filename) as file:

        reader = csv.reader(file, delimiter=',')
        hdr = next(file,None)
        matrix = []
        matrix.append([[item for item in row] for row in reader])
        return matrix

# Isolate candidate names into separate list from original data matrix
def pullCandidatesList(matrix, candidateIndex):

    votesByCandidate = []
    for list in matrix:

        votesByCandidate.append(list[candidateIndex])

    return votesByCandidate

# Calculat total vote counts for each candidate
def findVoteCount(votesByCandidate):

    CANDIDATES = []
    VOTE_COUNT = []

    for candidateName in votesByCandidate:

        if not candidateName in CANDIDATES:

            CANDIDATES.append(candidateName)
            VOTE_COUNT.append(1)

        else:
            indexC = CANDIDATES.index(candidateName)
            indexC = int(indexC)
            TOTAL = VOTE_COUNT[indexC]
            VOTE_COUNT[indexC] = TOTAL + 1
      
    return VOTE_COUNT, CANDIDATES

# Calculate each candidate's percentage of total votes and store in a list corresponding to candidate
#   names and totals    
def findPercentage(candidateList, voteTotalList, overallTotal):

    PERCENTAGES = []
    for name in candidateList:

        indexP = candidateList.index(name)
        candidateCount = voteTotalList[indexP]
        percentage = (candidateCount / overallTotal) * 100
        percentage = round(percentage, 2)
        PERCENTAGES.append(percentage)
        
    return PERCENTAGES

# Calculate the winning candidate by comparing vote totals
def findWinner(listA, listB):

    for x in range(1, len(listA)):

        winningCount = listB[0]
        winningName = listA[0]
        if listB[x] > winningCount:

            winningCount = listB[x]
            winningName = listA[x]

        else:
            winningCount = winningCount
            winningName = winningName

    return winningName

# Read election_data.csv file and identify index for candidate names:
#  the only three inputs that need to be changed
OriginalData = loadFile('election_data.csv')
nameIndex = 2
outputFile = "PollResults.txt"

OriginalData = OriginalData[0]

# Calculate total votes overall
TotalVotes = len(OriginalData)

# Separate candidate names into one list
VoteByCandidate = pullCandidatesList(OriginalData, nameIndex)

# Lists of calculated total votes for each candidate and candidate names in corresponding list
resultsTotals = findVoteCount(VoteByCandidate)[0]
resultsCandidates = findVoteCount(VoteByCandidate)[1]

# List of calculated percentages of total votes per each candidate
resultsPercentages = findPercentage(resultsCandidates, resultsTotals, TotalVotes)

# Calculate winner
Winner = findWinner(resultsCandidates, resultsTotals)

# Print results
print(f"""
Election Results
-------------------------
Total Votes: {TotalVotes}
------------------------- """)
for x in range(0, len(resultsCandidates)):
    print(f"{resultsCandidates[x]}: {resultsPercentages[x]}% ({resultsTotals[x]})")
print(f"""-------------------------
Winner: {Winner}
-------------------------
""")

# Write results to text file
txtfile = open(outputFile, "w")

txtfile.write(f"""Election Results
-------------------------
Total Votes: {TotalVotes}
-------------------------
""")
for x in range(0, len(resultsCandidates)):
    txtfile.write(f"{resultsCandidates[x]}: {resultsPercentages[x]}% ({resultsTotals[x]})\n")
txtfile.write(f"""-------------------------
Winner: {Winner}
-------------------------""")

txtfile.close()