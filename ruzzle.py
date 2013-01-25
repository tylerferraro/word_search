from trie import Trie, Node

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

def findWords(head, node, visited=[]):
	if head:
		visited.append(node)
		results = []
		for neighbor in node.getNeighbors():
			if neighbor not in visited and head[neighbor.getValue()]:
				endings = findWords(head[neighbor.getValue()], neighbor, visited)
				results.extend([head.getLetter() + ending for ending in endings])

		if head.isWordEnd():
			results.append(head.getLetter())

		return results

	return []

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

RUZZLE_PUZZLE = "RETTDAAKEISTRECN".lower()
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