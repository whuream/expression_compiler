#encoding: utf-8
__author__ = 'ST'

import re

class syntax_tree():
    def __init__(self, content):
        self.content = content
        self.legal = True if re.match(r'\nflag\s*=\s*(0|1)', content).group(1) == '0' else False
        self.list = re.findall(
            r'^Find ((\d+|\+|-|\*|/|\^|e|PI|,|log|sin|cos|tan|asin|acos|atan|ln|lg|\(|\)) in (\d+) to (\d+))',
            content, re.M)
        self.list.append(['', '$', 0, 0])
        self.list.reverse()
        self.item = [{'symbol': item[1],
                      'type': 'num' if re.match(r'\d+|PI|e', item[1]) else
                              '(' if item[1] == '(' else
                              ')' if item[1] == ')' else
                              ',' if item[1] == ',' else
                              '-' if item[1] == '-' else
                              'fo' if re.match(r'sin|cos|tan|asin|acos|atan|ln|lg', item[1]) else
                              'f2' if item[1] == 'log' else 'mo' if re.match(r'\+|\*|/|\^', item[1]) else
                              item[1],
                      'value': int(item[1]) if re.match(r'\d+', item[1]) else
                               3.14 if item[1] == 'PI' else
                               2.72 if item[1] == 'e' else
                               None,
                      'field': (item[2], item[3])
                      } for item in self.list]

        self.table = {'S': {'(': ('I',),
                           '-': ('I',),
                           'fo': ('I',),
                           'num': ('I',),
                           'f2': ('I',)},
                      'I': {'(': ('(', 'I', ')', 'I\''),
                            '-': ('f1', 'I', 'I\''),
                            'fo': ('f1', 'I', 'I\''),
                            'num': ('num', 'I\''),
                            'f2': ('f2', '(', 'I', ',', 'I', ')', 'I\'')},
                      'I\'': {'-': ('m2', 'I', 'I\''),
                              'mo': ('m2', 'I', 'I\''),
                              ')': ('E',),
                              ',': ('E',),
                              '$': ('E',)},
                      'm2': {'-': ('-',),
                             'mo': ('mo',)},
                      'f1': {'-': ('-',),
                             'fo': ('fo',)}
                      }
        self.terminal = ['(', '-', 'fo', 'num', 'f2', 'mo', ')', ',', 'E']
        self.unterminal = ['S', 'I', 'I\'', 'm2', 'f1']
        self.tree = ['S', []]
        self.flag = True
        if self.legal:
            try:
                self.solve(self.tree)
            except Exception:
                print self.tree
                self.flag = False

    def solve(self, node):
        if node[0] in self.terminal:
            if node[0] != 'E' and self.item[-1].get('type') != '$':
                self.item.pop()
            return
        if not self.item:
            return
        ex = self.table.get(node[0]).get(self.item[-1].get('type'))
        if not ex:
            symbol = self.item[-1].get('symbol')
            begin, end = self.item[-1].get('field')
            print '\nsynatax analysis failed.\nbegin in %s, end in %s, symbol: %s' %(begin, end, symbol)
            raise Exception
        node[1] = [[i, [], self.item[-1]] for i in ex]
        #node[1] = [[i, []] for i in ex]
        for i in node[1]:
            self.solve(i)


if __name__ == '__main__':
    content = open('a.txt', 'r').read()
    a = syntax_tree(content)
    if a.flag:
        print a.tree