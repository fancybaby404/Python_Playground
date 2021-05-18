def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()

    return (f"{f_name} {l_name}")

print(format_name("omegalul","brotha"))

def hamburgerDisplay(hamb_str, bool):
    if hamb_str == "hamburger" and bool == True:
        return print("HAMBURGER!!!")
	
hamburgerDisplay("hamburger", True)