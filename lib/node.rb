
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
