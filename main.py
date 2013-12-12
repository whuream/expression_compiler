#encoding: utf-8
__author__ = 'ST'

import os
from syntax_analysis.syntax_analysis import syntax_tree
from semantic_analysis.semantic_analysis import semantic_ana

str = r'compiler.exe in.txt _out.txt'
os.system(str)
print '\n'
content = open('_out.txt', 'r').read()
m = syntax_tree(content)
if m.legal and m.flag:
    print 'syntax abalysis succeed.\ntree: '
    print m.tree

m2 = semantic_ana(m.tree)
print m2.tree
print m2.tuple_4


