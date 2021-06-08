def remove_exclamation_marks(s):
    for char in s:
        if char == "!":
            s.replace(char, "")
    return print(s)

remove_exclamation_marks("!!!!!!!!! HELOOO !!!!!!!!!!!!!")
