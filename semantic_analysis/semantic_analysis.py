#encoding: utf-8


class node():
    def __init__(self, parent_node, child, attribute):
        self.parent = parent_node
        self.child = child
        self.attribute = attribute

class semantic_ana():
    def __init__(self, tree):
        self.tree = ['start', [tree]]
        self.analysis_tree(self.tree, tree[1][0])

    def analysis_tree(self, p_node, node):
        if len(node[1]) == 1:
            tmp = node[1][0]
            node.pop()
            node.pop()
            node += tmp

        for i in range(0, len(node[1]) - 1):
            self.analysis_tree(node, node[1][i])

