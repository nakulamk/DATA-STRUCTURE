# Need to Learn
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

class BinaryTree:
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

        direction = input("Enter the direction (e.g., 'L' or 'R'): ")
        current_node = self.root
        previous_node = None

        for char in direction:
            previous_node = current_node
            if char == 'L' or char == 'l':
                current_node = current_node.left
            elif char == 'R' or char == 'r':
                current_node = current_node.right
            else:
                break

        if current_node is not None:
            print("Invalid direction or node already exists at the given direction. Try a new direction.")
            self.insert_new_node()

        if direction[-1] == 'L' or direction[-1] == 'l':
            previous_node.left = new_node
        elif direction[-1] == 'R' or direction[-1] == 'r':
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
            node_to_be_searched = self.search_node(root.left, data, parent_node)
        if node_to_be_searched is None:
            parent_node[0] = root
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
        elif (node_to_be_deleted.left is not None and node_to_be_deleted.right is None) or (node_to_be_deleted.left is None and node_to_be_deleted.right is not None):
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
                del is_node
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
    bt = BinaryTree()
    while True:
        print("\n0.Exit\n1.Insert\n2.Display\n3.Search\n4.Delete\n5.Find height")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            exit(0)
        elif choice == 1:
            bt.insert_new_node()
        elif choice == 2:
            bt.display_tree()
        elif choice == 3:
            bt.search()
        elif choice == 4:
            bt.delete_node()
        elif choice == 5:
            bt.find_height()
        else:
            print("Enter a proper choice")