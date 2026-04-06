# Imports
import sys

# Constants (Global Variables)

# Class Definitions
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # Setup Default Value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Helper Functions


# Main Logic Function
def main():
    user_1 = User("001", "jeboy")
    user_2 = User("002", "juan")

    user_1.follow(user_2)
    print(user_1.followers)
    print(user_1.following)
    print(user_2.followers)
    print(user_2.following)



# Execution Guard
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited by user.")
        sys.exit(0)