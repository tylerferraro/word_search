Ruzzle-Solver
=============

Python script for solving a Ruzzle board. It reads in a dictionary text file and stores it in a
custom Trie structure. This dictionary isn't exactly what Ruzzle uses but it's close. The 
ruzzle board is hard coded right now but should be extracted out to let the user pass it in
via command line.

The algorithm works simply by iterating over each point in the ruzzle board setting it as the head node. It then uses the dictionary trie to find actual words selecting each neighbor node and only continuing on if it exists in the dictionary trie.