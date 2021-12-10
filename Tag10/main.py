import numpy as np
from collections import deque

def firstTask():
    syntaxScore = 0
    syntaxStack = deque()
    autoCompleteScores = []
    with open("input.txt") as file:
       while(line := file.readline().strip()):
           checkAutoComplete(syntaxStack, autoCompleteScores)

           syntaxStack = deque()
           for c in line:
                if c == '{':
                   syntaxStack.append('{')
                   continue
                if c == '}':
                    if syntaxStack.pop() != '{':
                        syntaxScore += 1197
                        syntaxStack.clear()
                        break 
                if c == '(':
                   syntaxStack.append('(')
                   continue
                if c == ')':
                    if syntaxStack.pop() != '(':
                        syntaxScore += 3
                        syntaxStack.clear()
                        break         
                if c == '<':
                   syntaxStack.append('<')
                   continue
                if c == '>':
                    if syntaxStack.pop() != '<':
                        syntaxScore += 25137
                        syntaxStack.clear()
                        break
                if c == '[':
                   syntaxStack.append('[')
                   continue
                if c == ']':
                    if syntaxStack.pop() != '[':
                        syntaxScore += 57
                        syntaxStack.clear()
                        break 
    checkAutoComplete(syntaxStack, autoCompleteScores)
    print(syntaxScore)
    autoCompleteScores.sort()
    print(autoCompleteScores)
    print(autoCompleteScores[int(len(autoCompleteScores)/2)])

def checkAutoComplete(syntaxStack, autoCompleteScores):
    # check last incomplete Line
    if syntaxStack:
        score = 0
        syntaxStack.reverse()
        for d in syntaxStack:
            score *= 5
            if d == '{':
                score += 3
                continue
            if d == '(':
                score += 1
                continue
            if d == '<':
                score += 4
                continue
            if d == '[':
                score += 2
                continue
        autoCompleteScores.append(score)
                
                






if __name__ == "__main__":
    firstTask()