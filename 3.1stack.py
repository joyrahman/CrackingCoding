class Stack:
	'constructor'
	#array=[]
	#top = 0
	#size = 0
	
	def __init__( self,base, size, global_list):
		self.base = base
		self.size = size
		self.top = 0
		self.array=global_list
		self.min  = 10000000
	
	def push(self,x):
		if(self.top>=self.size):
			print("no more space left")
		else:
			self.array[self.base+self.top]=x
			self.top+=1
			if(self.min>x):
				self.min= x

			
	def pop(self):
		if(self.top<=0):
			print ("empty list")
		else:
			self.top-=1
			return self.array[self.top];
	

	def getMin(self):
		return self.min
			

	def printStack(self):
		for i in range (0,self.top):
			print(self.array[self.base+i])






'main method'
global_size = input()
residue = global_size%3
global_list = [None]*global_size
stack1 = Stack(0*global_size/3,global_size/3 + residue,global_list)
stack2 = Stack(residue+ 1*global_size/3,global_size/3,global_list)
stack3 = Stack(residue+ 2*global_size/3,global_size/3,global_list)
'stack1'
print("-------s1-------")
stack1.push(5)
stack1.push(15)
stack1.printStack()
print("min:",stack1.getMin())
'stack2'
print("-------s2-------")
stack2.push(25)
stack2.push(35)
stack2.printStack()
print("min:",stack2.getMin())
'stack3'
print("-------s3-------")
stack3.push(17)
stack3.push(18)
stack3.printStack()
print("-------s1-------")
stack1.pop()
stack1.pop()
stack1.pop()
stack1.printStack()




			