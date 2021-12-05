import numpy

def firstTask():
    oceanFloor = numpy.zeros([1000,1000], dtype=int)
    with open("input.txt") as file:
       while(line := file.readline()):
        coordianate1, coordinate2 =  line.split(' -> ')
        x1, y1 = [int(x) for x in coordianate1.split(',')]
        x2, y2 = [int(x) for x in coordinate2.split(',')]
        xCoordinates = [x1, x2]
        xCoordinates.sort()
        x1, x2 = xCoordinates
        yCoordinates = [y1, y2]
        yCoordinates.sort()
        y1, y2 = yCoordinates
        if x1 == x2 or y1 == y2: # only horizontal lines
            for x in range(x1,x2+1):
                for y in range(y1, y2+1):
                   oceanFloor[x][y] = oceanFloor[x][y] +1

    print(oceanFloor)
    print((oceanFloor > 1).sum())

if __name__ == "__main__":
    firstTask()