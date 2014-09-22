require './lib/trie'
require './lib/node'

class Ruzzle
  def initialize puzzle_str, dictionary_file='var/dictionary.txt'
    @puzzle_str = puzzle_str
    self.create_graph puzzle_str
    self.create_trie dictionary_file
  end

  # Opens a dictionary text file, reads each word in
  # line by line and creates a Trie.
  def create_trie dictionary_file
    @trie = Trie.new
    File.readlines(dictionary_file).each do |line|
      head = @trie
      word = line.chomp
      word.scan(/\w/).each do |letter|
        head.add_branch(Trie.new letter) unless head[letter]
        head = head[letter]
      end

      head.set_word_end
    end
  end

  # Creates the ruzzle board from the string passed
  # in. The board is created from left to right, top 
  # to bottom
  def create_graph puzzle_str
    @board = puzzle_str.downcase.scan(/\w/).map { |letter| Node.new letter }
    puzzle_str.length.times do |m|
      node = @board[m]
      i, j = m / 4, m % 4
      puzzle_str.length.times do |n|
        x, y = n / 4, n % 4
        if (i-x).abs < 2 && (j-y).abs < 2 && m != n
          neighbor = @board[n]
          node.add_neighbor neighbor
        end
      end
    end
  end

  # Iterate over the nodes on the boards checking
  # for all solutions starting at that point
  def solve
    found_words = Array.new
    @board.each do |node|
      if @trie[node.value]
        words = process_trie @trie, node
        found_words = found_words + words
      end
    end
    found_words.uniq.sort_by { |x| [-x.length, x] }
  end

  # Starts at a passed in head node, if the
  # node is None then returns what it's found
  # Otherwise it checks if this is the end of
  # a word and adds it to words. Then checks
  # each neighbor node in turn.
  def process_trie head, node, visited=[]
    return [] unless head

    words = Array.new
    words << head.value if head.is_word_end?
    visited << node

    node.neighbors.each do |neighbor|
      unless visited.include? neighbor
        results = process_trie head[neighbor.value], neighbor, visited
        words = words + results.map { |ending| head.value + ending }
      end
    end
    visited.delete(node)

    words
  end
end
