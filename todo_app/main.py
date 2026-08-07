import random

from parsers import parse

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input(
    "Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)"
)

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(int(parsed["lower_bound"]), int(parsed["upper_bound"]))

print(rand)
