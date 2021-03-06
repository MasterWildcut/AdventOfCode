import numpy as np
import scipy as sp
from scipy import ndimage
from collections import Counter

def firstTask():
    rows = 100
    columns = 100
    heatMap = np.empty((rows,columns), dtype=int)
    i = 0
    with open("input.txt") as file:
       while(line := file.readline().strip()):
           heatMap[i] = [int(x) for x in list(line)]
           i += 1
    
    # horizontal sink map
    sinkHorizontal = np.empty((rows,columns), dtype=bool)
    sinkVertical = np.empty((rows,columns), dtype=bool)

    for r in range(rows):
        for c in range(columns):
            if(c == 0):
                sinkHorizontal[r][c] = heatMap[r][c] < heatMap[r][c+1]
                continue
            if (c == (columns-1)):
                sinkHorizontal[r][c] = heatMap[r][c] < heatMap[r][c-1]
                continue
            sinkHorizontal[r][c] = heatMap[r][c-1] > heatMap[r][c] and heatMap[r][c] < heatMap[r][c+1]

        for c in range(columns):
            for r in range(rows):
                if(r == 0):
                    sinkVertical[r][c] = heatMap[r][c] < heatMap[r+1][c]
                    continue
                if (r == (rows-1)):
                    sinkVertical[r][c] = heatMap[r][c] < heatMap[r-1][c]
                    continue
                sinkVertical[r][c] = heatMap[r-1][c] > heatMap[r][c] and heatMap[r][c] < heatMap[r+1][c]
    
    print(heatMap)
    # print(sinkHorizontal)
    # print(sinkVertical)
    sinkMap = np.logical_and(sinkVertical, sinkHorizontal)
    print(sinkMap)
    heatMap += 1
    print(sum(heatMap[sinkMap]))

def secondTask():
    heatMap = np.genfromtxt("input.txt", delimiter=1, dtype=int)
    areas, _ = ndimage.label(heatMap < 9)
    c = Counter(areas.flatten())

    print(areas)
    print(c)
    print(c.most_common(4))
    print(np.prod([value for key, value in c.most_common(4)[1:]])) # do not count the nines




if __name__ == "__main__":
    secondTask()