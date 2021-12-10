import numpy as np
from collections import deque

def firstTask():
    syntaxScore = 0
    syntaxStack = deque()
    with open("input.txt") as file:
       while(line := file.readline().strip()):
           syntaxStack = deque()
           for c in line:
                if c == '{':
                   syntaxStack.append('{')
                   continue
                if c == '}':
                    if syntaxStack.pop() != '{':
                        syntaxScore += 1197
                        break 
                if c == '(':
                   syntaxStack.append('(')
                   continue
                if c == ')':
                    if syntaxStack.pop() != '(':
                        syntaxScore += 3
                        break         
                if c == '<':
                   syntaxStack.append('<')
                   continue
                if c == '>':
                    if syntaxStack.pop() != '<':
                        syntaxScore += 25137
                        break
                if c == '[':
                   syntaxStack.append('[')
                   continue
                if c == ']':
                    if syntaxStack.pop() != '[':
                        syntaxScore += 57
                        break 

    print(syntaxScore)
                
                






if __name__ == "__main__":
    firstTask()