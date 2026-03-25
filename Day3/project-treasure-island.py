# ASCII ART HERE -- https://www.asciiart.eu/
print (r'''
             .-""-.
          _.->    <-._
       .-"   '-__-'   "-.
     ,"                  ",
   .'                      ',
  /    ___...------...___    \
 /_.-*"__...--------...__"*-._\
:_.-*"'  .*"*-.  .-*"*.  '"*-._;
;       /      ;:      \       :
;      ;    *  !!  *    :      :
:      :     .'  '.     ;      ;
 \      '-.-'      '-.-'      /
  \                          /
   '.                      .'
     *,      '-__-'      ,*
     /.'-_            _-'.'\
    /  "-_"*-.____.-*"_-"   \
   /      '"*-.___.-*'       \
  :    :        |        ;    ;
  |.--.;       *|        :.--.|
  (   ()        |        ()   )
   '--^_       *|        _^--'
      | "'*--.._I_..--*'" |
      | __..._  | _..._   |
     .'"      `"'"     ''"'.
     """""""""""""""""""""""
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the tresure.")

choice_one = input('You\'re at a cross road. '
                   'Where do you want to go?\n'
                   'Type "left" or "right"\n').lower()
if choice_one == "left":
    choice_two = input('You\'ve come to a lake. '
                       'There is an island in the middle of the lake.\n'
                       'Type "wait" to wait for a boat. '
                       'Type "swim" to swim across.\n').lower()
    if choice_two == "wait":
        choice_three = input('You arrive at the island unharmed. '
                             'There is a house with 3 doors.\n'
                             'One red, one yellow and one blue. '
                             'Which colour do you choose?\n').lower()
        match choice_three:
            case "red":
                print("Burned by fire. Game Over.")
            case "blue":
                print("Eaten by beasts. Game Over")
            case "yellow":
                print("Congratulations! You Win!")
            case _:
                print("Game Over")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
