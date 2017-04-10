def seconds(change_this):
    pass
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

# print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]

example_list = [6, 8, 3, 4, 5]

def seconds(the_list):
        new_list = []
        for element in range(0, len(the_list)):
            if element % 2 != 0:
                new_list.append(the_list[element])
        return new_list

print(seconds(example_list))
