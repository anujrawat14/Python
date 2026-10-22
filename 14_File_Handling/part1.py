# ==============================
# File Handling using open()
# ==============================

# Syntax:
# open("filename", "mode")


# File Opening Modes:
# "r"  -> Read; error if the file doesn't exist
# "w"  -> Write; overwrites content or creates a file
# "a"  -> Append; adds content at the end
# "x"  -> Create a new file; error if it already exists
# "r+" -> Read and write without truncating initially
# "b"  -> Binary mode modifier, e.g. "rb"
# "t"  -> Text mode modifier; default mode


# Open the file in write mode
file = open("youtube.txt", "w")

try:
    # Write content into the file
    file.write("chai aur code")

finally:
    # Ensure the file is closed
    # even if an exception occurs
    file.close()
