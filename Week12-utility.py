# https://github.com/Jon11287/csci102-week12-partA.git
# Jonathan Arroyo
# CSCI 102 - Section E
# Week 12 - Part A

def PrintOutput(str):
    out = "OUTPUT %s" % (str)
    return out

def LoadFile(str):
    with open(str, "r") as my_file:
        ls = my_file.read().split('\n')
        return PrintOutput(ls)

def UpdateString(str, letter, index):
    ls = list(str)
    ls[index] = letter
    out = ""

    for i in ls:
        out += i

    return PrintOutput(out)



