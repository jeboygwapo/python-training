# Dictionaries
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

print(colours["pear"])

colours["grapes"] = "purple"

print(colours["grapes"])
print(colours)

# Edit an existing
colours["grapes"] = "not purple"
print(colours)

# Wiping an existing dictionary 
#colours = {}
#print(colours)

# Loop through the dictionary
for key in colours:
    print(key)
    print(colours[key])
