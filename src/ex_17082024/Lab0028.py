# Escape Sequence
print("Hello World")
print("Hello\nWorld")   # \n --> new line
print("Hello\tWorld")   # \t --> tab line
print("Hello\bWorld")   # \b --> backspace

# dir = 'C:\Users\n.txt'
# dir = "C:\Users\n.txt"
# where this r concept will be used?
# Automation API, Web Automation, file_path = r concept
dir = r"C:\Users\n.txt"
dir2 = r'C:\Users\n.txt'
print(dir)
print(dir2)

name = 'pramod\'utta'   # \ --> escape sequence
name2 = "Pramod'utta"
print(name)
print(name2)