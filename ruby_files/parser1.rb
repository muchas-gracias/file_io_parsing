require 'pathname'

file_path = Pathname.new('../files/parser1.txt')

File.foreach(file_path) do |line|
    puts line
  end
  