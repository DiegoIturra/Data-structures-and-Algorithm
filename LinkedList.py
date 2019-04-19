#Lista simplemente enlazada en python

class Node():
	#iniciamos el nodo 
	def __init__(self,data):
		self.data = data
		self.next = None

#---------------------------------------------------------------------------------
class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.Size = 0

	#insersion en O(1) al principio de la lista
	def insertAtBeggining(self,data):
		#creamos un nuevo nodo
		newNode = Node(data)
		#si la lista esta vacia
		if(self.head == None):
			self.head = newNode
			self.tail = newNode
		#si la lista no esta vacia y hay al menos un nodo
		else:
			newNode.next = self.head
			self.head = newNode
		self.Size = self.Size + 1

	#insersion en O(1) al final de la lista
	def insertAtEnd(self,data):
		newNode = Node(data)
		#si la lista esta vacia
		if (self.head == None and self.tail == None):
			self.head = newNode
			self.tail = newNode
		#si la lista tiene al menos un elemento
		else:
			self.tail.next = newNode
			self.tail = newNode
		self.Size = self.Size + 1

	#insercion en O(n) , insertar en la posicion dada ,elementos se desplazan
	def insertAt(self,position,data):
		#si la lista esta vacia, se ignora la posicion
		if(self.tail == None and self.head == None):
			print("no existe la posicion dada")
			return
		else:
			newNode = Node(data)
			it = 0
			prevNode = self.head
			if(position <= self.Size and position >= 0):
				while(it < (position-1) and prevNode.next):
					prevNode = prevNode.next
					it += 1
				newNode.next = prevNode.next
				prevNode.next = newNode
				self.Size += 1
		#si la posicion no existe , simplemente no inserta

	#remover en O(n) peor caso , remueve en la posicion dada
	def removeNodeAt(self,position):
		if(position < 0 or position >= self.Size):
			print("no se puede eliminar una posicion que no existe")
			return
		if(position == 0):
			self.removeNodeAtBeggining()
		elif(position == self.Size-1):
			self.removeNodeAtEnd()
		else:
			it = 0
			prevNode = self.head
			while(it < (position-1) and prevNode.next):
				it += 1
				prevNode = prevNode.next
			prevNode.next = prevNode.next.next
			self.Size -= 1

	#remover O(1) , remueve al incio de la lista
	def removeNodeAtBeggining(self):
		#si la lista esta vacia
		if(self.head == None and self.tail == None):
			print("lista esta vacia")
			return
		auxNode = self.head
		self.head = auxNode.next
		self.Size -= 1

	#remover O(n) , remueve al final de la lista
	def removeNodeAtEnd(self):
		#si la lista esta vacia
		if(self.head == None and self.tail == None):
			print("lista esta vacia")
			return
		#si solo tiene un elemento
		elif(self.head.next == None):
			self.removeNodeAtBeggining()
		else:
			it = 0
			prevNode = self.head
			while(it < (self.Size-1) and prevNode.next.next):
				it += 1
				prevNode = prevNode.next
			prevNode.next = prevNode.next.next
			self.Size -= 1

	#obtenemos el nodo que esta en la posicion dada
	def getNodeAt(self,position):
		if(self.head == None and self.tail == None):
			return None
		elif(position < 0 or position >= self.Size):
			print("no hay nodo en la posicion dada")
			return None
		it = 0
		prevNode = self.head
		while (it < position and prevNode.next):
			it += 1
			prevNode = prevNode.next
		return prevNode

	#modifica el nodo en la posicion dada
	def setNodeAt(self,position,newData):
		if(self.head == None and self.tail == None):
			print("lista vacia , no se puede modificar un nodo")
			return
		elif(position < 0 or position >= self.Size):
			print("no se puede modificar un nodo que no existe")
			return
		it = 0
		prevNode = self.head
		while(it < position and prevNode.next):
			it += 1
			prevNode = prevNode.next
		prevNode.data = newData
			
	#obtenemos la dimension de la lista
	def getSize(self):
		return self.Size

	#imprime la lista enlazada
	def printLinkedList(self):
		pointer = self.head
		if(pointer == None):
			return
		else:
			while(pointer.next):
				print(pointer.data,"->",end="")
				pointer = pointer.next
			print(pointer.data,"->None")

#funcion principal , para probar metodos
def main():
	
	lista = LinkedList()
	lista.insertAtBeggining(1)
	lista.insertAtBeggining(3)
	lista.insertAtBeggining("Hello !!")
	lista.setNodeAt(1,"Hi !!")
	lista.printLinkedList()

if __name__ == '__main__':
	main()


