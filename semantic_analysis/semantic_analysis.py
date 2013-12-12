#encoding: utf-8


class semantic_ana():
    def __init__(self, tree):
        self.tree = ['start', [tree]]
        self.flag = True

        while self.flag:
            self.flag = False
            self.analysis_tree(self.tree, self.tree[1][0])
            self.analysis_tree2(self.tree)

        self.analysis_tree3(self.tree[1][0])


    def analysis_tree(self, p_node, node):  # 去除单链
        if len(node[1]) == 1:
            tmp = node[1][0]
            self.clear_list(node)
            node += tmp
            self.flag = True

        for i in range(0, len(node[1])):
            self.analysis_tree(node, node[1][i])

    def analysis_tree2(self, node):  # 去除非法叶子节点
        tmp = [i for i in node[1] if(len(i[1]) != 0 or i[0] not in ['E', '(', ')', ',', 'I', 'I\''])]
        if len(tmp) != len(node[1]):
            self.clear_list(node[1])
            node[1] += tmp
            self.flag = True

        for i in range(0, len(node[1])):
            self.analysis_tree2(node[1][i])

    def analysis_tree3(self, node):
        children = node[1]
        for item in children:
            if item[0] in ['I', 'I\'']:
                self.analysis_tree3(item)
        for item in children:
            if item[0] in ['-','fo', 'f2', 'mo']:
                children.remove(item)
                if len(item[1]) == 0:  # item is a leaf node
                    node[0] = item[0]
                    #node[2] = item[2]
                else:                  # item is not a leaf node
                    node[0] = item[0]
                    node[1] += item[1]
                    #node[2] = item[2]


    def clear_list(self, l):
        for i in range(0, len(l)):
            l.pop()