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
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		self.is_virtual = False
		self.balanceFactor = 0
		

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
	
	"""returns the balance Factor of the Node.

	@rtype: int
	@returns: balance Factor of the Node.
	"""
	def get_bf(self):
		return self.balanceFactor

	"""sets key
	

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key=key


	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value=value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left=node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right=node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent=node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height=h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	def set_size(self, s):
		self.size=s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.is_virtual
	
	def is_leaf(self):
		return (self.left == None and self.right==None)
	"""owner: Shir
	computes the BF of a node

	@rtype: int
	@returns: BF := self.left.hight - self.right.hight
	"""
	def compute_BF(self):
		if(self.get_left()==None and self.get_left()==None):
			return 0
		
		if(self.get_left()==None):
			return self.get_right().get_height()
		
		if(self.get_right()==None):
			return self.get_left().get_height()
		
		return self.get_left().get_height()-self.get_right().get_height()
		#return AVLNode(self.get_left()).get_height() - AVLNode(self.get_right()).get_height()




"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.height = 1
		self.root = None
		# add your fields here



	def find_Height(root,Node):
		if(root==None):
			return -1
		height = -1
		lHeight = AVLTree.find_Height(root.get_left(),Node)
		rHeight = AVLTree.find_Height(root.get_right(),Node)
		ret = max(lHeight,rHeight)

		if(root.get_key()==Node.get_key()):
			height = ret
		
		return height
	

	def get_Height(self,Node):
		if Node == None:
			return -1
		height = AVLTree.find_Height(self.get_root(),Node)

		return height
	

	
	def get_BF(self,Node):
		return Node.compute_BF()
	"""searches for a value in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: any
	@returns: the value corresponding to key.
	"""
	def search(self, key):
		root = self.get_root()
		if root!=None:
			print(root.get_key())
		AVLTree.search_func(root,key)

	def search_func(root : AVLNode,key):
		if root==None:
			return None
		if(root.get_key()==key):
			return root
			
		if(root.get_right()==None and root.get_left()==None):
			return None
		elif(root.get_key()>key):
			if root.get_left()==None:
				return None
			else:
				return AVLTree.search_func(root.get_left(),key)
		else:
			if root.get_right()==None:
				return None
			else:
				return AVLTree.search_func(root.get_right(),key)

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	
	
	insert BTS and returns the parent and the height before insertion
	"""
	def naive_insert(root,key,val):
		if root!=None:
			if root.get_key()>key:
				if root.get_left() == None:
					root.set_left(AVLNode(key,val))
				else:
					AVLTree.naive_insert(root.get_left(),key,val)
			elif root.get_key()<key:
				if root.get_right == None:
					root.set_right(AVLNode(key,val))
					
				else:
					AVLTree.naive_insert(root.get_right(),key,val)




	
	def insert(self, key, val):
		root = self.get_root()
		ret = 0


		#inserting the node
		if root is None or not root.is_real_node:
			self.root = AVLNode(key,val)
			self.root.is_virtual = True
			#return AVLNode(key,val)
		
		else:
			AVLTree.naive_insert(root,key,val)
		root = self.get_root()
		print(root.get_key())
		#updating the height of the root
		root.set_height(max(self.get_Height(root.get_right()),self.get_Height(root.get_left()))+1)

		#now we update the BF of each node and than, if necessary, rotate the tree.
		l = root.get_left()
		r = root.get_right()
		BF = self.get_BF(root)
		
		if BF<=-2:
			if key>r.key:
				ret+=1
				self.left_rotate(root)
				return ret
			else:
				root.right = self.right_rotate(root.right)
				self.left_rotate(root)
				ret+=2
				return ret
		
		if BF>=2:
			if key<l.key:
				ret+=1
				self.right_rotate(root)
				return ret
			else:
				root.left = self.left_rotate(root.right)
				self.right_rotate(root)
				ret+=2
				return ret

		return ret

				
	
	def right_rotate(self,node):
		tree = AVLTree(self)
		node = AVLNode(node)
		r = AVLNode(node.left)
		tree1 = r.right
		r.right = node
		node.left = tree1
		
		node.height=1+max(tree.get_Height(node.left), tree.get_Height(node.right))
		r.height=1+max(tree.get_Height(r.left),tree.get_Height(r.right))
		
		return r
	
	def left_rotate(self,node):
		tree = AVLTree(self)
		node = AVLNode(node)
		r = AVLNode(node.right)
		tree1 = r.left
		r.left = node
		node.right = tree1
		
		node.height=1+max(tree.get_Height(node.left), tree.get_Height(node.right))
		r.height=1+max(tree.get_Height(r.left),tree.get_Height(r.right))
		
		return r
	
	"""
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: tuple AVLNode, int
	@returns: the parent of the inserted node and the height of it before insertion
	"""
	
	"""
	************************************************************************************8
	shir's code:
	
		def insert(self, key, val):
			tup = (self.naive_insert(key, val))[0]
			y = tup[0]
			prev_height = tup[1]
			while(y.is_real_node):
				bf = y.compute_BF()
				#if(abs(bf) < 2 and y.get_height = )

			return -1
	


		def naive_insert(self, key, val):
		y = None
		x = AVLNode(self.root)
		while(x.is_real_node):
			y = x
			if(key < x.get_key):
				x = AVLNode(x.get_right)
			else:
				x = AVLNode(x.get_left)
		z = AVLNode(key, val)
		height = y.get_height
		z.set_parent = y
		if(not y.is_real_node):
			self.root = z
		elif(key < y.get_key):
			y.set_left = z
		else:
			y.set_right = z
		return y, height
	
		*************************************************************************************
	"""

	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, Node):
		if Node!=None:
			return(self.delete_func(self.get_root(),Node.key))



	def delete_func(self,root,key):
		Tree = AVLTree(self)
		root = AVLNode(root)
		ret = 0
		if not root.is_real_node or root == None:
			return ret
		elif key<root.key:
			root.left = Tree.delete(root.left,key)
			ret+=1
		elif key>root.key:
			root.right = Tree.delete(root.right,key)
			ret+=1
		else:
			if not AVLNode(root.right).is_real_node:
				a = root.left
				root = None
				ret +=1
				return ret
			elif not AVLNode(root.left).is_real_node:
				a = root.right
				root = None
				ret +=1
				return ret
			a = AVLNode(Tree.getMin(root.right))
			root.key = a.key
			ret +=1
			root.right = self.delete(root.right,a.key)

		
		if(not root.is_real_node):
			return ret

			
		

		root.height = max(Tree.get_Height(root.right),Tree.get_Height(root.left))+1
		BF = Tree.get_BF(root)


		#keep the tree balance:
		if BF<-1:
			if Tree.get_BF(root.right)<=0:
				Tree.left_rotate(root)
				ret+=1
				return ret
			else:
				root.right = self.right_rotate(root.right)
				Tree.left_rotate(root)
				ret+=2
				return ret
		if BF>1:
			if Tree.get_BF(root.left)<0:
				root.left = Tree.left_rotate(root.left)
				Tree.right_rotate(root.left)
				ret+=2
				return ret
			else:
				Tree.right_rotate(root)
				ret+=1
				return ret
		

		return ret


	"""performing left and right rotations

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: AVLNode
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	
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
	@returns: the absolute value of the difference between the height of the AVL trees joined
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


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		if(self!=None):
			return self.root
		return None
