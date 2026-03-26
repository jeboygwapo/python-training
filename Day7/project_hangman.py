import random

word_list = ["dog", "cat", "mouse", "tite"]
random_word = word_list[random.randint(0,len(word_list)-1)]
random_word_list = list(random_word)
current_guess = []
for current_guess_counter in range(0,len(random_word)):
    current_guess.append("_")

current_guess_str = "".join(current_guess)
lifeline = 6
#print(random_word)

print(f"Word to guess: {current_guess_str}")

while lifeline > 0 :
    if current_guess_str == random_word:
        print("-------------------------------------------------------------------")
        print("Congrats! YOU WIN")
        break
    else: 
        user_guess = input("Enter a letter: ")
        if user_guess in random_word_list:
            for x in range(0,len(random_word)):
                if user_guess is random_word_list[x]:
                    current_guess[x] = user_guess
                    current_guess_str = "".join(current_guess)
            print("-------------------------------------------------------------------\nCorrect")
            print(f"Word to guess: {current_guess_str}")
            print(f"Current lifeline: {lifeline}/6")
        else:
            lifeline -= 1
            print("-------------------------------------------------------------------")
            print(f"You guessed {user_guess}, that's not in the word. You lose a life")
            print(f"Word to guess: {current_guess_str}")
            print(f"Current lifeline: {lifeline}/6")
            if lifeline == 0:
                print("Game Over")
                break
