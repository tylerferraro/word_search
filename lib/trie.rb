
	class Trie
		attr_reader :is_word_end, :value

		def initialize value=""
			@branches = Hash.new
			@value = value
			@is_word_end = false
		end

		def [] value
			@branches[value]
		end

		def is_word_end?
			@is_word_end
		end

		def set_word_end value=true
			@is_word_end = value
		end

		def add_branch branch
			@branches[branch.value] = branch
		end

		def print
			puts @branches
		end
	end


