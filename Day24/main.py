# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Will change all in the text file
# "w" stands for write
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")


# Will add the text in the end of the file
# "a" stands for append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# if a file doesn't exist, it will create a new file
with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")