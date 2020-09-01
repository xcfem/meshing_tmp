# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import glob

routineDefs= list()
routineCalls= list()

def getRoutineDefinitions(fileName):
    def getRoutineName(line):
        retval= None
        if('_' in l):
            searchObj= re.search( r'([A-Z,a-z,0-9_]+)_ *\(.*', l, re.M|re.I)
            if(not searchObj):
                print('def ************',l)
            else:
                retval= searchObj.group(1)+'_'
        return retval
        
    if(fileName):
        f = open(fileName, "r")
        for l in f:
            if(l.startswith('/* Subroutine */ ')) or (l.startswith('doublereal ')) or (l.startswith('logical ')) or (l.startswith('void ')) or (l.startswith('integer ')) or (l.startswith('int ')):
                routineName= getRoutineName(l)
                if(routineName):
                    if(not routineName in routineDefs):
                        routineDefs.append(routineName)
        f.close()

def getRoutineCalls(fileName):
    if(fileName):
        f = open(fileName, "r")
        for l in f:
            if(('(' in l) and (not l.startswith('/* Subroutine */ '))):
                if('_' in l):
                    searchObj= re.search( r'([A-Z,a-z,0-9_]+)_\(.*', l, re.M|re.I)
                    if(searchObj):
                        routineName= searchObj.group(1)+'_'
                        if(not routineName in routineCalls):
                            routineCalls.append(routineName)
        f.close()

def writeFindFilesScript(fileName= 'find_files.sh'):
    f = open(fileName, 'w')
    for u in undefined:
        fName= u[:-1]
        f.write('find ../ -name \''+fName+'*\'\n')
    f.close

for fileName in glob.glob("*.c"):
    getRoutineDefinitions(fileName)
    getRoutineCalls(fileName)

undefined= list()
for r in routineCalls:
    if not r in routineDefs:
        undefined.append(r)
print(undefined)

if(len(undefined)> 0):
    writeFindFilesScript()
