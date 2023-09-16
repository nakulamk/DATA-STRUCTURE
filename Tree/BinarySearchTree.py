class Node:
  def __init__(self,value):
    self.Rchild=None
    self.data=value
    self.Lchild=None

class BST:
  def __init__(self,key) :
    self.key=key
    self.rchild=None
    self.lchild=None
  

  # for insertion 2 condition
  # 1.if root is present or not 
  # 2.if root is present then we need to check for which side to insert the node either left or right 
  def insert(self,data):
    # check if there is root node is there or not 
    if self.key is None:
      self.key=data
      return
    if self.key==data:
      return
    # if it is present we need to insert at left side
    if data<self.key:
      # if key is present and if we have lchild attached need to look where to insert
      if self.lchild:
        self.lchild.insert(data)
      # if no lchild is present just insert 
      else:
        self.lchild=BST(data)
    # if data is greater than child
    #  we need to insert at right side
    else:
      # if key is present and if we have lchild attached need to look where to insert
      if self.rchild:
        self.rchild.insert(data)
      # if no rchild is present just insert
      else:
        self.rchild=BST(data)

  def Search(self,data):
    if self.key==data:
      print("Node is found")
      return
    if data<self.key:
      if self.lchild:
        self.lchild.Search(data)
      else:
        print("Node is not found")
    else:
      if self.rchild:
        self.rchild.Search(data)
      else:
        print('Node is not present')
  
  def SearchNode(self,data,parentNode):
    if self is None:
      return
    
    if (self.key==data):
      return self
    
    nodeToBeSearched=None

    if data<self.key:
      parentNode=self
      nodeToBeSearched=self.lchild.SearchNode(data,parentNode)
      return nodeToBeSearched
    
    if data>self.key:
      parentNode=self
      nodeToBeSearched=self.rchild.SearchNode(data,parentNode)
      return nodeToBeSearched


  def SearchWithParent(self,data):
    if self is None:
      print("Tree is empty")
      return
    if self.key==data:
      print("Data is the Root")
    else:
      parentNode=None
      nodeTobeSearched=self.SearchNode(data,parentNode)
      if nodeTobeSearched==None:
        print("data not found")
      else:
        print(f"{nodeTobeSearched.key} is found and its parent is {parentNode.key}")

  def PreOrder(self):
    if self is None:
      return
    print(self.key,end=' ')
    if self.lchild:
      self.lchild.PreOrder()
    if self.rchild:
      self.rchild.PreOrder()

  def PostOrder(self):
    if self is None:
      return
    if self.lchild:
      self.lchild.PostOrder()
    if self.rchild:
      self.rchild.PostOrder()
    print(self.key,end=" ")

  def InOrder(self):
    if self is None:
      return
    if self.lchild:
      self.lchild.InOrder()
    print(self.key,end=' ')
    if self.rchild:
      self.rchild.InOrder()

  def displayTree(self):
    if self is None:
      print("Tree is empty")
      return 
    print(f"InOrder--")
    self.InOrder()
    print('\nPre-Order--')
    self.PreOrder()
    print("\nPost- ORDER--")
    self.PostOrder()

  #DELETION 
  # CONDITION 1 CHECK TREE IS EMPTY OR NOT
  # IF THER FIND AND DELETE
  def Delete(self,data):
    if self is None:
      print("tree is empty\n")
      return
    
  


root=BST(None)
list1=[10,6,98,3,7,1]
for i in list1:
  root.insert(i)

root.displayTree()
root.SearchWithParent(98)


























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
