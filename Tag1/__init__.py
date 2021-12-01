import collections

def singleIncrease():
    lastLine = float('inf')
    counterIncreased = 0
    with open("input.txt") as file:
        while (line := file.readline()):
            currentline = int (line)
            if( currentline > lastLine):
                counterIncreased += 1
            lastLine = currentline

    print(counterIncreased)

def slidingWindow():
    counterIncreased = 0
    lastMeasurement = float('inf')
    slidingWindowDepths = collections.deque(maxlen=3)
    with open("input.txt") as file:
        while (line := file.readline()):
            slidingWindowDepths.append(int (line))
            if( len(slidingWindowDepths) == 3):
                if (sum(slidingWindowDepths) > lastMeasurement):
                    counterIncreased += 1
                lastMeasurement = sum(slidingWindowDepths)
                slidingWindowDepths.popleft()
                

    print(counterIncreased)



if __name__ == "__main__":
    slidingWindow()