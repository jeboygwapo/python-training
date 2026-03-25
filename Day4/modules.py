# Random library documentation for python
# https://docs.python.org/3/library/random.html

import random
import my_module
from test_module import favorite_word_module

# Random integer will be generated from 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# Call module from local machine
print(my_module.my_favourite_number)

# Call module from another folder
print(favorite_word_module.favorite_word)
