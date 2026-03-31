def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Invalid input"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(input("Enter first name: "), input("Enter last name: "))

print(formated_string)

