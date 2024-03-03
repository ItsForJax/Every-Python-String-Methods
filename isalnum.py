# All string methods showcase by Erickson Dela Soledad

# Isalnum - Returns `True` if all characters in the string are alphanumeric. 

string_input = "Hello World"
string_input2 = '123'
string_input3 = '123qwerty'

print(string_input.isalnum()) # prints false since string_input only contains text
print(string_input2.isalnum()) # prints true since the string has numbers
print(string_input3.isalnum()) # prints true since the string has numbers