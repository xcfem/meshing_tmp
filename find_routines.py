# -*- coding: utf-8 -*-
from __future__ import print_function

import re

def getRoutineCalls(fileName):
    retval= list()
    if(fileName):
        f = open(fileName, "r")

        for l in f:
            ul= l.upper()
            if((ul[0]!='C')and (ul[0]!='c')):
                if('CALL ' in ul):
                    searchObj= re.search( r'CALL +([A-Z,a-z,0-9]+) *\(.*', ul, re.M|re.I)
                    if(not searchObj):
                        searchObj= re.search( r'CALL +([A-Z,a-z,0-9]+) *.*', ul, re.M|re.I)
                    if(not searchObj):
                        print('************',ul)
                    else:
                        retval.append(searchObj.group(1))
        f.close()
    return retval

def getRoutineDefinitions(fileName):
    retval= list()
    f = open(fileName, "r")

    for l in f:
        ul= l.upper()
        if((ul[0]!='C')and (ul[0]!='c')):
            if(' SUBROUTINE ' in ul):
                searchObj= re.search( r'SUBROUTINE +([A-Z,a-z,0-9]+) *\(.*', ul, re.M|re.I)
                if(not searchObj):
                    searchObj= re.search( r'SUBROUTINE +([A-Z,a-z,0-9]+) *.*', ul, re.M|re.I)
                if(not searchObj):
                    print('************',ul)
                else:
                    retval.append(searchObj.group(1))
            if(' FUNCTION ' in ul):
                searchObj= re.search( r'FUNCTION +([A-Z,a-z,0-9]+) *\(.*', ul, re.M|re.I)
                if(not searchObj):
                    searchObj= re.search( r'FUNCTION +([A-Z,a-z,0-9]+) *.*', ul, re.M|re.I)
                if(not searchObj):
                    print('************',ul)
                else:
                    retval.append(searchObj.group(1))
    f.close()
    return retval

routineDefinitionMap= dict()
fortranFiles = open('fortran_file_list.txt', "r")
for l in fortranFiles:
    fileName= l.rstrip()
    routineDefinitions= getRoutineDefinitions(fileName)
    #print(fileName, routineDefinitions)
    for r in routineDefinitions:
        routineDefinitionMap[r]= fileName

#Exceptions.
notFound= list()
        
rootFileName= "./seacas/applications/fastq/paving.f"
routineCalls= getRoutineCalls(rootFileName)

#print(routineCalls)

def getNextLevel(oldCalls):
    newCalls= list()
    for call in oldCalls:
        if(call in routineDefinitionMap):
            defFileName= routineDefinitionMap[call]
            #print(call, defFileName)
            tmpCalls= getRoutineCalls(defFileName)
            for r in tmpCalls:
                if((r not in routineCalls) and (r not in newCalls)):
                    newCalls.append(r)
        else:
            notFound.append(call)
    return newCalls

newCalls= getNextLevel(routineCalls)

while(len(newCalls)>0):
    routineCalls.extend(newCalls)
    newCalls= getNextLevel(newCalls)

filesToCompile= list()
for r in routineCalls:
    if(r not in notFound):
        fileName= routineDefinitionMap[r]
        filesToCompile.append(fileName)
    
print('routine calls: ', routineCalls)
print('exceptions: ', notFound)
print('files to compile: ', filesToCompile, len(filesToCompile))

f= open('lista.sh', 'w')
for fName in filesToCompile:
    f.write(fName)
    f.write('\n')
f.close()
    
