# Import required libraries
from __future__ import division
import sys
import csv

# Start a counter and store the textfile in memory
lines = sys.stdin.readlines()
lines.pop(0)

# Get max_age to determine number of lines needed
max_age = 0

def getColumn(line,idx):
	return int(line[idx])

for line in lines:
	line = line.strip().split(',')
	max_age = max(max_age, getColumn(line, 0))


# Open new file to write to
file = open("newfile.txt", "w")

# Logic for looping through csv to get summary statistics
def getSummary(age, gender, signed_in):
    people = 0
    totalClicks = 0
    totalImpressions = 0
    max_click = 0
    max_impressions = 0

    for line in lines:
        line = line.strip().split(',')

        if age-1 == int(line[0]) and gender == int(line[1]) and signed_in == int(line[4]):
            people = people + 1
            totalClicks = totalClicks + int(line[3])
            totalImpressions = totalImpressions + int(line[2])
            max_click = max(max_click, int(line[3]))
            max_impressions = max(max_impressions, int(line[2]))

    if people == 0:
        averageClicks = 0
        averageImpressions = 0
    else:
        averageClicks = totalClicks / people
        averageImpressions = totalImpressions / people

    file.write(str(averageClicks) + "," + str(averageImpressions) + "," + str(max_click) + "," + str(max_impressions) + "\n")


# Create lines in csv for age, gender and signed in and run summary statistics for each line
for x in range(0, max_age+2):
    if x == 0:
        file.write("age" + "," + "gender" + "," + "signed_in" + "," + "avg_click" + "," + "avg_impressions" + "," + "max_click" + "," + "max_impressions" + "\n")
    else:
        file.write(str(x-1) + "," + "0" + "," + "0" + ",")
        getSummary(x, 0, 0)
        file.write(str(x-1) + "," + "1" + "," + "0" + ",")
        getSummary(x, 1, 0)
        file.write(str(x-1) + "," + "0" + "," + "1" + ",")
        getSummary(x, 0, 1)
        file.write(str(x-1) + "," + "1" + "," + "1" + ",")
        getSummary(x, 1, 1)
