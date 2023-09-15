# class Node:
#   def __init__(self,value):
#     self.Rchild=None
#     self.data=value
#     self.Lchild=None

# class BST:
#   def __init__(self,key) :
#     self.key=key
#     self.rchild=None
#     self.lchild=None
  

#   # for insertion 2 condition
#   # 1.if root is present or not 
#   # 2.if root is present then we need to check for which side to insert the node either left or right 
#   def insert(self,data):
#     # check if there is root node is there or not 
#     if self.key is None:
#       self.key=data
#       return
#     if self.key==data:
#       return
#     # if it is present we need to insert at left side
#     if data<self.key:
#       # if key is present and if we have lchild attached need to look where to insert
#       if self.lchild:
#         self.lchild.insert(data)
#       # if no lchild is present just insert 
#       else:
#         self.lchild=BST(data)
#     # if data is greater than child
#     #  we need to insert at right side
#     else:
#       # if key is present and if we have lchild attached need to look where to insert
#       if self.rchild:
#         self.rchild.insert(data)
#       # if no rchild is present just insert
#       else:
#         self.rchild=BST(data)

#   def Search(self,data):
#     if self.key==data:
#       print("Node is found")
#       return
#     if data<self.key:
#       if self.lchild:
#         self.lchild.Search(data)
#       else:
#         print("Node is not found")
#     else:
#       if self.rchild:
#         self.rchild.Search(data)
#       else:
#         print('Node is not present')
  
#   def SearchNode(self,data,parentNode):
#     if self is None:
#       return
    
#     if (self.key==data):
#       return self
    
#     nodeToBeSearched=None

#     if data<self.key:
#       parentNode=self
#       nodeToBeSearched=self.lchild.SearchNode(data,parentNode)
#       return nodeToBeSearched
    
#     if data>self.key:
#       parentNode=self
#       nodeToBeSearched=self.rchild.SearchNode(data,parentNode)
#       return nodeToBeSearched


#   def SearchWithParent(self,data):
#     if self is None:
#       print("Tree is empty")
#       return
#     if self.key==data:
#       print("Data is the Root")
#     else:
#       parentNode=None
#       nodeTobeSearched=self.SearchNode(data,parentNode)
#       if nodeTobeSearched==None:
#         print("data not found")
#       else:
#         print(f"{nodeTobeSearched.key} is found and its parent is {parentNode.key}")

#   def PreOrder(self):
#     if self is None:
#       return
#     print(self.key,end=' ')
#     if self.lchild:
#       self.lchild.PreOrder()
#     if self.rchild:
#       self.rchild.PreOrder()

#   def PostOrder(self):
#     if self is None:
#       return
#     if self.lchild:
#       self.lchild.PostOrder()
#     if self.rchild:
#       self.rchild.PostOrder()
#     print(self.key,end=" ")

#   def InOrder(self):
#     if self is None:
#       return
#     if self.lchild:
#       self.lchild.InOrder()
#     print(self.key,end=' ')
#     if self.rchild:
#       self.rchild.InOrder()

#   def displayTree(self):
#     if self is None:
#       print("Tree is empty")
#       return 
#     print(f"InOrder--")
#     self.InOrder()
#     print('\nPre-Order--')
#     self.PreOrder()
#     print("\nPost- ORDER--")
#     self.PostOrder()

#   #DELETION 
#   # CONDITION 1 CHECK TREE IS EMPTY OR NOT
#   # IF THER FIND AND DELETE
#   def DeleteNode(self,data):
#     if self is None:
#       print("tree is empty\n")
#       return
#     # If the node to be deleted is the root and has children
#     if self.key==data and (self.lchild!=None or self.rchild!=None):
#       print("Root node can't be deleted unless it has no child.\n")
#       return
#     # CASE 1: If the node to be deleted is the root and has no children.
#     if self.key ==data and self.lchild==None and self.rchild==None:
#       print(f"Deleted root node with data= {self.key}")
#       del self
#       self=None
#       return
    

#     # SEARCH NODE
#     parentNode=None
#     nodeToBeDeleted=self.SearchNode(data,parentNode)
#     if (nodeToBeDeleted==None):
#       print("node with data does not exist")
#       return
#     else:
#       print("data deleted")
    
#     # CASE 2: If the node to be deleted is a leaf node.
#     if nodeToBeDeleted.lchild==None and  nodeToBeDeleted.rchild==None:
#       if nodeToBeDeleted==parentNode.lchild:
#         parentNode.rchild=None
#       else:
#         parentNode.rchild=None
  


# root=BST(None)
# list1=[10,6,98,3,7,1]
# for i in list1:
#   root.insert(i)

# root.displayTree()
# root.SearchWithParent(98)


























# root=BST(10)
# print(root.key)
# print(root.lchild)
# print(root.rchild)

