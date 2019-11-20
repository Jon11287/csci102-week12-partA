# https://github.com/Jon11287/csci102-week12-partA.git
# Jonathan Arroyo
# CSCI 102 - Section E
# Week 12 - Part A

def PrintOutput(str):
    print("OUTPUT %s" % (str))

def LoadFile(str):
    with open(str, "r") as my_file:
        ls = my_file.read().split('\n')
        return ls

def UpdateString(str, letter, index):
    ls = list(str)
    ls[index] = letter
    out = ""

    for i in ls:
        out += i

    PrintOutput(out)

def FindWordCount(ls, str):
    count = 0
    stLs = ""
    for i in ls:
        for j in i:
            stLs += j
        stLsNew = stLs.split()
        for i in stLsNew:
            if i == str:
                count += 1

    return count

def ScoreFinder(ls1, ls2, str):
    nameLower = str.lower()
    nameProper = str.title()
    if nameLower in ls1:
        strIndex = ls1.index(nameLower)
        score = ls2[strIndex]
        print(f"OUTPUT {nameProper} got a score of {score}")
    elif nameProper in ls1:
        strIndex = ls1.index(nameProper)
        score = ls2[strIndex]
        print(f"OUTPUT {nameProper} got a score of {score}")
    else:
        print("OUTPUT player not found")

def Union(ls1, ls2):
    ls3 = []
    for i in ls1:
        ls3.append(i)
    for i in ls2:
        if i not in ls3:
            ls3.append(i)
    return ls3

def Intersection(ls1, ls2):
    ls3 = []
    for i in ls1:
        if i in ls2:
            ls3.append(i)
    return ls3

def NotIn(ls1, ls2):
    ls3 = []
    for i in ls1:
        if i not in ls2:
            ls3.append(i)
    return ls3