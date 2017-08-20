# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self):
        self.children = []

    def addChild(self, c):
        self.children.append(c)

class TreeHeight:
    def __init__(self):
        self.nodes = []
        self.root = Node()
        self.tree_height = 0

    def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

            for i in range(0, self.n):
                self.nodes.append(Node())

            for child_index in range(0, self.n):
                self.parent_index = self.parent[child_index]

                if self.parent_index  == -1:
                    self.root = self.nodes[child_index]
                else:
                    self.nodes[self.parent_index].addChild(self.nodes[child_index])

    def print_tree_iteratively(self):
        for i in range(len(self.nodes)):
            print("Node {}'s children are:".format(i))
            print(self.nodes[i].children)

    def print_tree(self, node):
        if node == self.root:
            print("Root node:")
            print("{}\n".format(node))

        if len(node.children):
            print("{}'s children are:".format(node))
            print("{}\n".format(node.children))
            for child in node.children:
                self.print_tree(child)

    def max_height(self, node, current_height):
        current_height += 1
        if len(node.children):
            for child in node.children:
                return max(self.max_height(child, current_height), current_height)
        else:
            return current_height


    def compute_height(self):
        self.tree_height = self.max_height(self.root, 0)
        print('the tree height is: {}'.format(self.tree_height))

def main():
  tree = TreeHeight()
  tree.read()
  #tree.print_tree(tree.root)
  tree.compute_height()

threading.Thread(target=main).start()
