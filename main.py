#encoding: utf-8
__author__ = 'ST'

import os
from syntax_analysis.syntax_analysis import syntax_tree

str = r'./compiler.exe in.txt _out.txt'
os.system(str)
print '\n'
content = open('_out.txt', 'r').read()
m = syntax_tree(content)
if m.legal and m.flag:
    print 'syntax abalysis succeed.\ntree: '
    print m.tree