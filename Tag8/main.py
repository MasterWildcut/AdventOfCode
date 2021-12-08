import numpy as np
from collections import Counter

def firstTask():
    numberLights = [0] * 10 # counter for lights
    with open("input.txt") as file:
       while(line := file.readline().strip()):
        _ , numberLine = line.split(' | ')
        numbers = numberLine.split(' ')
        for n in numbers:
            if len(n) == 4:
                numberLights[4] += 1
                continue
            if len(n) == 2:
                numberLights[1] += 1
                continue
            if len(n) == 3:
                numberLights[7] += 1
                continue
            if len(n) == 7:
                numberLights[8] += 1
                continue
        
    print(numberLights)
    print(sum(numberLights))




if __name__ == "__main__":
    firstTask()