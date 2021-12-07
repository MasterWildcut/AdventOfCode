import numpy as np
from collections import Counter

def firstTask():
    with open("input.txt") as file:
       while(line := file.readline()):
        crabs = np.asarray(line.split(','), dtype=int)

    p = [0] * (np.max(crabs)+1)
    for k,v in Counter(crabs).items():
        p[k] = v

    print(p)
    bestPosition = 0
    bestUsedFuel = float('inf')
    usedFuel = 0
    for i in range(max(crabs)+1):
        for key,value in enumerate(p):
            usedFuel += np.abs(i-key)*value
        if(usedFuel < bestUsedFuel):
            bestPosition = i
            bestUsedFuel = usedFuel
        print(i)
        print(usedFuel)
        usedFuel = 0

    print(bestPosition)
    print(bestUsedFuel)
    

def secondTask():
    with open("input.txt") as file:
       while(line := file.readline()):
        crabs = np.asarray(line.split(','), dtype=int)

    p = [0] * (np.max(crabs)+1)
    for k,v in Counter(crabs).items():
        p[k] = v

    distanceMatrix = np.empty(np.max(crabs)+1, dtype=int)
    for i in range(len(distanceMatrix)):
        if (i == 0):
            distanceMatrix[i] = 0
            continue
        distanceMatrix[i] = distanceMatrix[i-1] + i 


    print(p)
    bestPosition = 0
    bestUsedFuel = float('inf')
    usedFuel = 0
    for i in range(max(crabs)+1):
        for key,value in enumerate(p):
            usedFuel += distanceMatrix[np.abs(i-key)]*value
        if(usedFuel < bestUsedFuel):
            bestPosition = i
            bestUsedFuel = usedFuel
        print(i)
        print(usedFuel)
        usedFuel = 0

    print(bestPosition)
    print(bestUsedFuel)
    





if __name__ == "__main__":
    secondTask()