#encoding: utf-8


class semantic_ana():
    def __init__(self, tree):
        self.tree = ['start', [tree]]
        self.flag = True

        while self.flag:
            self.flag = False
            self.analysis_tree(self.tree, self.tree[1][0])
            self.analysis_tree2(self.tree)


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
        if node[0] not in ['I', 'I\'']:
            return
        children = node[1]
        if children[1]:
            pass



    def clear_list(self, l):
        for i in range(0, len(l)):
            l.pop()