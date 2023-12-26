


# import random


# class Node:
#     def __init__(self, val=0):
#         self.val = val
#         self.right = None
#         self.left = None

# class Tree:

#     def __init__(self):
#         self.root = None
    
#     def insert(self, val):
#         def recInsert(node):
#             if not node:
#                 return Node()
#             if val < node.val:
#                 node
        
    
#     def traverse(self):
        
#         def inorder_traversal( node):
#             if node == None:
#                 return
#             inorder_traversal(node.left)
#             print(node.val, end = " ")
#             inorder_traversal(node.right)
#         inorder_traversal(self.root)

# if __name__ == "__main__":

#     tree = Tree()
#     print("random numbers: ")
#     for i in range(10):
#         num = random.randint(1,100)
#         print(num, end = ' ')
#         tree.insert(num)
#     print()
#     tree.traverse()




import random
class Node:

    def __init__(self, val = 0):
        self.val = val
        # self.lchild = self.rchild = None
        self.left=self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

class Tree:

    def __init__(self):
        self.root = None
    
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        
        def insert_rec(node, val):
            if val < node.val:
                if node.left ==None:
                    node.left = Node(val)
                else:
                    insert_rec(node.left,val)
            else:
                if node.right == None:
                    node.right = Node(val)
                else:
                    insert_rec(node.right, val)
        insert_rec(self.root, val)
    
    def traverse(self):
        self.inorder_trav(self.root)
    
    def inorder_trav(self, node):
        if not node:
            return
        self.inorder_trav(node.left)
        print(node.val, end = ' ')
        self.inorder_trav(node.right)

if __name__ == "__main__":

    tree = Tree()
    print("random numbers: ")
    for i in range(10):
        num = random.randint(1,100)
        tree.insert(num)
        print(num, end = ' ')
    print()
    tree.traverse()


        