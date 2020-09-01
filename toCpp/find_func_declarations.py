# -*- coding: utf-8 -*-
from __future__ import print_function

import re
import glob

readDecl= False
declarations= list()
funcDeclaration= list()

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

for fileName in glob.glob("*.c"):
    f= open(fileName, 'r')
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
    
outputFileName= 'paving.h'

f= open(outputFileName, 'w')
for d in declarations:
    for l in d:
        f.write(l);
    f.write('\n\n')
f.close()
