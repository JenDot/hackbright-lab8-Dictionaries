"""Restaurant rating lister.
Your job is to write a program named ratings.py that:

    Reads the ratings from the file

    Stores them in a dictionary

    And finally, spits out the ratings in alphabetical order by restaurant

Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.
"""


# define function
def restaurant(filename):
    # open scores.txt file to get data to add to dictionary
    new_file = open("scores.txt")

    # create empty dictionary to store data
    rest_dict = {}

    # loop through scores.txt to view all restaurants
    for line in new_file:
        # give 2 variables to store the 2 items from each list
        # rstrip = remove chars from rt end; split method to split by colon
        rest_name, score = line.rstrip().split(":")
        # key=rest_name, value=score
        rest_dict[rest_name] = score
        name = sorted(rest_dict)  # creates list of items from dictionary
        for idx in name:
            rating = rest_dict.get(name[idx])  # gets value of "name" item
            print(f"{name} rating is at {rating}")
#   print(name)

    # use list items to refer to dictionary and create an f string to print key and value
    # for item in sorted list:
    #    get item name
    #    look up item in dictionary to get value of item from sorted list--> rest_dict.get(name)
    #    print(f"{item from sorted list} rating is {value from dictionary}")


# sort the dictionary items by key (restaurant name)
# return filled, sorted dictionary
# print(rest_dict)
# call function
restaurant("scores.txt")


"""Big Bean Shack is rated at 3.
Chip Shop is rated at 3.
Diagon Alley cafe is rated at 2.
Eternelle's Elixir of Refreshment is rated at 5.
Florean Fortescue's Ice Cream Parlour is rated at 4.
Jellied Eel Shop is rated at 3.
Luchino Caffe is rated at 1.
Ministry Munchies is rated at 1.
The Bear & Staff is rated at 2.
The Club is rated at 2.
The Porcupine is rated at 5.
The Tavern is rated at 3.
"""

# https://docs.python.org/3.9/library/functions.html?highlight=sorted#sorted
