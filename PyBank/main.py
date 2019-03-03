import csv
import os

# Read file  - actual file input begins line 71
def loadFile(filename):

    print(os.getcwd())
    pth = os.path.join(filename)
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        hdr = next(file)
        matrix = []
        matrix.append([[x for x in row] for row in reader])
        return matrix

# Find sum of list[index] in matrix
def total(matrix, dataIndex):

    total = 0
    for list in matrix:
        for item in list:
            total += int(item[dataIndex])
    return total

# Calculate average, maximum, minimum from data matrix; specifying indeces for numeric and string data
def averageMinMax(data_List, numberIndex, dateIndex):

    # Separate the Profit/Losses in to a list
    totals = [[item[numberIndex] for item in entry] for entry in data_List]

    # Create a list of the change in each two Profit/Loss values
    changes = [(int(totals[0][x]) - int(totals[0][x - 1])) for x in range(1, len(totals[0]))]

    # Calculate average change in profit/loss
    averageChange = sum(changes) / len(changes)

    # Calculate maximum change in profit/loss and corresponding month/year
    months = [[item[dateIndex] for item in entry] for entry in data_List]
    monthlyChange = [months[0][n] for n in range(1, len(months[0]))]
    maxMonth = monthlyChange[0]
    maxChange = changes[0]

    for i in range(1, len(changes)):

        if changes[i] >= maxChange:

            maxChange = changes[i]
            maxMonth = monthlyChange[i]
        else:
            maxChange = maxChange
            maxMonth = maxMonth

    # Calculate minimum change in profit/loss and corresponding month/year
    minChange = changes[0]
    minMonth = monthlyChange[0]

    for x in range(1, len(changes)):

        if changes[x] <= minChange:

            minChange = changes[x]
            minMonth = monthlyChange[x]

        else:
            minChange = minChange
            minMonth = minMonth

    return averageChange, maxChange, maxMonth, minChange, minMonth

# Load budget_data.csv file into a matrix and identify indices for the data to be totaled and the month/year         
Profit_Loss_Data = loadFile('budget_data.csv')
PLIndex = 1
MnthIndex = 0
outputFile = "BankResults.txt"

# Find totals
netTotal = total(Profit_Loss_Data, PLIndex)
totalMonths = len(Profit_Loss_Data[0])

# List of calculated average monthly change
averageChanges = averageMinMax(Profit_Loss_Data, PLIndex, MnthIndex)[0]
averageChanges = round(averageChanges, 2)

# Calculated greatest increase
greatIncreaseMonth = averageMinMax(Profit_Loss_Data, PLIndex, MnthIndex)[2]
greatIncrease = averageMinMax(Profit_Loss_Data, PLIndex, MnthIndex)[1]

# Calculated greatest decrease
greatDecreaseMonth = averageMinMax(Profit_Loss_Data, PLIndex, MnthIndex)[4]
greatDecrease = averageMinMax(Profit_Loss_Data, PLIndex, MnthIndex)[3]

# Print to terminal
output = (f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netTotal}
Average Change: ${averageChanges}
Greatest Increase: {greatIncreaseMonth} (${greatIncrease})
Greatest Decrease: {greatDecreaseMonth} (${greatDecrease})""")

print(f"""
{output}
""")

# Write to text file
txtfile = open(outputFile, "w")
txtfile.write(output)
txtfile.close()