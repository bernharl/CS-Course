def stringrot(string):
    for char in string:
        yield chr(ord(char) + 13)
print("hello normal  world")
print("yes")
