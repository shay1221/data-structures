# username - galchapman
# id1      - 326163987
# name1    - Gal Chapman
# id2      - 325970838
# name2    - Erel Barzilay
from __future__ import annotations
from typing import Literal

"""A class representing a node in an AVL tree"""

VIRTUAL_NODE = None


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    @param virtual: is the node virtual
    """

    key: int | None
    value: object
    left: AVLNode | None
    right: AVLNode | None
    parent: AVLNode | None
    height: int
    size: int

    def __init__(self, key, value):  # O(1)
        self.key = key
        self.value = value
        self.height = 0
        self.size = 1
        self.parent = None
        self.left = VIRTUAL_NODE
        self.right = VIRTUAL_NODE

    def __repr__(self) -> str:  # O(1)
        if self.is_real_node():
            return f'AVLNode(k={self.key}, v={self.value}, h={self.height}, s={self.size})'
        return 'AVLNode(Virtual)'
    def get_bf(self):
        return self.left.height-self.right.height
    def get_key(self):  # O(1)
        """returns the key

        @rtype: int or None
        @returns: the key of self, None if the node is virtual
        """
        return self.key

    def get_value(self):  # O(1)
        """returns the value

        @rtype: any
        @returns: the value of self, None if the node is virtual
        """
        return self.value

    def get_left(self):  # O(1)
        """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child (if self is virtual)
        """
        return self.left

    def get_right(self):  # O(1)
        """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child (if self is virtual)
        """
        return self.right

    def get_parent(self):  # O(1)
        """returns the parent

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        return self.parent

    def get_height(self):  # O(1)
        """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        return self.height

    def get_size(self):  # O(1)
        """returns the size of the subtree

        @rtype: int
        @returns: the size of the subtree of self, 0 if the node is virtual
        """
        return self.size

    def set_key(self, key):  # O(1)
        """sets key

        @type key: int or None
        @param key: key
        """
        assert not self.is_real_node()
        self.key = key

    def set_value(self, value):  # O(1)
        """sets value

        @type value: any
        @param value: data
        """
        self.value = value

    def set_left(self, node):  # O(1)
        """sets left child

        @type node: AVLNode
        @param node: a node
        """
        self.left = node

    def set_right(self, node):  # O(1)
        """sets right child

        @type node: AVLNode
        @param node: a node
        """
        self.right = node

    def set_parent(self, node):  # O(1)
        """sets parent

        @type node: AVLNode
        @param node: a node
        """
        self.parent = node

    def set_height(self, h):  # O(1)
        """sets the height of the node

        @type h: int
        @param h: the height
        """
        self.height = h

    def set_size(self, s):  # O(1)
        """sets the size of node

        @type s: int
        @param s: the size
        """
        if not self.get_size() == 0:
            self.size = s

    def is_real_node(self):  # O(1)
        """returns whether self is not a virtual node

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        var = self.size == 0 or self.height == -1
        return not var

    def avl_to_arr_node(self, lst):  # O(size(self))
        # gets a list, fills the list with the derived array from the AVL tree which self is its root
        if self.is_real_node():
            self.get_left().avl_to_arr_node(lst) #add all smaller
            lst.append((self.get_key(), self.get_value()))
            self.get_right().avl_to_arr_node(lst) #add all higher

    def update(self):  # O(log n)
        """
        updates the attributes in the path to the root of the tree from the node
        """

        self.set_size(self.get_left().get_size() + self.get_right().get_size() + 1)
        self.set_height(max(self.get_left().get_height(), self.get_right().get_height()) + 1)
        if self.parent is not None and self.parent is not VIRTUAL_NODE:
            self.get_parent().update() #update the parent

    def select_node(self, size):  # O(log n)
        if self.get_left().get_size() == size:
            return self

        if self.get_left().get_size() < size: #if the exp. size is higher go right
            return self.get_right().select_node(size - self.get_left().get_size()-1)

        return self.get_left().select_node(size) #go left




VIRTUAL_NODE = AVLNode(0, 0)
VIRTUAL_NODE.set_size(0)
VIRTUAL_NODE.set_height(-1)


def _height(node: AVLNode | None):  # O(1)
    return -1 if not node.is_real_node() else node.height


