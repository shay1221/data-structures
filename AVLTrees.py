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
	def __init__(self, key, value, isReal = False):

		self.key = key
		self.value = value
		self.parent = None
		if(isReal):
			self.height = 0
			self.size = 1
			self.right = AVLNode(None,None,False)
			self.left = AVLNode(None,None,False)
			self.right.set_parent(self)
			self.left.set_parent(self)
		else:
			self.left = None
			self.right = None
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
		if self.is_real_node():
			return self.key
		return None

	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		if self.is_real_node():
			return self.value
		return None


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
		if self.parent != None:
			return self.parent
		return None


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		if self.is_real_node():
			return self.height
		return -1

	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	def get_size(self):
		if self.is_real_node():
			return self.size
		return 0


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
		self.size = s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if (self is None): return False
		return self.size!=0 or self.height != -1
	
	def is_leaf(self):
		return (self.height==0)

	def NodeUpdating(self):
		self.set_height(1+max(self.left.height,self.right.height))
		self.set_size(self.get_left().get_size()+self.get_right().get_size() + 1)

		if self.get_parent() is not None:
			self.parent.NodeUpdating()
	""""
	@rtype: int
	@returns: BF := self.left.hight - self.right.hight
	"""
	def get_bf(self):
		return self.left.height-self.right.height


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
		self.max_node = self.virtual
		# add your fields here
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def Tree_Height(self):
		root = self.get_root()
		if root is None:
			return 0
	
		else:
	
			# Compute the depth of each subtree
			lDepth = AVLTree.Tree_Height(root.get_left())
			rDepth = AVLTree.Tree_Height(root.get_right())
	
			# Use the larger one
			if (lDepth > rDepth):
				return lDepth+1
			else:
				return rDepth+1
	


	def get_Height(Node : AVLNode):
		if Node == None:
			return -1
		if not Node.is_real_node:
			return -1
		return Node.height
	
	def get_root(self):
		return self.root
	

	def set_root(self, node):
		self.root = node
		return
	
	def size_of_node(self, node : AVLNode):
		if(not node.is_real_node):
			return node.size
		else:
			return -1
	

	def rec_search(self, node : AVLNode, key):
		if (node is None or not node.is_real_node()):
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
		return self.rec_search( self.get_root(), key)
		
	
	def compute_bf(self, node : AVLNode):
		return  node.left.height - node.right.height

	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val, max = False):
		z = AVLNode(key, val, True)
		if(self.root is None or not self.root.is_real_node()):
			self.root = z
			self.root.height = 0
			self.root.size = 1
			self.max_node = self.get_root()
			return 0
		
		if max:
			node = self.max_node
			while True:
				if not node.get_parent() is None and node.parent.get_key()> key:
						node = node.get_parent()
				else:
					break
				
		else:
			node = self.root
		
		while True:
			assert key != node.key
			if node.get_key() < key:
				if node.right.is_real_node():
					node = node.right
				else:
					node.right = z
					if key>self.max_node.get_key():
						self.max_node = node.right
					node.right.parent = node
					node.right.size = 1
					node.right.size = 0
					node.NodeUpdating()
					node = node.right
					break
			else: #node.get_key() > key
				if key<node.key:
					if node.left.is_real_node():
						node = node.left
					else:
						node.set_left(z)
						node.get_left().set_parent(node)
						node.left.size = 1
						node.left.height = 0
						node = node.left
						break

		if key > self.max_node.get_key():
			self.max_node = node
		
		last_node = node
		ret = 0
		while(not node.parent is None):
			node = node.parent
			node.NodeUpdating()
			i, node = self.fix_height_after_insertion(node)
			ret += i
		
		last_node.NodeUpdating()
		return ret


	
	def right_rotation(self, node : AVLNode):
		
		n = node.left
		p = node.parent
		n.right , node.left = node, n.right
		if n.right:
			n.right.parent = node
		else:
			pass
		if n.left:
			node.left.parent = node
		n.parent = p
		node.parent = n

		
		n.height = (1+max(AVLTree.get_Height(n.left),AVLTree.get_Height(n.right)))
		node.height = (1+max(AVLTree.get_Height(node.left),AVLTree.get_Height(node.right)))
		node.size = (1+AVLTree.size_of_node(node.left) + AVLTree.size_of_node(node.right) )
		n.size = (1+AVLTree.size_of_node(n.left)  + AVLTree.size_of_node(n.right) )
		
		if p is None:
			self.root = n
		elif p.key>n.key:
			p.left = n
		else:
			p.right = n
		
		return n


	def left_rotation(self, node):
		n = node.right
		p = node.right
		n.left , node.right = node, n.left
		if n.left:
			n.left.parent = n
		if n.right:
			node.right.parent = node
		
		
		n.parent = p
		node.parent = n

		
		n.height = (1+max(AVLTree.get_Height(n.left),AVLTree.get_Height(n.right)))
		node.height = (1+max(AVLTree.get_Height(node.left),AVLTree.get_Height(node.right)))
		node.size = (1+AVLTree.size_of_node(node.left) + AVLTree.size_of_node(node.right) )
		n.size = (1+AVLTree.size_of_node(n.left)  + AVLTree.size_of_node(n.right) )
		
		if p is None:
			self.root = n
		elif p.key>n.key:
			p.left = n
		else:
			p.right = n
		
		return n
	#מקבל מצביע לצומת שהוספנו וברקורסיה מעדכן את הגבהים למעלה עד השורש(סופר פעולות עדכון גובה)
	def fix_height_after_insertion(self, node : AVLNode, changes = 0):
		changes = 0
		if AVLTree.get_Height(node.left) - AVLTree.get_Height(node.right)>1:
			if AVLTree.get_Height(node.left.right)> AVLTree.get_Height(node.left.left):
				self.left_rotation(node.left)
				changes +=1
			return changes + 1, self.right_rotation(node)
		elif AVLTree.get_Height(node.left) - AVLTree.get_Height(node.right)<-1:
			if AVLTree.get_Height(node.right.left)>AVLTree.get_Height(node.right.right):
				self.right_rotation(node.right)
				changes +=1
			return changes, self.left_rotation(node)
		return changes,node
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete_bst(self, node : AVLNode):
		#node is a leaf ;updating the height
		if(not node.left.is_real_node() and not node.right.is_real_node()):
			if(node.parent is None): #root
				self.root = None
			else:
				if node.parent.key > node.key:
					node.parent.left = node.right
					node.right.parent = node.parent
				else:
					node.parent.right = node.right
					node.right.parent = node.parent
				
		
		
		#node has only right son
		elif node.right.is_real_node() and not node.left.is_real_node():
			print("right son: ", node.key)
			if(node.parent is None): #root
				self.root = node.right
				self.root.parent = None 
			elif node.parent.key>node.key:
				node.parent.left = node.right
				node.right.parent = node.parent
			else:
				node.parent.right = node.right
				node.right.parent = node.parent
			

		
		
		#node has only left son
		elif node.left.is_real_node() and not node.right.is_real_node():
			if node.parent is None: #root 
				self.root = node.left
				self.root.parent = None
			elif node.parent.key > node.key:
				node.parent.left = node.left
				node.left.paernt = node.parent
			else:
				node.parent.right = node.left
				node.left.paernt = node.parent
			
			
		

		#node has 2 sons
		else:  #node.right.is_real_node() and node.left.is_real_node()
			max_after = self.successor(node)
			if node.parent is not None:
				if node.parent.key == max_after.key:
					node , max_after = max_after, node
			else:
				self.root = max_after
			if node.left.key== max_after.key:
				node_right = node.parent is not None and node.parent.right.key == node.key
				node.size, max_after.size = max_after.size , node.size
				node.height, max_after.height= max_after.height, node.height
				r = node.left.right
				l = node.left.left
				node.right.parent = max_after
				node.left.left = node
				node.left.right = node.right
				node.right = r
				node.left = l
				r.parent = node
				l.parent = node
				if(max_after.parent != None):
					if node_right:
						max_after.parent.right = max_after
					else:
						max_after.parent.left = max_after
                        
			
			elif node.right.key == max_after.key: #right son
				node_right = node.parent is not None and node.parent.right.key == node.key
				node.size, max_after.size = max_after.size , node.size
				node.height, max_after.height= max_after.height, node.height
				r = node.right.right
				l = node.right.left
				node.left.parent = max_after
				node.right.right = node
				node.right.left = node.left
				node.right.parent = node.parent
				node.parent = node.right
				node.right = r
				node.left = l
				r.parent = node
				l.parent = node
				if(max_after.parent != None):
					if node_right:
						max_after.parent.right = max_after
					else:
						max_after.parent.left = max_after
			
			else:
				if(max_after.parent != None):
					max_right = max_after.parent.right.key == max_after.key
				else:
					max_right = False
				if(node.parent != None):
					node_right = node.parent.right.key == node.key
				else:
					node_right = False
                
				    
				node.right , max_after.right = max_after.right, node.right
				node.left , max_after.left = max_after.left, node.left
				node.parent, max_after.parent = max_after.parent, node.parent
				node.right.parent = node
				node.left.parent = node
				max_after.right.parent = max_after
				max_after.left.parent = max_after
				max_after.size , node.size = node.size,  max_after.size 
				max_after.height , node.height = node.height,  max_after.height 
				if node.parent != None:
					if max_right:
						node.parent.right = node
					else:
						node.parent.left = node
				if max_after != None:
					if node_right:
						max_after.parent.right = node
					else:
						max_after.parent.left = node
				
				
				
			self.delete_bst(node)
			return max_after
		
		return node


	def delete(self, node : AVLNode):
		balances = 0 #the returned value
		node = self.delete_bst(node)

		while node.parent != None and node.parent.is_real_node():
			node = node.parent
			node.NodeUpdating()
			i, node = self.fix_height_after_insertion(node)
			balances += i
		

		if node.get_key() == self.max_node.get_key():
			cur_max = self.root
			while cur_max.get_right().is_real_node():
				cur_max = cur_max.get_right()
			self.max_node = cur_max
		if node.parent is not None and node.parent.is_real_node():
			if node.parent.left.is_real_node():
				node.parent.left.NodeUpdating()
			if node.parent.right.is_real_node():
				node.right.right.NodeUpdating()
			node.parent.NodeUpdating()
		
		return balances

	def leftMostNode(node : AVLNode):
		while node.is_real_node() and node.left.is_real_node:
			node = node.left
		return node
	
	def rightMostNode(node : AVLNode):
		while node.is_real_node() and node.right.is_real_node:
			node = node.right
		return node

	def findInorderRecursive(root : AVLNode, node: AVLNode):
		if not root.is_real_node():
			return None
		
		if(root.key == node.key or AVLTree.findInorderRecursive(root.left,node) or AVLTree.findInorderRecursive(root.left,node)):
			temp = AVLTree.findInorderRecursive(root.right,node)
		else:
			temp = AVLTree.findInorderRecursive(root.left,node)
		if(temp != None and temp.is_real_node()):
			if(root.left.key == temp.key):
				ret = root.data
			return ret
		return root
	

	def successor(self,node : AVLNode):
		if(node.right.is_real_node()):
			y = node.right
			x = None
			while(y.is_real_node()):
				x = y
				y = y.left
			return x
		else:
			y = node.parent
			x = node
			while(y is not None and x is y.right):
				x = x.parent
				y = y.parent
			return y
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def MakeArray(self, Node : AVLNode):
		res = []
		if(not Node is self.virtual and Node!=None):
			res = self.MakeArray(Node.get_left())
			res.append((Node.get_key(),Node.get_value()))
			res += self.MakeArray(Node.get_right())
			print("res: ", res)
		return res
	

	def avl_to_array(self):
		root = self.get_root()
		return(self.MakeArray(root))
	
	
	
    


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.get_root().get_size()

	
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
		x = AVLNode(key,val,True)
		root1 = self.get_root()

		if root1.get_key()<key:
			T1 = self
			T2 = tree
		else:
			T1 = tree
			T2 = self
		
		root1 = T1.get_root()
		root2 = T2.get_root()
		

		if(abs(T1.Tree_Height()-T2.Tree_Height()) <= 1):
			new_tree = AVLTree()
			new_tree.set_root(x)
			new_root = new_tree.get_root()
			root1.set_parent(new_root)
			root2.set_parent(new_root)
			new_root.set_right(root1)
			new_root.set_left(root2)
			return new_tree.find_Height()-self.find_Height()+1
		

		else:
			ret = T1.Tree_Height()-T2.Tree_Height()+1
			if(T1.Tree_Height()>T2.Tree_Height()):
				T3 = AVLTree()
				b = T1.find_Node(T2.Tree_Height())
				c = T1.find_Node(T2.Tree_Height())

				c.set_right(x)
				x.set_parent(c)
				x.set_right(T2.get_root())
				(T2.get_root()).set_parent(x)
				x.set_left(b)
				b.set_parent(x)
				T3.set_root(T1.get_root())
			

			else:
				T3 = AVLTree()
				b = T2.find_Node(T1.Tree_Height())
				c = T2.find_Node(T1.Tree_Height())
				
				c.set_left(x)
				x.set_parent(c)
				x.set_left(T1.get_root())
				(T1.get_root()).set_parent(x)
				x.set_right(b)
				b.set_parent(x)
				T3.set_root(T2.get_root())


				

		return ret



	def find_Node(self,i):
		root = self.get_root()
		height = self.find_Height(root)

		while(height != i):
			if(root.get_left() != AVLTree.virtual):
				root = root.get_right()
			else:
				root = root.get_left()

			height = self.find_Height(root)
		return root
		



	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	def rank(self, node : AVLNode):
		root = self.root
		if(not node.is_real_node):
			return 0
		
		if(node.get_value<root.get_value()):
			return(1+AVLTree.rank(root.get_right(),node)+AVLTree.rank(root.get_left(),node))
		else:
			return(AVLTree.rank(root.get_right(),node)+AVLTree.rank(root.get_left(),node))



	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	def select(self, i):
		a = self.avl_to_array()
		return(a[i])


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		if(self!=None):
			return self.root
		return None

	
