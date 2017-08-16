#Python3
#Crappy tree

class Node:
    def __init__(self, c=None):
        self.content = c
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def remove_child(self, index):
        self.children.pop[index]
    
    def print_node(self):
        print(self.content)

class Tree:
    def __init__(self, r=None):
        self.root = r
    
    def set_root(self, r):
        self.root = r

    def print_tree(self, node):
        print (node.content)
        if node.children:
            for i in node.children:
                print("The below node is a child of node {}".format(node.content))
                self.print_tree(i)
        elif node.children == []:
            print("^ this node has no children")

root_node = Node(-1)
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

root_node.add_child(node0)
root_node.add_child(node1)
node1.add_child(node2)
node1.add_child(node3)

t = Tree(root_node)

t.print_tree(t.root)

