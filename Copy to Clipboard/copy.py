import pyperclip, glob, os


# In this case, my complicated WoW password
text_to_copy = None

# Finds the txt file containing my password, and copies to keyboard.
for file in glob.glob("*.txt"):
    with open(file, 'r') as open_file:
        text_to_copy = open_file.read()
        pyperclip.copy(text_to_copy)
    break

