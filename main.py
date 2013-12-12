#encoding: utf-8
__author__ = 'ST'

import os
from syntax_analysis.syntax_analysis import syntax_tree
from semantic_analysis.semantic_analysis import semantic_ana
import sys


def control(middle_name, out_name):

    middle_file = open(middle_name, 'r')
    content = middle_file.read()
    middle_file.close()

    m = syntax_tree(content)
    if m.legal and m.flag:
        print '\nsyntax analysis succeed.\ntree: '
        print m.tree

        m2 = semantic_ana(m.tree)
        print '\nsemantic analysis succeed.\ntree:'
        print m2.tree

        o = open(out_name, 'w')
        for i in m2.tuple_4:
            for j in i:
                o.write(str(j) + ' ')
            o.write('\n')
        o.close()
        print '\nBuild succeed\nwrite file ' + out_name


def main():
    in_name = ''
    middle_name = ''
    out_name = ''
    if len(sys.argv) == 1:
        print 'useage: %s <inputfile> [outputfile]' %(sys.argv[0])
        return
    in_name = sys.argv[1]
    if len(sys.argv) == 3:
        out_name = sys.argv[2]
        middle_name = sys.argv[2] + '.o'
    else:
        middle_name = 'a.o'
        out_name = 'a.txt'

    win = True

    abspath = os.path.abspath(sys.argv[0])
    index = abspath.rfind('\\')
    com = ''
    now_path = os.getcwd()
    if index != -1:
        win = True
        abspath = abspath[:index]
        #middle_name = now_path + '\\' + middle_name
        com = abspath + '\\compiler.exe' + ' ' + in_name + ' ' + middle_name
    else:
        index = abspath.rfind('/')
        win = False
        abspath = abspath[:index]
        #middle_name = now_path + '/' + middle_name
        com = abspath + '/compiler.exe' + ' ' + in_name + ' ' + middle_name

    os.system(com)
    control(middle_name, out_name)

if __name__ == '__main__':
    main()
