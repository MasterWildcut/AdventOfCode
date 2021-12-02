import collections

def firstTask():
    horizontalPosition = 0
    depthPosition = 0
    with open("input.txt") as file:
        while (line := file.readline()):
            command = line.split()
            if (command[0] == 'forward'):
                horizontalPosition += int(command[1])
                continue
            if (command[0] == 'down'):
                depthPosition += int(command[1])
                continue
            if (command[0] == 'up'):
                depthPosition -= int(command[1])
                continue
            print("Unrecoginzed" + command[0])
            break
            
    print(horizontalPosition)
    print(depthPosition)
    print(depthPosition*horizontalPosition)

def secondTask():
    horizontalPosition = 0
    depthPosition = 0
    aim = 0
    with open("input.txt") as file:
        while (line := file.readline()):
            command = line.split()
            if (command[0] == 'forward'):
                horizontalPosition += int(command[1])
                depthPosition = depthPosition + aim * int(command[1])
                continue
            if (command[0] == 'down'):
                aim += int(command[1])
                continue
            if (command[0] == 'up'):
                aim -= int(command[1])
                continue
            print("Unrecoginzed" + command[0])
            break
            
    print(horizontalPosition)
    print(depthPosition)
    print(depthPosition*horizontalPosition)



if __name__ == "__main__":
    secondTask()