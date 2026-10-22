# ==============================
# File Handling using with
# ==============================

# The with statement manages the file resource
# automatically and closes the file when the
# block exits, even if an exception occurs.


# Open and read a file safely
with open("chai.txt", "r", encoding="utf-8") as file:

    # Read the entire file content
    content = file.read()

    # Display the content
    print(content)

# The file is automatically closed here.
