#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    for names in file:
        names_list.append((names.strip()))

for name in names_list:
    personalized_letter = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}-letter.txt", mode="w") as file:
        file.write(personalized_letter)
