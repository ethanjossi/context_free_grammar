# Author: Ethan Jossi
# This is the my_rng file for Project 1

import time

seed = 100
print_options = "A) Roll a dice\nB) Pick a random option\nC)quit\nEnter Choice:"

def set_seed(new_seed):
    """This function sets the global seed variable to a new seed inputted by the user.
    It also checks to make sure the new seed is within a valid range."""
    global seed
    if 1 <= new_seed <= (2**31-2):
        seed = new_seed
    else:
        print("INVALID SEED")

def next():
    """This function takes in no parameters and updates the global seed variable
    to a new "random" seed as given by the Park-Miller Algorithm."""
    global seed
    seed = ((7**5)*seed)%(2**31-1)
    return seed

def next_int(min, max):
    """This function takes in a min and max values, that are integers, and 
    returns a "random" number in between those min and max values, inclusive."""
    num_random = next()
    range = max - min + 1
    return num_random%range + min

def random_choice(seq):
    """This function takes in a list or tuple and returns a random element
    from the list or tuple. It uses the next_int() function."""
    element_random = next_int(0, len(seq)-1)
    return seq[element_random]

def rng_utility_option_A():
    # Grabs the max, min, and number of times inputs from the user
    max = input("Enter maximum number:")
    min = input("Enter minimum number:")
    times = input("Enter how many times:")

    # Checks to make sure that all the values the user entered are integers and that times > 1.
    if not(max.isdigit() and min.isdigit() and times.isdigit()):
        print("Inputs must be an integer and times must be greater than 0.")
        return

    # Sets max, min, and times all to integers
    max = int(max)
    min = int(min)
    times = int(times)

    # Checks to make sure max is greater than or equal to min
    if max < min:
        print("Max must be greater than or equal to min.")
        return
    
    # Prints the all the rolls with their corresponding random values.
    for i in range(1, times+1):
        print(f"roll {i}: {next_int(min, max)}")

def rng_utility_option_B():
    # Initializes the user_input variable and the user_input_list in which
    # all of the inputs are stored
    user_input = "Hi!!! My name is Ethan"
    user_input_list = []

    # While loop that accepts all the user's input and adds it to the list
    while user_input != "":
        user_input = input("Enter options or press enter to pick a random option:")
        if user_input != "":
            user_input_list.append(user_input)

    # Prints one of the inputs the user entered, randomly.
    print(random_choice(user_input_list))


# This line of code gives the illusion of a "random" seed. It isn't truly
# random, but it uses the computers clock to get a somewhat random number.
set_seed(int(time.time()))

# The "main" function, this is the user interface that lets the user choose an option
if __name__ == "__main__":
    user_input = ""
    while user_input != "C":
        print("RNG Utility:")
        user_input = input(print_options)
        if user_input == "A":
            rng_utility_option_A()
        elif user_input == "B":
            rng_utility_option_B()
        elif user_input == "C":
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
