"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example



The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

int steps: the number of steps on the hike
string path: a string describing the path
Returns

int: the number of valleys traversed
Input Format

The first line contains an integer , the number of steps in the hike.
The second line contains a single string , of  characters that describe the path.

Constraints

Sample Input

8
UDDDUDUU
Sample Output

1
"""
import datetime
#  Solution 1


def counting_valleys(steps):
    level = valleys = 0
    for step in steps:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys


n = int(input())
s = input().upper()
start_time = datetime.datetime.now()
print(counting_valleys(s))
end_time = datetime.datetime.now()
print(end_time - start_time)


# Solution 2 (best)
start_time = datetime.datetime.now()
lvl = val = 0
for i in range(len(s)):
    if lvl == 0 and s[i] == 'D':
        val += 1
    if s[i] == 'U':
        lvl += 1
    else:
        lvl -= 1
print(val)
end_time = datetime.datetime.now()
print(end_time - start_time)