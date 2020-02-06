import sys, os, time
# from __future__ import print_function

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
			print("%s"%(temp.data), end= ",")
			temp = temp.link

	def printRec(self, link):
		if link == None:
			return
		print(link.data, end=",")
		self.printRec(link.link)
	
	def revPrintRec(self, link):
		if link == None:
			return
		self.revPrintRec(link.link)
		print(link.data, end=",")

	def recP(self):
		self.printRec(self.__head)
	
	def recRevP(self):
		self.revPrintRec(self.__head)

	def rev(self):
		if self.__head == None:
			return
		prev, cur, nxt = None, self.__head, self.__head.link
		while cur != None:
			nxt = cur.link
			cur.link = prev
			prev = cur
			cur = nxt
		self.__head = prev

	def doRev(self, lnk):
		if lnk.link == None:
			self.__head = lnk
			return
		self.doRev(lnk.link)
		lnk.link.link = lnk
		lnk.link = None

	def revRec(self):
		self.doRev(self.__head)

def main():
	myll = ll()
	myll.insertNode(1)
	myll.insertNode(3)
	myll.insertNode(5)
	myll.insertNode(7)
	# myll.printll()
	
	# myll.recP()
	# print
	# myll.recRevP()
	print("Normal:")
	myll.printll()
	myll.rev()
	print("\nrev:")
	myll.printll()
	print("\nrev rev:")
	myll.revRec()
	myll.printll()
	print("")

if __name__ == "__main__":
	main()