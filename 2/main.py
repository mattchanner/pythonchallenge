def get_source():
    """ Returns the string to work with based on reading the contents of 
        the source.txt file in this directory. """
    fp = open("source.txt", "r")
    return fp.read()

source = get_source()

# dict(char, (count, first_index))
letters = {}

# go through each character in the source string and create a dictionary
# with the character as the key, and the value is a tuple containing the
# number of occurrences of the character, along with the index at which 
# it was first found in the source string.  The latter is used later to
# print out the rare characters in the order they were encountered
for index, char in enumerate(source):
    count = 0
    if char in letters:
        # get the current counter for this char along with its first 
        # index
        count, first_index = letters[char]
    else:
        first_index = index
    
    letters[char] = (count + 1, first_index)

rare_chars = list([[char, index] for char, (count, index) in letters.items() if count < 2])
sorted_rare_chars = sorted(rare_chars, key=lambda k: k[1])
print("".join([x[0] for x in sorted_rare_chars]))

# equality