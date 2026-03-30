capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# Print Lille
#print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 3,     
        "cities": ["Stuttgart", "Berlin"]
    }
}

print(travel_log["Germany"]["cities"][0])


