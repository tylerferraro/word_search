class Trie:
	def __init__(self, letter=""):
		self.branches = {}
		self.letter = letter
		self.end_word = False

	def __getitem__(self, letter):
		return self.branches.get(letter, None)

	def isWordEnd():
		return self.is_word_end

	def setWordEnd(self, value=True):
		self.word_end = value

	def getLetter(self):
		return self.letter

	def addBranch(self, branch):
		self.branches[branch.getLetter()] = branch

	def printTrie(self, tab_level=0):
		print "\t" * tab_level + self.letter
		for v in self.branches.values():
			v.printTrie(tab_level+1)

class Node:
	def __init__(self, letter):
		self.value = letter
		self.neighbors = []
		self.visited = False

	def addNeighbor(self, neighbor):
		self.neighbors.append(neighbor)

	def getNeighbors(self):
		return self.neighbors

	def setVisited(self, visited):
		self.visited = visited

	def isVisited(self):
		return self.visited

	def getValue(self):
		return self.value

def createTrie(dictionary_file):
	with open(dictionary_file, 'r') as fin:
		content = fin.readlines()

	trie = Trie()
	for line in content:
		head = trie
		word = line.rstrip()
		for letter in word:
			if not head[letter]:
				head.addBranch(Trie(letter))
			head = head[letter]
		head.setWordEnd()

	return trie

def createConnections(board, puzzle_str):
	for m in range(0, len(puzzle_str)):
		node = board[m]
		i, j = m // 4, m % 4
		for n in range(0, len(puzzle_str)):
			x, y = n // 4, n % 4
			if abs(i-x) < 2 and abs(j-y) < 2 and m != n:
				neighbor = board[n]
				node.addNeighbor(neighbor)

RUZZLE_PUZZLE = "ABCDEFGHIJKLMNOP"
board = [Node(letter) for letter in RUZZLE_PUZZLE]
createConnections(board, RUZZLE_PUZZLE)
trie = createTrie('test_dict.txt')
trie.printTrie()