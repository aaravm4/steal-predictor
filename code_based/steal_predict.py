#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:18:41 2019

@author: aaravm
"""
from itertools import permutations
import string
try:
    num_Points = int(input("How many data points do you have: "))
except ValueError:
    print("Invalid Command.")
while num_Points > 26:
    print("Max Number of Data Points is 26")
    num_Points = int(input("How many data points do you have: "))
points = []
for i in range(num_Points):
    alph = string.ascii_lowercase
    for k in range(2):
        points.append(alph[i])
num_check_points  =[]
for i in points:
    if i not in num_check_points:
        num_check_points.append(i)
perms = permutations(points, 2)
optDict = {("".join(p)): 0 for p in perms}
nameDict = {p: '' for p in points}
print("Welcome to the Sign Stealer.", end = "")
print("Please encode the following data points: ", end = "")
for i in num_check_points:
    encodedName = input("Encode test point {}:  ".format(i))
    nameDict[i] = encodedName
seqCount = 0
while True:
    resp = input("Enter e to end program or press enter to continue: ")
    if resp == 'e':
        break
    else:
        seqCount += 1
        print("Please type in the order of the moves (remember to only put {} letters): ".format(num_Points))
        print("Remember that: ")
        for i in nameDict:
            print("{} represents {}".format(i, nameDict[i]))
        order = input("Now please input the order: ")
        steal = input("If it was a steal put in y otherwise put n: ")
        while steal != 'y' and steal != 'n':
            print("Invalid Command.")
            steal = input("If it was a steal put in y otherwise put n: ")
        if steal == 'y':
            aDict = {}
            count = 0
            while count < len(order) - 1:
                if count != len(order):
                    aDict[order[count]] = order[count + 1]
                count += 1
            trash = []
            listed = []
            for entry in aDict:
                    trash.append(entry)
                    trash.append(aDict[entry])
                    listed.append(("".join(trash)))
                    trash = []
            for entry in optDict:
                try:
                    if aDict[entry] not in listed:
                        del(optDict[entry])
                except KeyError:
                    pass
            for i in listed:
                try:
                    optDict[i] += 1
                except KeyError:
                    pass
            maximum = 0
            bestChoice = ''
            for i in optDict:
                if optDict[i] > maximum:
                    maximum = optDict[i]
                    bestChoice = i
            print("Solved in {} sequences.".format(seqCount))
            print("Prediction {} then a {} is a steal.".format(nameDict[bestChoice[0]], nameDict[bestChoice[1]]))
        else:
            aDict = {}
            count = 0
            while count < len(order) - 1:
                if count != len(order):
                    aDict[order[count]] = order[count + 1]
                count += 1
            trash = []
            listed = []
            for entry in aDict:
                trash.append(entry)
                trash.append(aDict[entry])
                listed.append(("".join(trash)))
                trash = []
            for i in listed:
                try:
                    del(optDict[i])
                except KeyError:
                    pass
            maximum = 0
            bestChoice = ''
            for i in optDict:
                if optDict[i] > maximum:
                    maximum = optDict[i]
                    bestChoice = i
            try:
                print("Prediction {} then a {} is a steal.".format(nameDict[bestChoice[0]], nameDict[bestChoice[1]]))
            except IndexError:
                names = []
                i = 0
                while i < 2:
                    for entry in optDict:
                        names.append(entry)
                    i += 1
                print("Prediction {} then a {} is a steal.".format(nameDict[names[0][:1]], nameDict[names[0][:1]]))
