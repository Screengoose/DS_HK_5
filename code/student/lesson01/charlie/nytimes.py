#!/usr/bin/python
# Import required libraries
import sys

# Start a counter for different variables
sumAge, impressions, maxAge = 0, 0, 0
sumClicks = 0.0
lines = sys.stdin.readlines()
lines.pop(0)

# Loop over data
for line in lines:
    impressions = impressions + int(line.strip().split(',')[2])
    sumAge = sumAge + int(line.strip().split(',')[0])
    sumClicks = sumClicks + int(line.strip().split(',')[3])
    if int(line.strip().split(',')[0]) > maxAge:
        maxAge = int(line.strip().split(',')[0])

# Final calculations
averageAge = sumAge/len(lines)-1
clickThroughRate = sumClicks/impressions

# Print output
imp = 'Impressions Sum: ' + str(impressions) + '\n'
avAg = 'Average age: ' + str(averageAge) + '\n'
clThRa = 'Click through rate: ' + str(clickThroughRate) + '\n'
maxA = 'The oldest person in the file is: ' + str(maxAge)
print imp, avAg, clThRa, maxA

# Write to new file
file = open("newfile.txt", "w")
file.write(imp + avAg + clThRa + maxA)
