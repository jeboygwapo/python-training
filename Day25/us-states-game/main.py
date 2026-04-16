import pandas as pd
import turtle as t

# Constants
IMAGE = "blank_states_img.gif"
FONT = ("Courier", 12, "normal")  # Smaller font usually fits better on the map

# Screen Setup
screen = t.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
t.shape(IMAGE)

# Data Setup
data = pd.read_csv("50_states.csv")
data_indexed = data.set_index("state")
# Create lowercase dictionary for easy lookup
state_dict = {k.lower(): v for k, v in data_indexed.to_dict(orient="index").items()}

# Turtle for writing state names on the map
writer = t.Turtle()
writer.hideturtle()
writer.penup()

correct_guesses = []

while len(correct_guesses) < 50:
    # Get user input
    answer_state = screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # Check if user clicked cancel or wants to exit
    if answer_state is None or answer_state.lower() == "exit":
        break

    answer_lower = answer_state.lower()

    # Check if answer is correct and not already guessed
    if answer_lower in state_dict and answer_lower not in correct_guesses:
        correct_guesses.append(answer_lower)

        # Get coordinates from our dictionary
        state_data = state_dict[answer_lower]
        x = int(state_data["x"])
        y = int(state_data["y"])

        # Move writer to the state's location and write the name
        writer.goto(x, y)
        # Use .title() so "alabama" appears as "Alabama" on the map
        writer.write(answer_lower.title(), align="center", font=FONT)

