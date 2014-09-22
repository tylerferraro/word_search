#######################################
# Trie Class                          #
#                                     #
# Developer: Tyler Ferraro            #
#            tyler.ferraro@gmail.com  #
#######################################


# Main code execution, needs to be wrapped up.
# Passes in a board string, creates the board in
# an array, setups the connections, creates a trie
# from the dictionary and then iterates over each
# starting point on the board as the head node and
# returns found words.

require './lib/ruzzle'

puts "Usage: ./ruzzle_solver.rb PUZZLESTRING" unless ARGV.length == 1
game = Ruzzle.new ARGV.first
puts game.solve.inspect