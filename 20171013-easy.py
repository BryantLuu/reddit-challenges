"""
Description
What day of the week did hitler get elected on?

What day of the week did the Normans invade Britain on?

What day of the week did Jesus die on?

What day of the week did MacDonald get founded on?

Today we're gonna find out

For todays challenge you are allowed to use your languages built in Calender functions/classes.

But it's more interesting if you do the calculation yourself :)

Hint
It's leap-year if the year is divisible by 4

Ignore leap-year if the year is divisible by 100

Ignore previous rule if the year is divisible by 400

Input example
The input will be 3 integers as such:

YEAR MONTH DATE

Limits for the 3 integers:

8000 > YEAR > 0

13 > MONTH > 0

32 > DATE > 0

Sorry to anyone starting at 0.

January is 1 and December is 12

Assume all dates to be correct (i.e. no 31th of february)

Input will look like:

2017 10 30
Output example
Output is simply the day of the week of the given date, for above it would be:

Monday
Challenge input
2017 10 30
2016 2 29
2015 2 28
29 4 12
570 11 30
1066 9 25
1776 7 4
1933 1 30
1953 3 6
2100 1 9
2202 12 15
7032 3 26
Extra
If you have any challenges, please share it at /r/dailyprogrammer_ideas!

And remember to upvote challenges you like :)
"""
def day_of_the_week(line):
    daysOfWeek = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    split = line.split(' ')
    year, month, day = int(split[0]), int(split[1]) , int(split[2])
    if month <= 2:
        year -= 1
        month = 14
    if month <= 1:
        month = 13
    K = year % 100
    J = int(year/100)
    m = month
    q = day
    return daysOfWeek[(q + int((13 * (m + 1)) / 5) + K + int(K / 4) + int(J / 4) + 5 * J) % 7]

def find_days_of_the_week(lines):
    for line in lines.split('\n'):
        print(day_of_the_week(line.strip()))

find_days_of_the_week(
""" 2017 10 30
    2016 2 29
    2015 2 28
    29 4 12
    570 11 30
    1066 9 25
    1776 7 4
    1933 1 30
    1953 3 6
    2100 1 9
    2202 12 15
    7032 3 26""")
