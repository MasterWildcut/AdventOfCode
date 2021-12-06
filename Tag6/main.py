import numpy

def firstTask():
    with open("input.txt") as file:
       while(line := file.readline()):
        lanternfish = numpy.asarray(line.split(','), dtype=int)
    print("Initial state:")
    print(lanternfish)
    for day in range(1,81):
        lanternfish = numpy.append(lanternfish, numpy.repeat(9, (lanternfish == 0).sum()))
        lanternfish[lanternfish == 0] = 7
        lanternfish -= 1
        print("After "+ str(day)+ " day")
        print(lanternfish)
    print(len(lanternfish))



if __name__ == "__main__":
    firstTask()