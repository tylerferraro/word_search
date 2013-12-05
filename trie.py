#######################################
# Trie Class                          #
#                                     #
# Developer: Tyler Ferraro            #
#            tyler.ferraro@gmail.com  #
#######################################

class Trie:
	def __init__(self, letter=""):
		self.branches = {}
		self.letter = letter
		self.is_word_end = False

	def __getitem__(self, letter):
		return self.branches.get(letter, None)

	def isWordEnd(self):
		return self.is_word_end

	def setWordEnd(self, value=True):
		self.is_word_end = value

	def getLetter(self):
		return self.letter

	def addBranch(self, branch):
		self.branches[branch.getLetter()] = branch

	def printTrie(self):
		print self.branches

class Node:
	def __init__(self, value):
		self.value = value
		self.neighbors = []

	def addNeighbor(self, neighbor):
		self.neighbors.append(neighbor)

	def getNeighbors(self):
		return self.neighbors

	def getValue(self):
		return self.value





