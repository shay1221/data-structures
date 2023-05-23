#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value, children = None):

		self.key = key
		self.value = value
		self.left = children
		self.right = children
		self.parent = None
		if(not children == None):
			self.height = 0
			self.size = 1
		else:
			self.height = -1
			self.size = 0
	
	def __str__(self):
		s =  "key: " +  str(self.get_key() ) + "\n"  +"height: " + str(self.height) + "\n"   "size: " + str(self.size) + "\n" 
		return s

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		return self.size


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.size!=0
	
	def is_virtual(self):
		return self.size==0
	
	def is_leaf(self):
		return (self.left == None and self.right==None)
	
	""""
	@rtype: int
	@returns: BF := self.left.hight - self.right.hight
	"""
	def get_bf(self):
		if(self.get_left()==None and self.get_left()==None):
			return 0
		
		if(self.get_left()==None):
			return self.get_right().get_height()
		
		if(self.get_right()==None):
			return self.get_left().get_height()
		
		return self.get_left().get_height()-self.get_right().get_height()



"""
A class implementing an AVL tree.
"""

class AVLTree(object):
	
	virtual = AVLNode(-1,0)

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		# add your fields here
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root
	def set_root(self, node):
		self.root = node
		return
	def rec_search(self, node, key):
		if(node is self.virtual):
			return None
		elif(node.get_key() == key):
			return node
		if(key < node.get_key()):
			return self.rec_search(node.get_left(), key)
		else:
			return self.rec_search( node.get_right(), key)
	
	"""searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""
	def search(self, key):
		if(self.get_root() is None):
			return None
		return self.rec_search( self.get_root(), key)
		
	
	def compute_bf(self, node:AVLNode):
		return  node.get_left().get_height() - node.get_right().get_height()

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		res = 0
		#print(self.get_root())
		res += self.insert_bst(key, val)
		return res

	def insert_bst(self, key, val):
		balances = 0
		z = AVLNode(key, val, self.virtual)
		if(self.root is None):
			self.set_root(z)
			return 1
		y = None
		x = self.root
	
		while(x != None and not x is self.virtual):
			y = x
			if(z.get_key() < x.get_key()):
				x = x.get_left()
			else:
				x = x.get_right()
			z.set_parent(y)
		
		if(y == None):
			self.set_root(z)

				
		
		elif(z.get_key() < y.get_key()):
			y.set_left(z)
		else:
			y.set_right(z)
		h = y.get_height()
		
		balances += self.fix_height_after_insertion(z)
		h2 = y.get_height()
		
		while(y is not None):
			bf = self.compute_bf(y)
			if(abs(bf) < 2 and h == h2):
				return balances
			elif(abs(bf) < 2):
				y = y.get_parent()
			else:
				
				return balances + self.rotation(y)
		return balances
	
	def rotation(self, node : AVLNode):
		balances = 0
		bf = self.compute_bf(node)
		
		if(bf == 2):
			if(self.compute_bf(node.get_left()) == 1):
				#right rotation
				self.right_rotation(node)
				balances += 1
			else:
				#left then right
				node_left = node.get_left()
				self.left_rotation(node_left)
				self.right_rotation(node)
				balances += 2
		else:
			if(self.compute_bf(node.get_right()) == -1):	
				#left rotation
				self.left_rotation(node)
				balances += 1
			else:
				#right then left rotation
				node_right = node.get_right()
				self.right_rotation(node_right)
				self.left_rotation(node)
				balances += 2
		return balances

	
	def right_rotation(self, node):
		
		b = 0
		if(node.get_parent() is None):
			b+=2

		elif(node is node.get_parent().get_right()):
			b +=1
		a = node.get_left()
		ar_height_before = a.get_right().get_height()
		node.set_left(a.get_right())
		node.get_left().set_parent(node)
		a.set_right(node)
		a.set_parent(node.get_parent())

		if(b == 1):
			a.get_parent().set_right(a)
		elif(b==0):
			a.get_parent().set_left(a)
		else:
			self.set_root(a)
		node.set_parent(a)
		node.set_height(1 + max(ar_height_before, node.get_right().get_height()))
		a.set_height(1 + max(node.get_height(), a.get_left().get_height()))	
	def left_rotation(self, node):
		b = 0
		if(node.get_parent() is None):
			b+=2

		elif(node is node.get_parent().get_left()):
			b +=1
		a = node.get_right()
		ar_height_before = a.get_left().get_height()
		node.set_right(a.get_left())
		node.get_right().set_parent(node)
		a.set_left(node)
		a.set_parent(node.get_parent())

		if(b == 1):
			a.get_parent().set_left(a)
		elif(b==0):
			a.get_parent().set_right(a)
		else:
			self.set_root(a)
		node.set_parent(a)
		node.set_height(1 + max(ar_height_before, node.get_left().get_height()))
		a.set_height(1 + max(node.get_height(), a.get_right().get_height()))	
		
	#מקבל מצביע לצומת שהוספנו וברקורסיה מעדכן את הגבהים למעלה עד השורש(סופר פעולות עדכון גובה)
	def fix_height_after_insertion(self, node, changes = 0):
		#print(node)
		if(node.get_parent() is None):
			if(changes>=node.get_height()):
				node.set_height(changes)
				changes+=1
			return changes
			#if(1 + node.get_height() > node.get_height()):
			#	changes +=1
			#node.set_height(max(1 + node.get_height(), node.get_height()))
			#return changes
		if(1 + node.get_height() >= node.get_parent().get_height()):
			changes += 1
		node.get_parent().set_height(max(1 + node.get_height(), node.get_parent().get_height()))
		return self.fix_height_after_insertion(node.get_parent(), changes)
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete_bst(self, node : AVLNode):
		balances = 0
		node_parent = node.get_parent()
		#node is a leaf ;updating the height
		if(node.get_left() is self.virtual and node.get_right() is self.virtual):
			if(node is self.get_root()):
				self.set_root(None)
				return 0
			if(node is node_parent.get_right()):
				node_parent.set_right(self.virtual)
				node_parent.set_height(max(0, 1 + node_parent.get_left().get_height()))
				

			else:
				node_parent.set_left(self.virtual)
				node_parent.set_height(max(0, 1 + node_parent().right))
			#height changes before rotation
			balances += self.fix_height_after_insertion(node_parent, 1)
		#node had only right son	
#node had only right son
		else:
			if(node is node_parent.get_right()):
				
				node_parent.set_right(node.get_right())
				node.get_right().set_parent(node_parent)
			else:
				node_parent.set_left(node.get_right())
				node.get_right().set_parent(node_parent)
			#height changes before rotation
			node_parent.set_height(node_parent.get_height() - 1)
			balances += self.fix_height_after_insertion(node_parent, 1)
		return balances
	def delete(self, node):
		balances = 0 #the returned value
		node_parent = node.get_parent()
		pass_node = None
		h_before = -1
		h_after = -1
		#node is a leaf ;updating the height
		if(node.get_left() is self.virtual and node.get_right() is self.virtual):
			if(node is self.get_root()):
				self.set_root(None)
				return 0
			if(node is node_parent.get_right()):
				node_parent.set_right(self.virtual)
				node_parent.set_height(max(0, 1 + node_parent.get_left().get_height()))
				

			else:
				node_parent.set_left(self.virtual)
				node_parent.set_height(max(0, 1 + node_parent().get_right()))
			#height changes before rotation
			h_before = node_parent.get_height()
			balances += self.fix_height_after_insertion(node_parent, 1)
			h_after = node_parent.get_height()
			pass_node = node_parent
		#node had only right son
		elif(node.get_left() is self.virtual):
			if(node is node_parent.get_right()):
				
				node_parent.set_right(node.get_right())
				node.get_right().set_parent(node_parent)
			else:
				node_parent.set_left(node.get_right())
				node.get_right().set_parent(node_parent)
			#height changes before rotation
			node_parent.set_height(node_parent.get_height() - 1)
			h_before = node_parent.get_height()
			balances += self.fix_height_after_insertion(node_parent, 1)
			h_after = node_parent.get_height()
			pass_node = node_parent
		#node has only left son
		elif(node.get_right() is self.virtual):
			if(node is node_parent.get_left()):
				node_parent.set_left(node.get_left())
				node.get_left().set_parent(node_parent)
			else:
				node_parent.set_right(node.get_left())
				node.get_left().set_parent(node_parent)
			#height changes before rotation
			node_parent.set_height(node_parent.get_height - 1)
			h_before = node_parent.get_height()
			balances += self.fix_height_after_insertion(node_parent, 1)
			h_after = node_parent.get_height()
			pass_node = node_parent
		#node has 2 children
		else:
			y = self.successor(node)
			balances += self.delete_bst(y)
			#b = 0 - node is left son.b = 1 - node is right son.b = 2 - node is the root 
			b = 0
			if(node.get_parent() is None):
				b += 2
			elif(node is node.get_parent().get_right()):
				b += 1
			y.set_right(node.get_right())
			y.set_left(node.get_left())
			y.set_parent(node.get_parent())
			if(b == 0):
				node.get_parent().set_left(y)
			elif(b == 1):
				node.get_parent().set_right(y)
			else:
				self.set_root(y)
			node.get_right().set_parent(y)
			node.get_left().set_parent(y)
			#height changes before rotation
			y.set_height(1 + max(y.get_left().get_height(), y.get_right().get_height()))
			h_before = y.get_height()
			balances += self.fix_height_after_insertion(y, 1)
			h_after = y.get_height()
			pass_node = y
		balances += self.balancing_after_deletion(pass_node, h_after, h_before)
		return balances

	def balancing_after_deletion(self, node, h_after, h_before):
		changes = 0
		while(not node is None):
			bf = self.compute_bf(node)
			if(abs(bf) < 2 and h_after == h_before):
				return changes
			elif(abs(bf) < 2):
				node = node.get_parent()
			else:
				changes += self.drotation(node)
				node = node.get_parent()
		
		return changes
	def drotation(self, node):
		balances = 0
		bf = self.compute_bf(node)
		
		if(bf == 2):
			if(self.compute_bf(node.get_left()) == 1 or self.compute_bf(node.get_left()) == 0 ):
				#right rotation
				self.right_rotation(node)
				balances += 1
			else:
				#left then right
				node_left = node.get_left()
				self.left_rotation(node_left)
				self.right_rotation(node)
				balances += 2
		else:
			if(self.compute_bf(node.get_right()) == -1 or self.compute_bf(node.get_right()) == 0):	
				#left rotation
				self.left_rotation(node)
				balances += 1
			else:
				#right then left rotation
				node_right = node.get_right()
				self.right_rotation(node_right)
				self.left_rotation(node)
				balances += 2
		return balances

	def successor(self, node):
		if(node.get_right() is not self.virtual):
			y = node.get_right()
			x = None
			while(y is not self.virtual):
				x = y
				y = y.get_left()
			return x
		else:
			y = node.get_parent()
			x = node
			while(x is y.get_right() and y is not None):
				x = x.get_parent()
				y = y.get_parent()
			return y
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		res = []
		root = AVLNode(self.get_root)
		if(root.is_real_node):
			res=self.avl_to_array(root.get_left)
			res.append((root.get_key,root.get_value))
			res+=res+self.avl_to_array(root.get_right)
		return res

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		Tree = AVLTree(self)
		root = AVLNode(Tree.root)
		if(not root.is_real_node):
			return 0
		return(AVLTree.size(root.get_left)+AVLTree.size(root.get_right)+1)

	
	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None

	
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
	@returns: the absolute value of the difference between the height of the AVL trees joined +1
	"""
	def join(self, tree, key, val):
		return None


	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node):
		root = AVLNode(self.root)
		node = AVLNode(node)
		if(not node.is_real_node):
			return 0
		
		if(node.get_value<root.get_value):
			return(1+AVLTree.rank(root.get_right,node)+AVLTree.rank(root.get_left,node))
		else:
			return(AVLTree.rank(root.get_right,node)+AVLTree.rank(root.get_left,node))



	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		tree = AVLTree(self)
		a = tree.avl_to_array()
		return(a[i])


	
