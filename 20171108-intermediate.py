"""
Description
A carriage company is renting cars and there is a particular car for which the interest is the highest so the company decides to book the requests one year in advance. We represent a request with a tuple (x, y) where x is the first day of the renting and y is the last. Your goal is to come up with an optimum strategy where you serve the most number of requests.

Input Description
The first line of the input will be n the number of requests. The following two lines will consist of n numbers for the starting day of the renting, followed by another n numbers for the last day of the renting corresponding. For all lines 0 < x i < y i <= 365 inequality holds, where i=1, 2, ..., n.

10
1 12 5 12 13 40 30 22 70 19
23 10 10 29 25 66 35 33 100 65
Output Description
The output should be the maximum number of the feasable requests and the list of these requests. One possible result may look like this:

4
(1,23) (30,35) (40,66) (70,100)
But we can do better:

5
(5,10) (13,25) (30,35) (40,66) (70,100)
Remember your goal is to find the scenario where you serve the most number of costumers.

Credit
This challenge was suggested by user /u/bessaai
, many thanks. If you have a challenge idea, please share it in /r/dailyprogrammer_ideas and there's a good chance we'll use it.
"""

def most_appointments(appointments):
    appointments = appointments.split('\n')
    appointments = zip(
        [int(x) for x in appointments[0].strip().split(' ')],
        [int(x) for x in appointments[1].strip().split(' ')]
    )
    sorted_by_end = sorted(appointments, key=lambda x: int(x[1]))
    results = [sorted_by_end[0]]
    del sorted_by_end[0]
    while sorted_by_end:
        to_delete = []
        for index, appointment in enumerate(sorted_by_end):
            if appointment[0] > results[-1][1]:
                results.append(appointment)
                to_delete.append(appointment)
                break
            to_delete.append(appointment)
        for appointment in to_delete:
            sorted_by_end.remove(appointment)
    return results

most_appointments(
    """11 12 5 12 13 40 30 22 70 19
    23 10 10 29 25 66 35 33 100 65"""
)
