#from game_data import data
from random import randint

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    }
]
def get_character():
    character = data([randint(0,2)])
    chr_name = character[0]
    chr_desc = character[2]
    chr_cntry = character[3]
    
    
    

def get_choice():
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

def main():
    get_main_character()
    get_choice()
if __name__ == "__main__":
    main()
# Printed strings 
Compare A: {name}, a {description}, from {country}.
vs
Against B: {name}, a {description}, from {country}.
input(Who has more followers? Type 'A' or 'B': )

clear screen every after guess


Once correct put the score above the Compare A 
You're right! Current score: 1.

Once you're wrong...
Sorry, that's wrong. Final score 3
