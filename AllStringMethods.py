# All string methods showcase by Erickson Dela Soledad

# get all string methods except dunder methods and save it in a txt file
import os

methodss = { "capitalize" : "Returns a copy of the string with the first character capitalized.",
            "casefold" : "Returns a casefolded copy of the string, suitable for caseless comparisons.",
            "center" : "Returns a centered string of length `width`. Optionally, padding can be specified with the `fillchar`.",
            "count" : "Returns the number of occurrences of substring `sub` in the string. Optional parameters `start` and `end` specify the slice of the string to search within.",
            "encode" : "Returns an encoded version of the string using the specified encoding.",
            "endswith" : "Returns `True` if the string ends with the specified suffix.",
            "expandtabs" : "Returns a copy of the string where tab characters are replaced by one or more spaces, depending on the current column and the given tab size.",
            "find" : "Returns the lowest index in the string where substring `sub` is found. Returns -1 if `sub` is not found.",
            "format" : "Formats the string with the supplied arguments and/or keyword arguments.",
            "format_map" : "Similar to `format()`, but uses a mapping object to fill in the placeholders.",
            "index": "Similar to `find()`, but raises a `ValueError` if `sub` is not found.",
            "isalnum": "Returns `True` if all characters in the string are alphanumeric.",
            "isalpha": "Returns `True` if all characters in the string are alphabetic.",
            "isascii": "Returns `True` if all characters in the string are ASCII.",
            "isdecimal": "Returns `True` if all characters in the string are decimal.",
            "isdigit": "Returns `True` if all characters in the string are digits.",
            "isidentifier": "Returns `True` if the string is a valid Python identifier.",
            "islower": "Returns `True` if all characters in the string are lowercase.",
            "isnumeric": "Returns `True` if all characters in the string are numeric.",
            "isprintable": "Returns `True` if all characters in the string are printable.",
            "isspace": "Returns `True` if all characters in the string are whitespace.",
            "istitle": "Returns `True` if the string is titlecased.",
            "isupper": "Returns `True` if all characters in the string are uppercase.",
            "join" : "Returns a string concatenated with the elements of an iterable.",
            "ljust" : "Returns the string left-justified in a string of length `width`. Padding is done using the specified `fillchar`.",
            "lower" : "Returns a copy of the string converted to lowercase.",
            "lstrip" : "Returns a copy of the string with leading whitespace removed.",
            "maketrans" : "Returns a translation table usable for `translate()`.",
            "partition" : "Returns a tuple containing the part before the first occurrence of `sep`, the separator itself, and the part after the separator.",
            "removeprefix" : "Returns a copy of the string with the specified prefix removed.",
            "removesuffix" : "Returns a copy of the string with the specified suffix removed.",
            "replace" : "Returns a copy of the string with all occurrences of `old` replaced by `new`. If the optional argument `count` is given, only the first `count` occurrences are replaced.",
            "rfind" : "Returns the highest index in the string where substring `sub` is found, such that `sub` is contained within `s[start:end]`. Returns -1 on failure.",
            "rindex" : "Like `rfind()` but raises `ValueError` when the substring is not found.",
            "rjust" : "Returns the string right-justified in a string of length `width`. Padding is done using the specified `fillchar`.",
            "rpartition" : "Returns a tuple containing the part before the last occurrence of `sep`, the separator itself, and the part after the separator.",
            "rsplit" : "Returns a list of the words in the string, using `sep` as the delimiter string, starting from the right.",
            "rstrip" : "Returns a copy of the string with trailing whitespace removed.",
            "split" : "Returns a list of the words in the string, using `sep` as the delimiter string.",
            "splitlines" : "Returns a list of the lines in the string, breaking at line boundaries.",
            "startswith" : "Returns `True` if the string starts with the specified prefix.",
            "strip" : "Returns a copy of the string with leading and trailing whitespace removed.",
            "swapcase" : "Returns a copy of the string with uppercase characters converted to lowercase and vice versa.",
            "title" : "Returns a version of the string where each word is titlecased.",
            "translate" : "Returns a copy of the string where each character has been mapped through the given translation table.",
            "upper" : "Returns a copy of the string converted to uppercase.",
            "zfill" : "Returns the numeric string left filled with zeros in a string of length `width`."
}

def getMethods():
    with open('AllStringMethods.txt', 'w') as file:
        file.writelines("# All string methods showcase by Erickson Dela Soledad\n# All string methods (alphabetically)\n\n")
        for method in zip(z := [x for x in dir(str) if "__" not in x], range(len(z))):
            file.writelines(f"{method[1]+1}: {method[0]} \n")

getMethods()

# create separate files for each methods
def create_files():
    for method in [x for x in dir(str) if "__" not in x]:
        with open(f"{method}.py", 'w') as file:
            file.writelines(f"# All string methods showcase by Erickson Dela Soledad\n\n")
            file.writelines(f"# {method.capitalize()} - {methodss[method]} \n\n")
            file.writelines(f"string_input = \"Hello World\"\n")
            file.writelines(f"print(string_input.{method}())")
            
create_files()