def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase once
    combined_names = (name1 + name2).lower()
    
    # Count occurrences for "TRUE"
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e
    
    # Count occurrences for "LOVE"
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    # 'e' is already counted above
    love_score = l + o + v + e
    
    # Concatenate scores and print
    print(f"{true_score}{love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")
