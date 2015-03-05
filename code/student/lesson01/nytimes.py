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
print 'Impressions Sum:', impressions
print 'Average age:', averageAge
print 'Click through rate:', clickThroughRate
print 'The oldest person in the file is:', maxAge