# now in root.lchild we have address of the new node that is created
# root.lchild=BST(5)
# print(root.key)
# when we print root.lchild we get the address of new node created
# print(root.lchild)

# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)



class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_new_node(self):
        data = int(input("Enter the data: "))
        new_node = Node()
        new_node.data = data
        new_node.left = None
        new_node.right = None

        if self.root is None:
            print("New node inserted as the root")
            self.root = new_node
            return

        child_node = self.root
        previous_node = None

        while child_node is not None:
            previous_node = child_node
            if child_node.data >= new_node.data:
                child_node = child_node.left
            else:
                child_node = child_node.right

        if previous_node.data > new_node.data:
            previous_node.left = new_node
        else:
            previous_node.right = new_node

        print("New node inserted")

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        print(root.data, end=' ')
        self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data, end=' ')

    def pre_order(self, root):
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def display_tree(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("\nInOrder Traversal: ", end='')
        self.in_order(self.root)
        print("\nPostOrder Traversal: ", end='')
        self.post_order(self.root)
        print("\nPreOrder Traversal: ", end='')
        self.pre_order(self.root)
        print()

    def search_node(self, root, data, parent_node):
        if root is None:
            return None
        node_to_be_searched = None
        if root.data == data:
            node_to_be_searched = root
        if node_to_be_searched is None:
            parent_node[0] = root
            if root.data > data:
                node_to_be_searched = self.search_node(root.left, data, parent_node)
            else:
                node_to_be_searched = self.search_node(root.right, data, parent_node)
        return node_to_be_searched

    def search(self):
        if self.root is None:
            print("Tree is empty")
            return
        data = int(input("Enter the data of the node to be searched: "))
        if self.root.data == data:
            print("Searching node data =", data, "and it is the root of the tree")
        else:
            parent_node = [None]
            node_to_be_searched = self.search_node(self.root, data, parent_node)

            if node_to_be_searched is None:
                print("Node with data =", data, "doesn't exist in the tree")
            else:
                print("Searching node data =", node_to_be_searched.data, "and its parent node data =", parent_node[0].data)

    def delete_node(self):
        if self.root is None:
            print("Tree is empty")
            return
        data = int(input("Enter the data of the node to be deleted: "))
        if self.root.data == data and (self.root.left is not None or self.root.right is not None):
            print("Root node can't be deleted unless it has no child.")
            return
        if self.root.data == data and self.root.left is None and self.root.right is None:
            print("Deleted root node with data =", self.root.data)
            del self.root
            self.root = None
            return

        parent_node = [None]
        node_to_be_deleted = self.search_node(self.root, data, parent_node)
        if node_to_be_deleted is None:
            print("Node with data =", data, "doesn't exist in the tree")
            return
        else:
            print("Deleting node data =", node_to_be_deleted.data, "and its parent node data =", parent_node[0].data)

        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            if node_to_be_deleted == parent_node[0].left:
                parent_node[0].left = None
            else:
                parent_node[0].right = None
            del node_to_be_deleted
        elif (node_to_be_deleted.left is not None and node_to_be_deleted.right is None) or (
                node_to_be_deleted.left is None and node_to_be_deleted.right is not None):
            if node_to_be_deleted.right is None:
                if node_to_be_deleted == parent_node[0].left:
                    parent_node[0].left = node_to_be_deleted.left
                else:
                    parent_node[0].right = node_to_be_deleted.left
            else:
                if node_to_be_deleted == parent_node[0].left:
                    parent_node[0].left = node_to_be_deleted.right
                else:
                    parent_node[0].right = node_to_be_deleted.right
            del node_to_be_deleted
        else:
            is_node = node_to_be_deleted.right
            isp_node = node_to_be_deleted
            while is_node.left is not None:
                isp_node = is_node
                is_node = is_node.left
            node_to_be_deleted.data = is_node.data
            if is_node.left is None and is_node.right is None:
                if is_node == isp_node.left:
                    isp_node.left = None
                else:
                    isp_node.right = None
            else:
                if is_node == isp_node.left:
                    isp_node.left = is_node.right
                else:
                    isp_node.right = is_node.right
            del is_node
        print("Node deleted with data:", data)

    def height_of_tree(self, root):
        if root is None:
            return 0
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)
        return max(left_height, right_height) + 1

    def find_height(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("Height of the tree is:", self.height_of_tree(self.root) - 1)


if __name__ == "__main__":
    bst = BinarySearchTree()
    while True:
        print("\n0.Exit\n1.Insert\n2.Display\n3.Search\n4.Delete\n5.Find height")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            bst.insert_new_node()
        elif choice == 2:
            bst.display_tree()
        elif choice == 3:
            bst.search()
        elif choice == 4:
            bst.delete_node()
        elif choice == 5:
            bst.find_height()
        else:
            print("Enter a proper choice")
