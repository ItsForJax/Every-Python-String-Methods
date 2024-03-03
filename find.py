# All string methods showcase by Erickson Dela Soledad

# Find - Returns the lowest index in the string where substring `sub` is found. Returns -1 if `sub` is not found. 

string_input = "Hello World"
print(string_input.find('el')) # prints -> 1 (its the index of the first letter, this case e)
print(string_input.find('o')) # prints -> 4 (at index 4 is the first occurence of letter "o")
print(string_input.find('x')) # prints -> -1 (x is not found)
