# Trie class for storing the dictionary
# of words used to solve the Ruzzle
# game. This is not the exact dictionary
# used in the actual game.

class Trie
	attr_reader :is_word_end, :value

	def initialize(value="")
		@branches = { }
		@value = value
		@is_word_end = false
	end

	def [](value)
		@branches[value]
	end

	def is_word_end?
		@is_word_end
	end

	def set_word_end(value=true)
		@is_word_end = value
	end

	def add_branch(branch)
		@branches[branch.value] = branch
	end

	def print
		puts @branches
	end
end