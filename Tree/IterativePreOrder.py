def preOrder(root):
  preOrder=[]
  if root is None:
    return preOrder
  st=[]
  s.append(root)
  while st:
    node=s.pop()
    preOrder.append(node.data)
    if node.right:
      s.append(node.right)
    if node.left:
      s.append(node.left)
   return preOrder
.............................................CPP..........................................
vector < int > preOrderTrav(node * curr) {
  vector < int > preOrder;
  if (curr == NULL)
    return preOrder;

  stack < node * > s;
  s.push(curr);

  while (!s.empty()) {
    node * topNode = s.top();
    preOrder.push_back(topNode -> data);
    s.pop();
    if (topNode -> right != NULL)
      s.push(topNode -> right);
    if (topNode -> left != NULL)
      s.push(topNode -> left);
  }
  return preOrder;

}
