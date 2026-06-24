print("=== Cyber Archives Security ===\n")
def secure_archive(filename: str, action: str = "r", content: str ="")->tuple:
    if action != "r" or action != "w":
        return (False, "Invalid usage of function")
    if action == 'r':
        try:
            print(f"Using 'secure_archive to read from {filename} file:")
            with open(filename, "r") as file:
                contenu = file.read()
                return (True, contenu)
        except FileNotFoundError:
            return (False, f"[Errno 2] No such file or directory: '{filename}'")
        except PermissionError:
            return (False, f"[Errno 13] Permission denied: '{filename}'")
    elif action == 'w':
        try:
            print(f"Using 'secure_archive' to write previous content to a new file")
            with open(filename) as file:
                contenu = file.read()
                with open("file", "w") as new_file:
                    if content == "":
                        new_file.write(contenu)
                    else:
                        new_file.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, f"{e}") 
    
print(secure_archive("test.txt", "a", "wessd"))