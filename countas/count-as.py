    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.
from os import path


def count_as(file_name):
    try:
        fr = open(file_name, "r")
        text = fr.read()
        letter_a = 1
        for letter in text:
            if letter == "a":
                letter_a += 1
        return letter_a
    except FileNotFoundError:
        return "0"

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
