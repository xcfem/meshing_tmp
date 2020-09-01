# -*- coding: utf-8 -*-
from __future__ import print_function

import glob

readDecl= False
declarations= list()
funcDeclaration= list()
fileNamesToCMake= list()

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

for fileName in glob.glob("*.c"):
    f= open(fileName, 'r')
    if fileName not in fileNamesToCMake:
        fileNamesToCMake.append(fileName)
    for l in f:
        if(l.startswith('/* Subroutine */ ')):
            l= remove_prefix(l, '/* Subroutine */ ')
            readDecl= True
        if(l.startswith('{')):
            if(readDecl):
                funcDeclaration[-1]= funcDeclaration[-1].strip('\n')
                funcDeclaration[-1]+=';'
                declarations.append(funcDeclaration)
                funcDeclaration= list()
            readDecl= False
        if(readDecl):
            l= l.strip()
            funcDeclaration.append(l)
    f.close()
    
outputFileName= 'paving.ih'

f= open(outputFileName, 'w')
for d in declarations:
    for l in d:
        f.write(l);
    f.write('\n\n')
f.close()


outputFileName= 'paving.cmake'
prefix= 'utility/paving/'

setStr= 'set(paving '
for fName in fileNamesToCMake:
    tmp= fName[:-2]
    setStr+= prefix+tmp+' '
setStr+= ')\n'
print(setStr)
f= open(outputFileName, 'w')
f.write(setStr)
f.close()
