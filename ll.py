import sys, os, time

class Node(object):
	def __init__(self, data):
		self.data = data
		self.link = None

class ll(object):
	def __init__(self):
		self.__head = None

	def insertNode(self, data):
		newNode = Node(data)
		if self.__head == None:
			self.__head = newNode
			return

		temp = self.__head
		while(temp.link != None):
			temp = temp.link
		temp.link = newNode

	def printll(self):
		temp = self.__head 
		while temp != None:
			print("%s"%(temp.data))
			temp = temp.link

	def printRec(self, link):
		if link == None:
			return
		print link.data
		self.printRec(link.link)
	
	def revPrintRec(self, link):
		if link == None:
			return
		self.revPrintRec(link.link)
		print link.data

	def rec(self):
		self.printRec(self.__head)
	
	def recRev(self):
		self.revPrintRec(self.__head)

	def rev(self):
		prev, cur, nxt = None,

def main():
	myll = ll()
	myll.insertNode(1)
	myll.insertNode(3)
	myll.insertNode(5)
	myll.insertNode(7)
	# myll.printll()
	
	myll.rec()
	print
	myll.recRev()

if __name__ == "__main__":
	main()