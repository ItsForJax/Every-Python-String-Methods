# All string methods showcase by Erickson Dela Soledad

# Index - Similar to `find()`, but raises a `ValueError` if `sub` is not found. 

string_input = "Hello World"
print(string_input.index('el')) # prints -> 1 (its the index of the first letter, this case e)
print(string_input.index('o')) # prints -> 4 (at index 4 is the first occurence of letter "o")
try:
    print(string_input.index('x')) # Throws an error so will go thru the value error
except ValueError:
    print("This prints because of error")
