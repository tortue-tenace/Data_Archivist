print("=== Cyber Archives Security ===\n")


def secure_archive(
    filename: str, action: str = "r", content: str = ""
) -> tuple[bool, str]:
    if action != "r" and action != "w":
        return (False, "Invalid usage of function")
    if action == "r":
        try:
            print(f"Using 'secure_archive' to read from '{filename}' file:")
            with open(filename, "r") as file:
                return (True, file.read())
        except OSError as e:
            return (False, f"{e}")
    try:
        print(f"Using 'secure_archive' to write content to '{filename}':")
        with open(filename, "w") as file:
            file.write(content)
        return (True, "Content successfully written to file")
    except OSError as e:
        return (False, f"{e}")


print(secure_archive("test.txt", "w", "wessd"))
print(secure_archive("test.txt", "r"))
