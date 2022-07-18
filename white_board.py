# Remove vowels
# Write a function that will remove all vowels from a given string. 
# The function should return a string.
# Example:

# Input: ‘Joel’
# Output: ‘Jl’


def func(word):
    newvalue = list(word)
    vowel = ['a','e','i','o', 'u']
    for x in newvalue:
        if x in vowel:
            newvalue = word.replace(word, "", 5)
            return word

print(func('Joel'))