def _size(node: AVLNode | None):  # O(1)
    return 0 if not node.is_real_node() else node.size


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    root: AVLNode | None
    max_node: AVLNode | None

    def __init__(self):  # O(1)
        self.root = VIRTUAL_NODE
        self.max_node = VIRTUAL_NODE

    # add your fields here

    def search(self, key):  # O(log n)
        """searches for a node in the dictionary corresponding to the key

        @type key: int
        @param key: a key to be searched
        @rtype: AVLNode
        @returns: node corresponding to key. If there is none, return None
        """
        curr_node = self.root
        while curr_node.is_real_node():
            if curr_node.get_key() < key: #if smaller than current key go right
                curr_node = curr_node.get_right()
            elif curr_node.get_key() > key: #if higher go left
                curr_node = curr_node.get_left()
            else:
                return curr_node
        return None

    def _rotate(self, node: AVLNode, direction: Literal['left', 'right']) -> AVLNode:
        new_node = node.right if direction == 'left' else node.left
        # Swap relationship
        parent = node.parent
        if direction == 'left':
            new_node.left, node.right = node, new_node.left
            if new_node.left:
                new_node.left.parent = new_node
            if node.right:
                node.right.parent = node
        else:
            new_node.right, node.left = node, new_node.right
            if not new_node.right:
                pass
            else:
                new_node.right.parent = new_node
            if node.left:
                node.left.parent = node
        new_node.parent = parent
        node.parent = new_node
        # Fix heights
        node.height = 1 + max(_height(node.left), _height(node.right))
        new_node.height = 1 + max(_height(new_node.left), _height(new_node.right))
        # Fix sizes
        node.size = 1 + _size(node.left) + _size(node.right)
        new_node.size = 1 + _size(new_node.left) + _size(new_node.right)
        if parent is None:
            self.root = new_node
        elif parent.key > new_node.key:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node

    def _balance(self, node: AVLNode) -> tuple[int, AVLNode]:
        rotations = 0
        if _height(node.left) - _height(node.right) > 1:
            if _height(node.left.right) > _height(node.left.left):
                self._rotate(node.left, 'left')
                rotations += 1
            return rotations + 1, self._rotate(node, 'right')
        elif _height(node.left) - _height(node.right) < -1:
            if _height(node.right.left) > _height(node.right.right):
                self._rotate(node.right, 'right')
                rotations += 1
            return rotations, self._rotate(node, 'left')
        return rotations, node

    def insert(self, key: int, val, max_search=False):
        """inserts val at position i in the dictionary
        @param max_search: true if the search should be conducted as in a (maximum) finger tree
        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        if self.root is VIRTUAL_NODE:
            self.root = AVLNode(key, val)
            self.max_node = self.get_root()
            self.root.height = 0
            self.root.size = 1
            return 0
        if not max_search:
            node = self.root
        else:
            node = self.max_node
            while True:
                if node.get_parent() is not None and node.parent.key > key:
                    node = node.get_parent()
                else:
                    break
        while True:
            assert key != node.key
            if key < node.key:
                if node.left.is_real_node():
                    node = node.left
                else:
                    node.set_left(AVLNode(key, val))
                    node.get_left().set_parent(node)
                    node.left.size = 1
                    node.left.height = 0
                    node.update()
                    node = node.left
                    break
            else:
                if node.right.is_real_node():
                    node = node.right
                else:
                    node.right = AVLNode(key, val)
                    if key > self.max_node.get_key():
                        self.max_node = node.right
                    node.right.parent = node
                    node.right.size = 1
                    node.right.height = 0
                    node.update()
                    node = node.right
                    break
        if key > self.max_node.get_key():
            self.max_node = node
        balances_count = 0
        save_node = node
        while node.parent is not None:
            node = node.parent
            node.size += 1
            node.height = 1 + max(_height(node.left), _height(node.right))
            acted, node = self._balance(node)
            balances_count += acted
        save_node.update()
        return balances_count

    @staticmethod
    def _successor(node: AVLNode, key) -> AVLNode | None:
        if not node.is_real_node():
            return None

        if node.key > key:
            if not node.left.is_real_node():
                return node
            return AVLTree._successor(node.left, key)
        if node.right.is_real_node() and node.right.key > key:
            return AVLTree._successor(node.right, key)
        if node.parent is not None:
            return AVLTree._successor(node.parent, key)

        return node

    def _bst_delete(self, node: AVLNode) -> AVLNode:
        if not node.left.is_real_node():
            if node.parent is None:
                if node.right.is_real_node():
                    self.root = node.right
                    self.root.parent = None
                else:
                    self.root = None
            elif node.parent.key > node.key:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            if node.right.is_real_node():
                node.right.parent = node.parent
        elif not node.right.is_real_node():
            if node.parent is None:
                if node.left.is_real_node():
                    self.root = node.left
                    self.root.parent = None
                else:
                    self.root = None
            elif node.parent.key > node.key:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
        else:
            suc = AVLTree._successor(node, node.key)
            self._bst_delete(suc)
            node.key = suc.key
            node.value = suc.value
            return suc
        return node

    def delete(self, node) -> int:
        """deletes node from the dictionary

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        node = self._bst_delete(node)

        balances = 0
        while node.parent:
            node = node.parent
            node.size -= 1
            node.height = 1 + max(_height(node.left), _height(node.right))
            acted, node = self._balance(node)
            balances += acted
        if node.get_key() == self.max_node.get_key():
            cur_max = self.root
            while cur_max.get_right().is_real_node():
                cur_max = cur_max.get_right()
            self.max_node = cur_max
        if node.parent is not None and node.parent is not VIRTUAL_NODE:
            if node.parent.left is not None:
                node.parent.left.update()
            if node.parent.right is not None:
                node.parent.right.update()
            node.parent.update()
        return balances

    def avl_to_array(self):  # O(n)
        """returns an array representing dictionary

        @rtype: list
        @returns: a sorted list according to key of touples (key, value) representing the data structure
        """
        lst = []
        node = self.root
        node.avl_to_arr_node(lst) #call the relevant node func
        return lst

    def size(self):
        """returns the number of items in dictionary

        @rtype: int
        @returns: the number of items in dictionary
        """
        return self.get_root().get_size()

    def split(self, node: AVLNode) -> tuple[AVLTree, AVLTree, int, int]:  # should delete the ints
        """splits the dictionary at a given node

        @type node: AVLNode
        @pre: node is in self
        @param node: The intended node in the dictionary according to whom we split
        @rtype: list
        @returns: a list [left, right], where left is an AVLTree representing the keys in the
        dictionary smaller than node.key, right is an AVLTree representing the keys in the
        dictionary larger than node.key.
        """
        self.root = None
        left = AVLTree()
        right = AVLTree()
        left.root = node.left
        right.root = node.right
        if node.left:
            node.left.parent = None
        if node.right:
            node.right.parent = None
        while node.parent:
            key = node.key
            node = node.parent

            if key > node.key:
                temp = AVLTree()
                temp.root = node.left
                temp.root.parent = None
                left.join(temp, node.key, node.value)

            else:
                temp = AVLTree()
                temp.root = node.right
                temp.root.parent = None
                right.join(temp, node.key, node.value)

        return left, right

    def join(self, tree, key, val):
        """joins self with key and another AVLTree

        @type tree: AVLTree
        @param tree: a dictionary to be joined with self
        @type key: int
        @param key: The key separting self with tree
        @type val: any
        @param val: The value attached to key
        @pre: all keys in self are smaller than key and all keys in tree are larger than key,
        or the other way around.
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        if (self.max_node is None and tree.max_node is not None) or (tree.max_node.get_key() > self.max_node.get_key()):
            self.max_node = tree.max_node
        bf = abs(_height(self.root) - _height(tree.root))
        if bf <= 1:  # Simple solution
            root = self.root
            self.root = AVLNode(key, val)
            if root is not None:
                if root.key < key:
                    self.root.left = root
                else:
                    self.root.right = root
                root.parent = self.root
            if tree.root is not None:
                if tree.root.key < key:
                    self.root.left = tree.root
                else:
                    self.root.right = tree.root
                tree.root.parent = self.root
            self.root.size = _size(self.root.left) + 1 + _size(self.root.right)
            self.root.height = 1 + max(_height(self.root.left), _height(self.root.right))
        else:

            # More complicated solution
            r1, r2 = self.root, tree.root
            if r1.height < r2.height:
                r1, r2 = r2, r1
                self.root = r1
            node = r1
            for _ in range(bf - 1):
                if r1.key < r2.key:
                    node = node.right
                else:
                    node = node.left

            x = AVLNode(key, val)

            x.height = 1 + r2.height
            x.size = 1 + r2.size + _size(node.right if r1.key < r2.key else node.left)
            x.parent = node

            if r1.key > r2.key:
                x.left = r2
                x.right = node.left
                node.left = x
            else:
                x.right = r2
                x.left = node.right
                node.right = x

            if x.right:
                x.right.parent = x
            if x.left:
                x.left.parent = x

            while node:
                node.size += r2.size + 1
                node.height = 1 + max(_height(node.left), _height(node.right))
                _, node = self._balance(node)
                node = node.parent

        tree.root = None
        return bf + 1

    def rank(self, node) -> int:  # complexity: O(logn)
        """compute the rank of node in the self

        @type node: AVLNode
        @pre: node is in self
        @param node: a node in the dictionary which we want to compute its rank
        @rtype: int
        @returns: the rank of node in self
        """
        assert node is not VIRTUAL_NODE and node is not None
        rank = node.left.size
        while node is not self.root:
            node_2 = node.parent
            if node is node_2.get_right(): #if the node is the result of going right
                rank = rank + node_2.get_left().get_size() + 1 #add the size of the parent.left + 1
            node = node_2 #go to the parent
        return rank + 1

    def select(self, i) -> AVLNode | None:  # O(log n)
        """finds the i'th smallest item (according to keys) in self
        @type i: int
        @pre: 1 <= i <= self.size()
        @param i: the rank to be selected in self
        @rtype: int
        @returns: the item of rank i in self
        """
        curr_node = self.get_root()
        return curr_node.select_node(i - 1) #select in node function

    def get_root(self) -> AVLNode:  # O(1)
        """returns the root of the tree representing the dictionary

        @rtype: AVLNode
        @returns: the root, None if the dictionary is empty
        """
        return self.root
