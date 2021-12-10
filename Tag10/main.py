import numpy as np
from collections import deque

def firstTask():
    bracketCounter = 4 * [0]
    syntaxScore = 0
    syntaxStack = deque()
    with open("input.txt") as file:
       while(line := file.readline().strip()):
           syntaxStack = deque()
           bracketCounter = 4 * [0]
           for c in line:
                if c == '{':
                   bracketCounter[0] +=1
                   syntaxStack.append('{')
                   continue
                if c == '}':
                    bracketCounter[0] -= 1
                    if(bracketCounter[0] < 0):
                        syntaxScore += 1197
                        break
                    if syntaxStack.pop() != '{':
                        syntaxScore += 1197
                        break 
                if c == '(':
                   bracketCounter[1] +=1
                   syntaxStack.append('(')
                   continue
                if c == ')':
                    bracketCounter[1] -= 1
                    if(bracketCounter[1] < 0):
                        syntaxScore += 3
                        break
                    if syntaxStack.pop() != '(':
                        syntaxScore += 3
                        break 
                    
                if c == '<':
                   bracketCounter[2] +=1
                   syntaxStack.append('<')
                   continue
                if c == '>':
                    bracketCounter[2] -= 1
                    if bracketCounter[2] < 0:
                        syntaxScore += 25137
                        break
                    if syntaxStack.pop() != '<':
                        syntaxScore += 25137
                        break
                if c == '[':
                   bracketCounter[3] +=1
                   syntaxStack.append('[')
                   continue
                if c == ']':
                    bracketCounter[3] -= 1
                    if syntaxStack.pop() != '[':
                        syntaxScore += 57
                        break 
                    if bracketCounter[3] < 0:
                        syntaxScore += 57
                        break

    print(syntaxScore)
                
                






if __name__ == "__main__":
    firstTask()