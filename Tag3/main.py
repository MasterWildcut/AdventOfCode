import numpy

def firstTask():
    gammaRateCounter = numpy.zeros(12,dtype=int)
    gammaRate = 0
    epsilonRate = 0
    # epsilonCounter = numpy.zeros(12,dtype=int)
    with open("input.txt") as file:
        while (line := file.readline()):
            for idx, val in enumerate(line):
                if (val == '0'):
                    gammaRateCounter[idx] -= 1
                    continue
                if (val == '1'):
                    gammaRateCounter[idx] += 1
                    continue
    
    print(gammaRateCounter)
    for idx, val in enumerate(gammaRateCounter):
        if(gammaRateCounter[idx]> 0):
            gammaRate += (2 ** (11-idx))
        else:
            epsilonRate += (2 ** (11-idx))
    
    print(gammaRate)
    print(epsilonRate)
    print(gammaRate*epsilonRate)

def secondTask():
    measurements = ["" for x in range(1000)]
    idx = 0

    oxygenGeneratorRatingCount = float('inf')
    cOTwoGeneratorRatingCount = float('inf')
    oxygenString = ''
    cOTwoString = ''
    with open("input.txt") as file:
        while (line := file.readline()):
            measurements[idx] = line
            idx += 1
    measurements.sort()
    while(oxygenGeneratorRatingCount > 1):
        measureZero =numpy.char.startswith(measurements, oxygenString+'0', start=0)
        measureOne =numpy.char.startswith(measurements, oxygenString+'1', start=0)
        print(0)
        print(sum(measureZero))
        print(1)
        print(sum(measureOne))
        oxygenString += '0' if sum(measureZero)>sum(measureOne) else '1'
        print(oxygenString)
        oxygenGeneratorRatingCount = sum(numpy.char.startswith(measurements, oxygenString, start=0))
    while(cOTwoGeneratorRatingCount > 1):
        measureZero =numpy.char.startswith(measurements, cOTwoString+'0', start=0)
        measureOne =numpy.char.startswith(measurements, cOTwoString+'1', start=0)
        cOTwoString += '1' if sum(measureZero)>sum(measureOne) else '0'
        cOTwoGeneratorRatingCount = sum(numpy.char.startswith(measurements, cOTwoString, start=0))
        print(0)
        print(sum(measureZero))
        print(1)
        print(sum(measureOne))
        print(cOTwoString)
        

    oxygenGeneratorRating = measurements[numpy.argmax(numpy.char.startswith(measurements, oxygenString, start=0))]
    cotwoRating = measurements[numpy.argmax(numpy.char.startswith(measurements, cOTwoString, start=0))]
    print(cOTwoString)
    print(oxygenString)
    print(oxygenGeneratorRating)
    print(cotwoRating)
    print(int(oxygenGeneratorRating,2))
    print(int(cotwoRating,2))
    print(int(cotwoRating,2)*int(oxygenGeneratorRating,2))




if __name__ == "__main__":
    secondTask()