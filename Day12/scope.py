enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside the functionL {enemies}")

# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

# Will print 2
drink_potion()

# This cannot access the variable created inside the drink_potion function
#print(potion_strength)


# Global scope
player_health = 10

