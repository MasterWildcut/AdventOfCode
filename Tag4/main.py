import numpy

def firstTask():

    with open("input.txt") as file:
       luckyNumbers = numpy.array(file.readline().split(','),int)
       boardCounter = -1
       axisCounter = -1
       bingoBoard = numpy.empty([100, 5,5],dtype=int)
       while(line := file.readline()):
           if(line == '\n'):
               boardCounter += 1
               axisCounter = 0
               continue
           bingoBoard[boardCounter][axisCounter] = numpy.array(line.split(),int)
           axisCounter += 1

    for luckyNumber in luckyNumbers:
        bingoBoard[numpy.where(bingoBoard == luckyNumber)] = -1
        for i in range(100):
            if -5 in numpy.sum(bingoBoard[i], axis=0) or -5 in numpy.sum(bingoBoard[i], axis=1):
                print(bingoBoard[i])
                print(i)
                print(luckyNumber)
                print(numpy.sum(bingoBoard[i][bingoBoard[i]>0]))
                print(luckyNumber * numpy.sum(bingoBoard[i][bingoBoard[i]>0]))
                break


def secondTask():
    with open("input.txt") as file:
        luckyNumbers = numpy.array(file.readline().split(','),int)
        boardCounter = -1
        axisCounter = -1
        bingoBoard = numpy.empty([100, 5,5],dtype=int)
        while(line := file.readline()):
            if(line == '\n'):
                boardCounter += 1
                axisCounter = 0
                continue
            bingoBoard[boardCounter][axisCounter] = numpy.array(line.split(),int)
            axisCounter += 1
    won = numpy.zeros((100), dtype=bool)
    for luckyNumber in luckyNumbers:
        bingoBoard[numpy.where(bingoBoard == luckyNumber)] = -1
        for i in range(100):
            if(won[i]):
                continue
            if -5 in numpy.sum(bingoBoard[i], axis=0) or -5 in numpy.sum(bingoBoard[i], axis=1):
                won[i] = 1
                if (sum(won) == 100):
                    print(bingoBoard[i])
                    print(i)
                    print(luckyNumber)
                    print(numpy.sum(bingoBoard[i][bingoBoard[i]>0]))
                    print(luckyNumber * numpy.sum(bingoBoard[i][bingoBoard[i]>0]))
                    exit()

def scripts():
    bingoBoard = numpy.arange(0,25, dtype=float)
    bingoBoard = numpy.reshape(bingoBoard, (5,5))
    print(bingoBoard)
    print(numpy.sum(bingoBoard, axis=0))
    print(numpy.sum(bingoBoard, axis=1))

    bingoBoard[0][0] = -1
    bingoBoard[0][1] = -1
    bingoBoard[0][2] = -1
    bingoBoard[0][3] = -1
    bingoBoard[0][4] = -1

    print(bingoBoard)
    print(numpy.sum(bingoBoard, axis=0))
    print(numpy.sum(bingoBoard, axis=1))
    print("true" if -5 in numpy.sum(bingoBoard, axis=0) else "false")
    print("true" if -5 in numpy.sum(bingoBoard, axis=1) else "false")
    print(numpy.sum(bingoBoard[bingoBoard>0]))
    print(numpy.sum(bingoBoard))


if __name__ == "__main__":
    secondTask()