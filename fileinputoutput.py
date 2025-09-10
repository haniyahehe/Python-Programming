filename = "sample_file.txt"

with open(filename, "w") as file:
    file.write("This is the first line.\n")
    file.write("Learning Python is fun!\n")

with open(filename, "r") as file:
    content = file.read()
print("File content after writing:")
print(content)

with open(filename, "a") as file:
    file.write("This is a new line added later.\n")
    file.write("Python file I/O is easy!\n")

with open(filename, "r") as file:
    updated_content = file.read()
print("File content after appending:")
print(updated_content)