#username - shayklein
#id1      - 329453732
#name1    - shay klein
#id2      - 328374095
#name2    - shir arikha



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""
	#O(1)
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
	

	"""returns a string reprsnting the node

	@rtype: string
	@returns: returns a string reprsnting the nod
	"""
	#O(1)
	def __str__(self):
		s =  "key: " +  str(self.get_key() ) + "\n"  +"height: " + str(self.height) + "\n"   "size: " + str(self.size) + "\n" 
		return s

	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	#O(1)
	def get_key(self):
		if self.is_real_node():
			return self.key
		return None

	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	#O(1)
	def get_value(self):
		if self.is_real_node():
			return self.value
		return None


	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	#O(1)
	def get_left(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	#O(1)
	def get_right(self):
		return self.right


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	#O(1)
	def get_parent(self):
		if self.parent != None:
			return self.parent
		return None


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	#O(1)
	def get_height(self):
		if self.is_real_node():
			return self.height
		return -1

	"""returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""
	#O(1)
	def get_size(self):
		if self.is_real_node():
			return self.size
		return 0


	"""sets key

	@type key: int or None
	@param key: key
	"""
	#O(1)
	def set_key(self, key):
		self.key = key


	"""sets value

	@type value: any
	@param value: data
	"""
	#O(1)
	def set_value(self, value):
		self.value = value


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	#O(1)
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	#O(1)
	def set_right(self, node):
		self.right = node


	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	#O(1)
	def set_parent(self, node):
		self.parent = node


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	#O(1)
	def set_height(self, h):
		self.height = h


	"""sets the size of node

	@type s: int
	@param s: the size
	"""
	#O(1)
	def set_size(self, s):
		self.size = s


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	#O(1)
	def is_real_node(self):
		if (self is None): return False
		return self.size!=0 or self.height != -1
	"""@rtype: bool
	@returns: False if self is not a laef, True otherwise.
	"""
	#O(1)
	def is_leaf(self):
		return (self.height==0)
	"""updating the size and height of a node

	@rtype: None
	"""
	#O(log(n))
	def NodeUpdating(self, up = True):
		self.set_height(1+max(self.left.height,self.right.height))
		self.set_size(self.get_left().get_size()+self.get_right().get_size() + 1)
		if up:
			if self.get_parent() is not None:
				self.parent.NodeUpdating()
	""""
	@rtype: int
	@returns: BF := self.left.hight - self.right.hight
	"""
	#O(1)
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
	#O(1)
	def __init__(self):
		self.root = None
		self.max_node = self.virtual
		# add your fields here
	"""returns the height of thr tree representing the dictionary

	@rtype: int
	@returns: the height of thr tree representing the dictionary
	"""
	#O(1)
	def Tree_Height(self):
		return self.get_root().get_height()
		

	"""returns the height of node

	@rtype: int
	@returns: the hright -1 if virtual
	"""
	#O(1)
	def get_Height(Node : AVLNode):
		if Node == None:
			return -1
		if not Node.is_real_node:
			return -1
		return Node.height
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	#O(1)
	def get_root(self):
		return self.root
	
	"""sets the root of the tree representing the dictionary

	@rtype: none
	@pre:self.gett_root == node
	"""
	#O(1)
	def set_root(self, node):
		self.root = node
		return
	"""returns the size of node

	@rtype: int
	@returns: the size of node
	"""
	#O(1)
	def size_of_node(self, node : AVLNode):
		if(not node.is_real_node()):
			return node.size
		else:
			return -1
	
	#O(log(n))
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
	#O(log(n))
	def search(self, key):
		return self.rec_search( self.get_root(), key)
		
	#O(1)
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
	#O(log(n))
	def insert(self, key, val):
		ret = 0
		z = AVLNode(key, val, True)
		t =  self.insert_bst(z) 
		ret += t[0]
		height_changed = t[1] 
		y = z.get_parent()
		while(y is not None):
			bf = y.get_left().get_height() -  y.get_right().get_height()
			if(abs(bf)<2 and not height_changed):
				return ret
			elif(abs(bf)<2):
				y = y.get_parent()
			else:
				
				return ret + self.rotate(y)
			
	
	def rotate(self, node):
		ret = 0
		bf = node.get_left().get_height() - node.get_right().get_height()
		if(bf == 2):
			
			#b = AVLNode.get_Height(node.get_left().get_left()) - AVLNode.get_Height(node.get_left().get_right())
			b = self.compute_bf(node.get_left())
			if(b == 1):
				self.right_rotation(node)
				ret += 1
			else:
				self.left_rotation(node.get_left())
				self.right_rotation(node)
				ret += 2

		else:
			#b = AVLNode.get_Height(node.get_right().get_left()) - AVLNode.get_Height(node.get_right().get_right())
			b = self.compute_bf(node.get_right())
			if(b == 1):
				self.right_rotation(node.get_right())
				self.left_rotation(node)
				ret += 2
			else:
				self.left_rotation(node)
				ret += 1
		return ret
	def insert_bst(self, node):
		node_copy = node
		ret = 0
		if(self.get_root() is None):
			self.set_root(node)
			return ret, False
		y = None
		x = self.get_root()
		while(x.is_real_node() and x is not None):
			y = x
			if(node.get_key() < x.get_key()):
				x = x.get_left()
			else:
				x = x.get_right()
		node.set_parent(y)
		if(y is None):
			self.set_root(node)
		elif(node.get_key() < y.get_key()):
			y.set_left(node)
		else:
			y.set_right(node)

		y = node.get_parent()
		x = y
		h1 = y.get_height()
		while(y is not None):

			l1 = y.get_height()
			y.NodeUpdating(False)
			l2 = y.get_height()
			if(not l1 == l2):
				ret+=1
			y = y.get_parent()
		h2 = x.get_height()
		height_changed = not h1 == h2
		return ret, height_changed
	
	#O(1)
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
		y = node
		while(y.get_parent() is not None):
			
			y.NodeUpdating(False)
			y = y.get_parent()
		
		if p is None:
			self.root = n
		elif p.key>n.key:
			p.left = n
		else:
			p.right = n
		
		return n
	

	#O(1)
	def left_rotation(self, node : AVLNode):
		n = node.right
		p = node.parent
		n.left , node.right = node, n.left
		if n.left:
			n.left.parent = node
		else:
			pass
		if n.right:
			node.right.parent = node
		n.parent = p
		node.parent = n
		y = node
		while(y.get_parent() is not None):
			
			y.NodeUpdating(False)
			y = y.get_parent()
		
		if p is None:
			self.root = n
		elif p.key<n.key:
			p.right = n
		else:
			p.left = n
		
		return n
	#O(log(n))
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
	#O(log(n))
	def delete_bst(self, node : AVLNode):
		#node is a leaf ;updating the height
		if(not node.left.is_real_node() and not node.right.is_real_node()):
			if(node.parent is None): #root
				self.root = AVLNode(None,None)
			else:
				if node.parent.left.key == node.key:
					node.parent.left = node.right
					node.right.parent = node.parent
				else:
					node.parent.right = node.right
					node.right.parent = node.parent
				
		
		
		#node has only right son
		elif node.right.is_real_node() and not node.left.is_real_node():
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
				r = max_after.right
				l = max_after.left
				node_r = node.right

				if node.parent is not None:
					node_right = node.parent.right.key == node.key
					
				else:
					node_right = False
					
				#replacing size and height 
				node.size, max_after.size = max_after.size , node.size
				node.height, max_after.height= max_after.height, node.height
				max_after.parent = node.parent

				#update max_after sons 
				max_after.right = node_r
				max_after.left = node
				
				#parent updating
				max_after.right.parent = max_after
				max_after.left.parent = max_after

				#update node sons
				node.right = r
				node.left = l
				r.parent = node
				l.parent = node

				node.NodeUpdating()
				max_after.NodeUpdating()
		
			if(max_after.parent != None): #if node was right or left son
					if node_right:
						max_after.parent.right = max_after
					else:
						max_after.parent.left = max_after
			
      
			
			elif node.right.key == max_after.key: #right son
				
				r = max_after.right
				l = max_after.left
				node_l = node.left
		
				if node.parent is not None:
					node_right = node.parent.right.key == node.key
					
				else:
					node_right = False
					
				
				#replacing size and height 
				node.size, max_after.size = max_after.size , node.size
				node.height, max_after.height= max_after.height, node.height
				max_after.parent = node.parent
				#update max_after sons 
				max_after.right = node
				max_after.left = node_l

				#parent updating
				max_after.right.parent = max_after
				max_after.left.parent = max_after
		
				#update node sons
				node.right = r
				node.left = l
				r.parent = node
				l.parent = node

				
				node.NodeUpdating()
				max_after.NodeUpdating()

				if(max_after.parent != None): #if node was right or left son
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
			max_after.NodeUpdating()
			return max_after
		
		return node

	#O(log(n))
	def delete(self, node : AVLNode):
		balances = 0 #the returned value
		node = self.delete_bst(node)
		
		while node.parent != None and node.parent.is_real_node():
			node = node.parent
			node.NodeUpdating()
			i, node = self.fix_height_after_insertion(node)
			balances += i
		
		if node.parent is not None and node.parent.is_real_node():
			if node.parent.left.is_real_node():
				node.parent.left.NodeUpdating()
			if node.parent.right.is_real_node():
				node.parent.right.NodeUpdating()
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
	
	#O(log(n))
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
	#O(n)
	def MakeArray(self, Node : AVLNode):
		res = []
		if(Node.is_real_node() and Node!=None):
			res = self.MakeArray(Node.get_left())
			res.append((Node.get_key(),Node.get_value()))
			res += self.MakeArray(Node.get_right())
		return res
	
	#O(n)
	def avl_to_array(self):
		root = self.get_root()
		return(self.MakeArray(root))
	
	
	
    


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	#O(1)
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
	#O(log^2(n))
	def split(self, node):
		smaller = AVLTree() #will include the bigger than node nodes
		bigger = AVLTree() #will include the bigger than node nodes
		if(not node.get_left().is_real_node()):
			smaller.set_root(None)
		else:
			smaller.set_root(node.get_left())
			node.get_left().set_parent(None)
		if(not node.get_right().is_real_node()):
			bigger.set_root(None)
		else:
			bigger.set_root(node.get_right())
			node.get_right().set_parent(None)
		while(node.get_parent() is not None):
			key = node.get_key()
			node = node.get_parent()
			if(key > node.get_key()):#היינו בבן ימני
				to_join = AVLTree()
				to_join.set_root(node.get_left())
				node.get_left().set_parent(None)#unlink
				smaller.join(to_join, node.get_key(), node.get_value())
			else:#היינו בבן שמאלי
				to_join = AVLTree()
				to_join.set_root(node.get_right())
				node.get_right().set_parent(None)#unlink
				bigger.join(to_join, node.get_key(), node.get_val())

		return smaller, bigger

	
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
	#O(log(n))
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
			new_root.NodeUpdating()
			self.set_root(x)
			return abs(T1.Tree_Height() - T2.Tree_Height())+1
		

		else:
			ret = abs(T1.Tree_Height()-T2.Tree_Height())+1

			if(T1.Tree_Height()>T2.Tree_Height()):
				T3 = AVLTree()
				b = T1.find_Node(T2.Tree_Height(),"r")
				b_parent = b.get_parent()
				x.set_right(T2.get_root())
				(T2.get_root()).set_parent(x)
				
				x.set_left(b)
				b.set_parent(x)
				b_parent.set_right(x)
				x.set_parent(b_parent)
				
				y = x
				while(y is not None):
					y.NodeUpdating()
					y = y.get_parent()
				root1.set_parent(None)
				self.set_root(root1)
				
			

			else:
				
				T3 = AVLTree()
				b = T2.find_Node(T1.Tree_Height(),"l")
				b_parent = b.get_parent()
				x.set_left(T2.get_root())
				(T2.get_root()).set_parent(x)
				x.set_right(b)
				b.set_parent(x)
				b_parent.set_left(x)
				x.set_parent(b_parent)
				y = x

				while(y is not None):
					
					y.NodeUpdating()
					y = y.get_parent()

				self.set_root(root1)


		tree = None		
		self.set_root(root1)
		return ret


	#O(log(n))
	def find_Node(self,i, d):
		root = self.get_root()
		height = root.get_height()
		if(d == "r"):
			while(height != i):
				if(root.get_right().is_real_node()):
					root = root.get_right()
				else:
					root = root.get_left()

				height = root.get_height()
			return root
		else:
			while(height != i):
				if(root.get_left().is_real_node()):
					root = root.get_left()
				else:
					root = root.get_right()

				height = root.get_height()
			return root
		



	"""compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""
	#o(log(n))
	def rank(self, node : AVLNode):
		c = node.get_left().get_size()+1
		y = node
		while(y.get_parent() is not None):
			x = y
			y = y.get_parent()
			if(x is y.get_right()):
				c += y.get_left().get_size()+1

		return c



	"""finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""
	#o(log(n))
	def select(self, i):
		return self.select_rec(self.get_root(), i)

	
	"""finds the i'th smallest item (according to keys) in the tree rooted in node

	@type i: int
	@pre: 1 <= i <= node.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in the tree rooted in node
	"""
	#o(log(n))
	def select_rec(self,node, i):
		r = node.get_left().get_size() + 1
		if(i == r):
			return node
		elif(i < r):
			return self.select_rec(node.get_left(), i)
		else:
			return self.select_rec(node.get_right(), i - r)


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	#O(1)
	def get_root(self):
		if(self!=None):
			return self.root
		return None

	
