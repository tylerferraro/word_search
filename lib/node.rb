# Graph node class for the ruzzle board.
# Used to traverse the board and find 
# words based on a dictionary trie

class Node
  attr_reader :value, :neighbors

  def initialize value
    @value = value
    @neighbors = Array.new
  end

  def add_neighbor neighbor
    @neighbors << neighbor
  end
end