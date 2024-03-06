# Author: Ethan Jossi
# This is the Context Free Grammar portion of Project 1
# For an outline and a list of rules on how the idea of 
# Context free grammar works, check the documentation
# of Project 1.

import my_rng
import csv
import time

# These are the keys for grammar. It's a tuple because it's not meant
# to be modified. It is used in the grammar_from_file function.
possible_grammar_keys = []

def new_grammar():
    """This function returns a new empty data structure for the grammar
    rules. The grammar data structure is a dictionary, where the keys are
    strings of the rules -- the variables. and the values are lists within
    lists. The outer list is a list of possible different sets of replacements
    for that key, and the inner list is a list of strings, representing
    variable and terminals."""
    return {}

def add_rule(grammar, variable, replacement):
    """This function takes in three parameters. Grammar (a dictionary of
    the rules and replacements), variable, which is the left hand side of
    the rules, and replacement, which is what variable can be replaced with.
    If variable is in grammar, it adds replacement to the list associated with
    variable. Else, it adds a new key entry with variable and list with replacement.
    This function modifies the given dictionary passed to it."""

    # If replacement is a tuple, cast it to a list
    if (isinstance(replacement, tuple)):
        replacement = list(replacement)

    # Add variable to the possibly keys if it's not already in it
    if variable not in possible_grammar_keys:
        possible_grammar_keys.append(variable)

    if grammar.get(variable, -1) == -1: # If variable not in dictionary, add it with its replacements
        grammar[variable] = [replacement]
    else: # Else, add the additional set of replacements to the existing variable.
        grammar[variable].append(replacement)


def generate(grammar):
    """This function generates text from a given grammar structure. It returns
    a list of strings."""
    output_list = [] # Final list of strings to output
    input_list = [] # List of strings that holds both variables and terminals
    input_list.append("Start") # Adds the variable "Start" to input_list

    # This while statement repeats the given code inside until the input_list is empty.
    # When input list is empty, we know that we have finished generating the grammar.
    while len(input_list) != 0:

        # if first element in input list is a variable, then replace with random from grammar 
        if input_list[0] in possible_grammar_keys:
            replacement_list = grammar[input_list[0]] # This is a list of lists
            replacement = my_rng.random_choice(replacement_list) # This is just a list

            # Remove the first element from the input_list and add the replacement list to the front of input list
            input_list.pop(0) 
            input_list = replacement + input_list
        
        # else add that element to output_list and remove that element from the input list
        else:
            word_to_add = input_list.pop(0)
            output_list.append(word_to_add)
    return output_list
        
def grammar_from_file(filename):
    """This function takes in the name of a csv file. It then creates a 
    grammar structure from that csv file. The data structure of grammar is 
    outline in the new_grammar() function."""

    # Create a reader object. This is a dictionary of the rows in the the csv file.
    reader = csv.DictReader(open(filename))
    grammar = {} # Create new grammar

    for row in reader:
        key = row["variable"]
        if key not in possible_grammar_keys:
            possible_grammar_keys.append(key)
    
    reader = csv.DictReader(open(filename))
    
    for row in reader:
        # Getting the keys and values from the file
        grammar_key = row["variable"]
        grammar_values = row["replacement"].split() # This is a string

        # Inserting the variables and replacements into the grammar dictionary
        if grammar.get(grammar_key, -1) == -1:
            grammar[grammar_key] = [grammar_values]
        else:
            grammar[grammar_key].append(grammar_values)
    return grammar

def print_word_list(word_list):
    """This is just a simple function that is designed to print a list of
    strings. It is most intentionally designed to be used with the 
    generate() function."""
    for word in word_list:
        print(word + " ", end="")
    print()

if __name__ == "__main__":
    my_rng.set_seed(int(time.time())) # Setting a random seed from the my_rng.py file
    filename = input("Please enter a filename to create a sequence: ") # Prompting the user for a filename

    # Creating a grammar structure, generating text from it, and printing that text as output.
    input_grammar = grammar_from_file(filename)
    final_output = generate(input_grammar)
    print_word_list(final_output)