'''
Write a class for a stack data structure (LIFO) in Python, called StackLib:
Methods:
* init
* push
* pop

Write a function "bc" that takes in a string, and return a list, L which indicates whether the brackets match and the index at which the matching failed, if at all.

Note: Ctrl-D is used to indicate the end of user input.
'''

class stack:

        def __init__(self):
                self.list = [] #internal variable

        def push (self, value):
                self.list = self.list + [value] #add to the stack from the tail end


        def pop(self):
                length = len(self.list)
                if length == 0:
                        return -1 #underflow check
                else:
                        rval = self.list[length-1]
                        self.list = self.list[0:length-1] #remove from the tail end, subsequently return the removed value.
                        return rval

        def disp(self):
                M = list(self.list)
                return M # a debugging tool to display our stack. Not necessary, but good practice.
              
def bc(str):
  #initialize all variables
	input_list = stack()
	L = []
	c = ''
	pos = -1 #starting vaule, since we increment before processing
	length = len(str)
	while (pos<length-1): #iterate over the entire list
		pos = pos + 1
		c = str[pos] #get value at the index

		if c in ['(','{','[']: #Opening brackets, push to stack
			input_list.push(c)

		if c == ')':
			x = input_list.pop()
			if x != '(': #check for bracket mismatch
				L = [False, pos]
				return L
		if c == '}':
			x = input_list.pop()
			if x != '{':
				L =  [False, pos]
				return L
		if c == ']':
			x = input_list.pop()
			if x != '[':
				L = [False, pos]
				return L

	x = input_list.pop() #Check if the stack is empty, to verify bracket imbalance
	if x != -1:
		L = [False, pos]
		return L
	elif x == -1: #If all of our tests pass, the brackets match.
		L = [True, 0]
		return L #Required output
