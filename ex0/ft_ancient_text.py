import typing, io, sys

print("=== Cyber Archives Recovery ===")

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
except:
    PermissionError
    print(f"Error: Access to '{sys.argv[1]}' is not allowed")
    sys.exit()
print("---------")
print(f.read())
print("---------")

try:
    f.close()
    print(f"File '{sys.argv[1]}' closed.")
except FileNotFoundError:
    print(f"Error: Unabe to close '{sys.argv[1]}' file")