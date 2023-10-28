def zigZagTraversal(self, root):
        result=[]
        if root is None:
            return
        q=[root]
        flag=True
        while q:
            size=len(q)
            row=[0]*size
            for i in range(size):
                node=q.pop(0)
                if flag:
                    index=i
                else:
                    index=size-1-i
            
                row[index]=node.val
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            flag= not flag
            result.append(row)
    
        return result

...........................................................CPP.......................................................


  vector < vector < int >> zigzagLevelOrder(Node * root) {
  vector < vector < int >> result;
  if (root == NULL) {
    return result;
  }

  queue < Node * > nodesQueue;
  nodesQueue.push(root);
  bool leftToRight = true;

  while (!nodesQueue.empty()) {
    int size = nodesQueue.size();
    vector < int > row(size);
    for (int i = 0; i < size; i++) {
      Node * node = nodesQueue.front();
      nodesQueue.pop();

      // find position to fill node's value
      int index = (leftToRight) ? i : (size - 1 - i);

      row[index] = node -> val;
      if (node -> left) {
        nodesQueue.push(node -> left);
      }
      if (node -> right) {
        nodesQueue.push(node -> right);
      }
    }
    // after this level
    leftToRight = !leftToRight;
    result.push_back(row);
  }
  return result;
}
