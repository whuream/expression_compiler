#encoding: utf-8

class semantic_ana():
    def __init__(self, tree):
        self.tree = ['start', tree]
        self.analysis_tree(self.tree, tree)

    def analysis_tree(self, p_node, node):
        if len(node[1]) == 1:
            node = node[1][0]
        for i in node[1]:
            self.analysis_tree(node, i)

