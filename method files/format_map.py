# All string methods showcase by Erickson Dela Soledad

# Format_map - Similar to `format()`, but uses a mapping object to fill in the placeholders. 

mapping = {"Key1": "Hello", "key2": "World"}
string_input = "{Key1} {key2}"

print(string_input.format_map(mapping))

# prints -> Hello World (notice that the keys are replaced by the map values)