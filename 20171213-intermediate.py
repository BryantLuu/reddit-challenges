"""
Description:
Create a program that will solve the banker’s algorithm. This algorithm stops deadlocks from happening by not allowing processes to start if they don’t have access to the resources necessary to finish. A process is allocated certain resources from the start, and there are other available resources. In order for the process to end, it has to have the maximum resources in each slot.

Ex:

Process	Allocation	Max	Available
A B C	A B C	A B C
P0	0 1 0	7 5 3	3 3 2
P1	2 0 0	3 2 2
P2	3 0 2	9 0 2
P3	2 1 1	2 2 2
P4	0 0 2	4 3 3
Since there is 3, 3, 2 available, P1 or P3 would be able to go first. Let’s pick P1 for the example. Next, P1 will release the resources that it held, so the next available would be 5, 3, 2.

The Challenge:
Create a program that will read a text file with the banker’s algorithm in it, and output the order that the processes should go in. An example of a text file would be like this:

[3 3 2]

[0 1 0 7 5 3]

[2 0 0 3 2 2]

[3 0 2 9 0 2]

[2 1 1 2 2 2]

[0 0 2 4 3 3]

And the program would print out:

P1, P4, P3, P0, P2
Bonus:
Have the program tell you if there is no way to complete the algorithm.
"""

def solve_bankers_algorithm(file_path):
    def clean(line):
        split = line.strip('[]\n').split(' ')
        return list(map(lambda x: int(x), split))

    def get_resources_and_processes(file_path):
        file_object = open(os.path.join(os.getcwd(), file_path), 'r')
        index = 0
        resources = None
        processes = dict()
        for line in file_object:
            if index == 0:
                resources = clean(line)
            else:
                processes['P'+str((index-1))] = clean(line)
            index += 1
        return resources, processes

    def find_processable_process(resources, processes):
        for key in processes.keys():
            if (
                resources[0] + processes[key][0] >= processes[key][3] and
                resources[1] + processes[key][1] >= processes[key][4] and
                resources[2] + processes[key][2] >= processes[key][5]
            ):
                return key

    resources, processes = get_resources_and_processes(file_path)
    complete = list()
    while processes:
        process = find_processable_process(resources, processes)
        if not process:
            return complete
        resources[0] += processes[process][0]
        resources[1] += processes[process][1]
        resources[2] += processes[process][2]
        complete.append(process)
        del processes[process]
    return complete

solve_bankers_algorithm('./20171213-intermediate.txt')
