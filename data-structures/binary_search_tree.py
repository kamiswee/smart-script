# binary_search_tree.py
#
# K. Sweebe

# A binary search tree is a node-based binary tree data structure which has
# the following properties:
#     - For each node n in a BST, all node elements in the left subtree are
#       less than n
#     - For each node n in a BST, all node elements in the right subtree are
#       greater than n
#     - For each node n in a BST, the left and right subtrees are also BSTs
#
#
# binary_search_tree.py has the following contents:
#     - node class
#


# node class
class Node:
    def __init__(self, data):
        """
        Node Constructor
        """
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        """
        metadata
        """
        return str(self.data)


    def insert(self, data):
        """
        Insert new node with data
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
        @param data: node data object to look up
        @param parent: node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data,self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data,self)
        else:
            return self, parent

    def children_count(self):
        """
        Returns whether a single node has 0, 1, or 2 children
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        """
        Delete node containing data

        There are 3 possibilities to handle
            1. the node to remove has no children
            2. the node to remove has 1 child
            3. the node to remove has 2 children
        """
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # then just remove the Node
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    # it's the root
                    self.data = None

            elif children_count == 1:
                # then check if it has a left or right child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    # it's the root
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data

            else:
                # node has two children
                # find the successor of the node
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node by successor data
                node.data = successor.data
                # fix successor's parent's child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def print_tree(self):
        """
        Print tree in order
        """
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()


# Test our class for BST
DEBUG = True
if DEBUG == True:
    root = Node(8)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(7)
    root.insert(14)
    root.insert(13)
    print "\n\nOur Tree: "
    root.print_tree()

    node, parent = root.lookup(6)
    print "\n\nLookup node: {0}, parent: {1}".format(node, parent)
    root.delete(1)
    print "\n\nDelete entry of 1."
    node, parent = root.lookup(1)
    print "\n\nLookup node: {0}, parent: {1}".format(node, parent)
    root.print_tree()

    print "\n\nDelete entry of 14"
    root.delete(14)
    root.print_tree()

    print "\n\nDelete entry of 3"
    root.delete(3)
    root.print_tree()

    print "\n\nNow try a tree with multiple values"
    root.insert(6)
    root.insert(6)
    root.print_tree()

    print "\n\nDelete entry of 6"
    root.delete(6)
    root.print_tree()

    print "\n\nDelete entry of 4"
    root.delete(4)
    root.print_tree()
