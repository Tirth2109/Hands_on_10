class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left:
                self._insert_recursive(node.left, key)
            else:
                node.left = TreeNode(key)
        elif key > node.key:
            if node.right:
                self._insert_recursive(node.right, key)
            else:
                node.right = TreeNode(key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right = self._delete_recursive(node.right, min_larger_node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)


class AVLTreeNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return AVLTreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursive(node.right, result)

    def _get_height(self, node):
        return node.height if node else 0

    def _balance(self, node):
        balance_factor = self._get_height(node.left) - self._get_height(node.right)
        if balance_factor > 1:
            if self._get_height(node.left.left) >= self._get_height(node.left.right):
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance_factor < -1:
            if self._get_height(node.right.right) >= self._get_height(node.right.left):
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)


class RedBlackTreeNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackTreeNode(None, color='black')  # Sentinel NIL node
        self.root = self.NIL

    def insert(self, key):
        new_node = RedBlackTreeNode(key)
        new_node.left = self.NIL
        new_node.right = self.NIL
        self._insert(new_node)

    def _insert(self, new_node):
        y = None
        x = self.root
        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if not y:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        new_node.color = 'red'
        self._fix_insert(new_node)

    def _fix_insert(self, z):
        while z != self.root and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._rotate_left(z.parent.parent)
        self.root.color = 'black'

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        node = self.root
        while node != self.NIL and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node != self.NIL

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node != self.NIL:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


# Test Code with Outputs
def test_trees():
    # Binary Search Tree Test
    bst = BinarySearchTree()
    for key in [10, 5, 20, 3, 7]:
        bst.insert(key)
    print("Binary Search Tree (BST):")
    print("In-order after insertions:", bst.inorder_traversal())
    print("Search for 10:", bst.search(10))
    print("Search for 15:", bst.search(15))
    bst.delete(10)
    print("In-order after deletion of 10:", bst.inorder_traversal())
    print()

    # AVL Tree Test
    avl = AVLTree()
    for key in [10, 5, 20, 3, 7]:
        avl.insert(key)
    print("AVL Tree:")
    print("In-order after insertions:", avl.inorder_traversal())
    print("Search for 10:", avl.search(10))
    print("Search for 15:", avl.search(15))
    avl.delete(10)
    print("In-order after deletion of 10:", avl.inorder_traversal())
    print()

    # Red-Black Tree Test
    rbt = RedBlackTree()
    for key in [10, 5, 20, 3, 7]:
        rbt.insert(key)
    print("Red-Black Tree (RBT):")
    print("In-order after insertions:", rbt.inorder_traversal())
    print("Search for 10:", rbt.search(10))
    print("Search for 15:", rbt.search(15))
    print("In-order after attempted deletion of 10 (not implemented):", rbt.inorder_traversal())
    print()

test_trees()

'''output'''
'''
Binary Search Tree (BST):
In-order after insertions: [3, 5, 7, 10, 20]
Search for 10: True
Search for 15: False
In-order after deletion of 10: [3, 5, 7, 20]

AVL Tree:
In-order after insertions: [3, 5, 7, 10, 20]
Search for 10: True
Search for 15: False
In-order after deletion of 10: [3, 5, 7, 20]

Red-Black Tree (RBT):
In-order after insertions: [3, 5, 7, 10, 20]
Search for 10: True
Search for 15: False
In-order after attempted deletion of 10 (not implemented): [3, 5, 7, 10, 20]'''
