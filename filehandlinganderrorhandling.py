# File Handling
# Opening A File
file = open("sample.txt", "w")  # Opening in write mode
print("File opened successfully for writing.")
file.close()

# Writing To A File
file = open("sample.txt", "w")  # 'w' mode will overwrite if file exists
file.write("This is the first line.\n")
file.write("This is the second line.\n")
print("Data written to file.")
file.close()

# Reading A File
file = open("sample.txt", "r")  # Open in read mode
content = file.read()
print("Reading file content:")
print(content)
file.close()

# Closing A File
file = open("sample.txt", "r")
print("File is open.")
file.close()
print("File is closed.")

# Using With Statement
with open("sample.txt", "r") as file:
    content = file.read()
    print("📄 File content using 'with':")
    print(content)
# File is automatically closed here
print("✅ File closed automatically after 'with' block.")


# Error Handling
# Basic Try-Except Block
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a valid number.")