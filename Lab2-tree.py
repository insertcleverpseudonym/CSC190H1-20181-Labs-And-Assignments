'''
Trees

1. Consider a general Tree, T:
* T can be an empty list
* T can be a 2 element list where:
     * T[0] is a value (node)
     * T[1] is a list of subtrees
       
Example of usage:
>>> x = tree(1)
>>> y = tree(2)
>>> z = tree(3)
>>> x.AddSuccessor(y)
>>> x.AddSuccessor(z)
>>> c = tree(5)
>>> z.AddSuccessor(c)

The diagram for this tree is (identation -> subtrees):
1000
   2000
   3000
        5

* define Print_DepthFirst(self), for use as a debugging tool.
* define Get_LevelOrder and return a linear list of the level order traversal values.
* define ConvertToBinaryTree that will generate and return the equivalent binary tree representation of the tree.
'''
import binary_tree #put binary_tree.py in the same directory as this file when you run it + rename this file to tree.py

class queue:
	def __init__(self):
		self.queue = []
	
	def Enqueue(self,x):
		self.queue = self.queue + [x]

	def Dequeue(self):
		if(self.queue != []):	
			rval = self.queue[0]
			self.queue = self.queue[1:]
			return rval
		else:
			return 0

	def anti_dequeue(self): #essentially a stack-pop
		if (self.queue != []):
			rval = self.queue[len(self.queue)-1]
			self.queue = self.queue[0:len(self.queue)-1]
			return rval
		else:
			return 0
      
	def empty(self): #Checks if the queue is empty
		if self.queue == []:
			return True
		else:
			return False
      
	def length(self): #length utility
		count = 0
		for i in self.queue:
			count = count+1
		return count

	def printQ(self): # print utility
		print self.queue

class tree:
    def __init__(self,x): #empty list of subtrees, user-input node value
        self.store = [x,[]]

    def AddSuccessor(self,x): #Adds a successor
        self.store[1] = self.store[1] + [x]
        return True

    def Print_DepthFirst(self):
	    self.checker(0)

    def checker(self, depth): #print_DepthFirst helper function
      print self.store[0]
      for i in range (0,len(self.store[1]),1):
        print '    '*(depth+1)*2, #Adds indents
        self.store[1][i].checker(depth+1) #Recursively calls the function for the next 'layer'

    def Get_LevelOrder(self): #LevelOrder function
      temp = queue()
      accum = []
      temp.Enqueue(self.store) #Add the root of the tree to the queue
      while(temp.empty() == False): #This is akin to a visited-check approach.
        node = temp.Dequeue()
        accum = accum + [node[0]]
        for i in range(0, len(node[1]),1): #Add each node, layer by layer.
          temp.Enqueue(node[1][i].store)
      return accum
	
    def ConvertToBinaryTree(self):
	temp = queue()
	retval = binary_tree.binary_tree(self.store[0]) #initialize a binary tree to store our general tree
	for i in range(0,len(self.store[1])):
		subtree = self.store[1][i].ConvertToBinaryTree() #recursively convert subtrees
		temp.Enqueue(subtree) #add the convert subtrees to the queue

	while(temp.length() > 1):
		a = temp.anti_dequeue() #pop the first two nodes
		b = temp.anti_dequeue()

		b.AddRight(a) #make the siblings right sucessors
		temp.Enqueue(b)
	leftcheck = temp.Dequeue()
	if isinstance(leftcheck, binary_tree.binary_tree): #Ensure that we're adding a subtree, not an incorrect type.
                #This prevents a bug where garbage is added. Exercise: Make the function work without this patch.
		retval.AddLeft(leftcheck)
	return retval #Return the binary tree

#Commented Out Test Code, uncomment to run.
#x=tree(1000)
#y=tree(2000)
#z=tree(3000)
#x.AddSuccessor(y)
#x.AddSuccessor(z)
#c=tree(5)
#d =tree(6)
#z.AddSuccessor(c)
#c.AddSuccessor(d)
#x.Print_DepthFirst()
#L = x.Get_LevelOrder()
#print L
#M = x.genBinaryTree()
#print M.Get_LevelOrder()
