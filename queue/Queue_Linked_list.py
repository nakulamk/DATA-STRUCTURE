class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Queue:
  def __init__(self):
    self.front=None
    self.rear=None

  def enque(self,data):
    newnode=Node(data)
    if self.rear is None and self.front is None:
      self.front=self.rear=newnode
    else:
      self.rear.next=newnode
      self.rear=newnode
  
  def deque(self):
    if self.front is None:
      print("que is Empty")
      return None
    else:

      temp=self.front
      self.front=self.front.next
      print(f"del is ele is ${temp.data}")
      return temp.data
    
  def display(self):
    if self.front is None:
      print("Queue is empty")
      return None
    else:
      temp=self.front
      while temp:
        print(temp.data,end=" ")
        temp=temp.next
      print()
  
  def peek(self):
    if self.front is None:
      print("que is empty")
      return
    else:
      print(f"first ele is {self.front.data}")
      return self.front.data
    
q=Queue()

q.enque(10)
q.enque(20)
q.enque(30)
q.display()
q.deque()
q.display()
q.enque(40)
q.display()
q.peek()


