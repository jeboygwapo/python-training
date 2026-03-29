# def greet():
#     print("Hello")
#     print("Good day!")
#     print("How are you?")
#
# greet()
#
# # Functions that allows input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#
# name = input("Enter your name: ")
#  greet_with_name(name)

# Functions for more 1 input
# def greet_with(name, location):
#     print(f"Hello {name}! How's the weather in {location}?")
#
# greet_with(location = "Riyadh", 
#            name     = "Jayvee"
#            )


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = []
word = input("Enter word: ")
word_list = list(word)
shift = int(input("Enter shift: "))
print(word_list)

ctr = 0
for x in word_list:
    position = alphabet.index(x)
    z = shift + position
    if z > len(alphabet)-1:
        z = z % len(alphabet)
        word_list[ctr] = alphabet[z]
    else:
        word_list[ctr] = alphabet[z]
    ctr += 1

output = "".join(word_list)
print(output)
#    if 26 letters

