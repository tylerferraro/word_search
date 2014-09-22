#######################################
# Ruzzle Solver                       #
#                                     #
# Use: For finding the largest words  #
#   and almost all words in the       #
#   Ruzzle puzzle game.               #
#                                     #
# Developer: Tyler Ferraro            #
#            tyler.ferraro@gmail.com  #
#######################################

require './lib/ruzzle'

puts "Usage: ./ruzzle_solver.rb PUZZLESTRING" unless ARGV.length == 1
game = Ruzzle.new ARGV.first
puts game.solve.inspect