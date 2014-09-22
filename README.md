## Ruzzle Solver
[Official Ruzzle Url](http://www.ruzzle-game.com)

This solver uses a generic dictionary found on the internet and not the actual dictionary used in the game. It isn't 100% accurate but does get a high majority of the words, especially the large ones.

There are two main branches to this repository. The original solver was written in **python**. I have since updated the master to point to the **ruby** implementation which I am more comfortable writing in these days.

---
### Technical notes
The algorithm works simply by iterating over each point in the ruzzle board setting it as the head node. It then uses the dictionary trie to find actual words by traversing the graph of the board. Selecting each neighboring node and only continuing on if it exists in the dictionary trie helps this algorithm to be more efficient.

The answers are printed out alphabetically and by largest words first.

<br/>

![Ruzzle icon](http://www.ruzzle-game.com/images/logo.png) 