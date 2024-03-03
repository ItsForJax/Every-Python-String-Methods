# All string methods showcase by Erickson Dela Soledad

# Expandtabs - Returns a copy of the string where tab characters are replaced by one or more spaces, depending on the current column and the given tab size. 

string_input = "\tHello\tWorld"
print(string_input.expandtabs(10)) # default is 8 space

# prints -> "          Hello     World" 