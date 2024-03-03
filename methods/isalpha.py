# All string methods showcase by Erickson Dela Soledad

# Isalpha - Returns `True` if all characters in the string are alphabetic. 

string_input = "Hello World"
string_input2 = 'qwerty'
string_input3 = '123qwerty'

print(string_input.isalpha()) # prints false multiple duplicate letter
print(string_input2.isalpha()) # prints true since it only contain a character once
print(string_input3.isalpha()) # prints false since the input has numbers