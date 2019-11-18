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



