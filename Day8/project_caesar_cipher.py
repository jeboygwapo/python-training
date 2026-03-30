def encode_message(user_message, nbr_of_shift, alphabet):
    user_message_list = list(user_message)
    ctr = 0
    for x in user_message_list:
        if x in alphabet:
            position = alphabet.index(x)
            z = position + nbr_of_shift
            if z > len(alphabet)-1:
                z = z % len(alphabet)
                user_message_list[ctr] = alphabet[z]
            else:
                user_message_list[ctr] = alphabet[z]
        ctr += 1

    output = "".join(user_message_list)
    print(f"Here's the encoded result: {output}")

def decode_message(user_message, nbr_of_shift, alphabet):
    user_message_list = list(user_message)
    ctr = 0
    for x in user_message_list:
        if x in alphabet:
            position = alphabet.index(x)
            z = position - nbr_of_shift
            if z > len(alphabet)-1:
                z = z % len(alphabet)
                user_message_list[ctr] = alphabet[z]
            else:
                user_message_list[ctr] = alphabet[z]
        ctr += 1

    output = "".join(user_message_list)
    print(f"Here's the decoded result: {output}")

def go_again():
    while True:
        to_continue = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        if to_continue == "yes":
            return True
        elif to_continue == "no":
            return False
        else:
            print("Invalid input, please try again.\n")


session = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while session:
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if user_choice in ["encode", "decode"]:
        user_message = input("Type your message: ")
        
        shift_nbr = int(input("Type the shift number: "))
        if user_choice == "encode":
            encode_message(user_message = user_message,
                           nbr_of_shift = shift_nbr,
                           alphabet = alphabet
                           )
        else:
            decode_message(user_message = user_message,
                           nbr_of_shift = shift_nbr,
                           alphabet = alphabet
                           )
        session = go_again()    
    else:
        print("Invalid type, please try again.\n")


