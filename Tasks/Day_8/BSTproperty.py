class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self, root = None):
        self.root = Node(root)

    def insert(self, data):
        self.insert_helper(self.root, data)

    def insert_helper(self, current, data):
        if current.data < data:
            if current.right:
                self.insert_helper(current.right, data)
            else:
                current.right = Node(data)
        else:
            if current.left:
                self.insert_helper(current.left, data)
            else:
                current.left = Node(data)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)


bst = BST()
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)
print(bst.search(9),"\n")
print(bst.search(14),"\n")

tree = BST()
tree.root = Node(12)
tree.root.left = Node(3)
tree.root.right = Node(14)
tree.root.left.left = Node(1)
tree.root.left.right = Node(11)
tree.root.right.left = Node(13)
tree.root.right.right = Node(15)
print(tree.is_bst_satisfied(),"\n")

tree1 = BST()
tree1.root = Node(12)
tree1.root.left = Node(3)
tree1.root.right = Node(14)
tree1.root.left.left = Node(1)
tree1.root.left.right = Node(13)
tree1.root.right.left = Node(11)
tree1.root.right.right = Node(15)
print(tree1.is_bst_satisfied(),"\n")
