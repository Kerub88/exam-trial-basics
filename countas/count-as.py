    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

def count_as(file_name):
    fr = open(file_name, "r")
    text = fr.read()

    letter_a = 0
    for letter in file_name:
        if letter == "a":
            letter += 1
    return letter_a


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
