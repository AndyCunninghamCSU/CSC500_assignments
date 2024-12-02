class Node:
    def __init__(self, payload, parent = None, left = None, right = None):
        self.payload = payload
        self.parent = parent
        self.left = left
        self.right = right

class MyTree:
    
    def __init__(self):
        self.__myTree = []

    # adds a node to the tree, updating the parent, filling in the tree from left to right
    # does NOT rebalance.
    # returns -1 if parent has two children before the add, and does not add the node
    # returns None if executes successfully
    def add_node(self, node: Node):

        # find the parent of the new node to update that node's children
        if node.parent:

            parent_index = self.find_node(node.parent.payload)
            if parent_index != -1:
                parent_node = self.__myTree[parent_index]

                # update left first to fill the tree left to right
                if parent_node.left is None:
                    parent_node.left = node
                elif parent_node.right is None:
                    parent_node.right = node
                else:

                    # parent already has two children
                    return -1
        
        # add the child node only after properly updating the tree to avoid corruption if the
        # parent has two children
        self.__myTree.append(node)

    def find_node(self, payload):
        for index, node in enumerate(self.__myTree):
            if node.payload == payload:
                return index
        return -1
    


tree = MyTree()

root_node = Node(payload='root')

tree.add_node(root_node)
child_node = Node(payload='child', parent = root_node)

tree.add_node(child_node)

print (tree.find_node('child'))