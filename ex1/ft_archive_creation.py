import sys, typing, io

if len(sys.argv) != 2:
    print("Usage: ft_ancient_text.py <path to file>")
    sys.exit()
path = sys.argv[1]
try:
    print(f"Accessing file '{sys.argv[1]}'")
    f = open(path, "r")
except FileNotFoundError:
    print(f"Error: Invalid path, couldn't open file")
    sys.exit()
except PermissionError:
    print(f"Error: Access to '{sys.argv[1]}' is not allowed")
    sys.exit()
print("---------")
print(f.read())
print("---------")
try:
    f.close()
    print(f"File '{sys.argv[1]}' closed.", end="\n\n")
except FileNotFoundError:
    print(f"Error: Unabe to close '{sys.argv[1]}' file")
print("Transform data:")
print("----------")
f = open(path, "r")
text = f.read()
new = ""
for i in range(len(text)):
    char = text[i]
    if char == "\n":
        new += "#"
        new += char
    elif i == len(text) - 1:
        new += char
        new += "#"
    else:
        new += char
print(new)
nfile_path = input("Enter new file name (or empty): ")
if (nfile_path == "empty"):
    print("Not saving data")
    sys.exit()
nfile = open(nfile_path, "w")
nfile.write(new)
print(f"Saving data to '{nfile_path}'\nData saved in file '{nfile_path}'.")
print("---------")