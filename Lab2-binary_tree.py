'''
* Create a class "binary_tree" restricted to trees with only two subtrees, L and R (a left binary subtree and a right binary subtree.)
* AddLeft, and AddRight methods
* A Get_LevelOrder function.

* Create a function, ConvertToTree, for the binary tree class that will generate the associated
tree representation.
The return value is a list where the first element of the list is True (if the 
conversion can be performed) or False (if otherwise). The second element of the list
is the Tree that is created .
'''
import tree #Run in the same directory as tree.py, and rename this file to binary_tree.py

class queue: #Same as in tree.py
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

        def anti_dequeue(self):
                if (self.queue != []):
                        rval = self.queue[len(self.queue)-1]
                        self.queue = self.queue[0:len(self.queue)-1]
                        return rval
                else:
                        return 0
        def empty(self):
                if self.queue == []:
                        return True
                else:
                        return False
                        
        def length(self):
                count = 0
                for i in self.queue:
                        count = count+1
                return count

        def printQ(self):
                print self.queue

class binary_tree:
    def __init__(self,x): #Initialize L and R subtrees to 0, and user inputted node value.
        self.bstore = [x,[0],[0]]

    def AddLeft(self,x):
        self.bstore[1] = [x]
        return True

    def AddRight(self,x):
	self.bstore[2] = [x]
	return True
        
    def rval(self): #Debugging utility
	return self.bstore
   
    def Get_LevelOrder(self):
        temp = queue()
        accum = []
        temp.Enqueue(self.bstore)
        while(temp.empty() == False):
                node = temp.Dequeue()
                accum = accum + [node[0]]	
		for i in range(0, len(node[1]),1): #Add all the left subtree elements to level order
			if node[1][i] != 0:        
				temp.Enqueue(node[1][i].bstore)

		for i in range(0, len(node[2]),1): #Add all the right subtree elements to level order
			if node[2][i] != 0:
	                       	temp.Enqueue(node[2][i].bstore)

        return accum

    def help_ConvertToTree(self): #helper function to convert binary to k-ary tree
	temp = queue()
	retval = tree.tree(self.bstore[0]) #initialize return tree
        
        for i in range(0,len(self.bstore[1])):
                if isinstance(self.bstore[1][i], binary_tree): #Add everything in the left subtree recursively to the queue
			subtree = self.bstore[1][i].help_ConvertToTree()
                	temp.Enqueue(subtree)
                        
	for i in range(0,len(self.bstore[2])):
		if self.bstore[2][i] != 0: #Add everything in the right subtree recursively to the queue (if it exists)
			subtree = self.bstore[2][i].help_ConvertToTree()
			temp.Enqueue(subtree)
                        
        while(temp.length() > 1):
		a = temp.Dequeue()
                while temp.length() > 0:
			b = temp.anti_dequeue() #Convert left successors to children and right successors as siblings
			retval.AddSuccessor(b)
                temp.Enqueue(a)
		M = temp.printQ()
		print M
        check = temp.Dequeue()
        if isinstance(check, tree.tree): #instance check, as in tree.py; Again, fix the patch as an exercise.
                retval.AddSuccessor(check)
        return retval

    def ConvertToTree(self): #Calls the helper function
	ret_tree = self.help_ConvertToTree()
	return [True, ret_tree] 
