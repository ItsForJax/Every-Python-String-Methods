# All string methods showcase by Erickson Dela Soledad

# Center - Returns a centered string of length `width`. Optionally, padding can be specified with the `fillchar`. 

string_input = "Hello World"

print(string_input.center(20))

print(string_input.center(20, '*')) # with fillchar


# prints:

#     Hello World     
# ****Hello World*****

# notice that without fillchar it adds space instead