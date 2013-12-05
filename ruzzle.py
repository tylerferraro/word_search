#######################################
# Trie Class                          #
#                                     #
# Developer: Tyler Ferraro            #
#            tyler.ferraro@gmail.com  #
#######################################

from trie import Trie, Node

# Opens a dictionary text file, reads each word in and 
# creates a Trie.
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

# Creates the ruzzle board from a string passed into
# the function. Creates the board left to right, top 
# to bottom
def createConnections(board, puzzle_str):
	for m in range(0, len(puzzle_str)):
		node = board[m]
		i, j = m // 4, m % 4
		for n in range(0, len(puzzle_str)):
			x, y = n // 4, n % 4
			if abs(i-x) < 2 and abs(j-y) < 2 and m != n:
				neighbor = board[n]
				node.addNeighbor(neighbor)

# Starts at a passed in head node, if the
# node is None then returns what it's found
# Otherwise it checks if this is the end of
# a word and adds it to found. Then checks
# each neighbor node in turn.
def algorithm(head, node, visited=[]):
	found = []
	
	if not head:
		return found

	if head.isWordEnd():
		found.append(head.getLetter())

	visited.append(node)

	for neighbor in node.getNeighbors():
		if neighbor not in visited:
			results = algorithm(head[neighbor.getValue()], neighbor, visited)
			found.extend([head.getLetter() + ending for ending in results])

	visited.remove(node)
	return found

# Main code execution, needs to be wrapped up.
# Passes in a board string, creates the board in
# an array, setups the connections, creates a trie
# from the dictionary and then iterates over each
# starting point on the board as the head node and
# returns found words.
RUZZLE_PUZZLE = "TIMILNEDEAOMTCAR".lower()
board = [Node(letter) for letter in RUZZLE_PUZZLE]
createConnections(board, RUZZLE_PUZZLE)
trie = createTrie('ruzzle_dictionary.txt')

results = []
for node in board:
	head = trie
	if head[node.getValue()]:
		found_words = algorithm(head[node.getValue()], node)

		if len(found_words) > 0:
			results.extend(found_words)

results = list(set(results))
output = sorted(results, key=lambda word: [len(word)], reverse=True)

print len(results)
print output