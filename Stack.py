#Stack con lista enlazada en python
class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack():
	def __init__(self):
		self.size = 0
		self.header = None

	#push O(1)
	def push(self,data):
		#si el stack esta vacio
		if(self.header == None):
			newNode = Node(data)
			self.header = newNode
		else:
			newNode = Node(data)
			newNode.next = self.header
			self.header = newNode
		self.size += 1

	#pop O(1)
	def pop(self):
		#si el Stack esta vacio , no se hace pop
		if(self.header == None):
			print("Stack vacio , no se puede hacer pop")
			return
		top = self.header.data
		self.header = self.header.next
		self.size -= 1
		return top

	def top(self):
		#si el Stack esta vacio
		if(self.header == None):
			print("el Stack esta vacio,no hay elementos en la cima")
			return None
		nodeTop = self.header.data
		return nodeTop


	def getSize(self):
		return self.size

	def isEmpty(self):
		if(self.header == None):
			return True
		return False

	def printStack(self):
		if(self.header == None):
			print("Stack vacio")
			return
		reference = self.header
		while(reference.next):
			print(reference.data,"-> ",end='')
			reference = reference.next
		print(reference.data,"-> None")


def main():
	stack = Stack()
	stack.pop()
	stack.top()
	stack.printStack()

if __name__ == '__main__':
	main()






