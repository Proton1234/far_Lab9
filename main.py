def encode(password):
    new_string=''
    for i in password:
        new_string+=str(int(i)+3)
    return new_string

def decode(password):
    new_string = ""
    for char in password:
        if char == "4":
            new_string += "1"
        elif char == "5":
            new_string += "2"
        elif char == "6":
            new_string += "3"
        elif char == "7":
            new_string += "4"
        elif char == "8":
            new_string += "5"
        elif char == "9":
            new_string += "6"
        elif char == "0":
            new_string += "7"
        elif char == "1":
            new_string += "8"
        elif char == "2":
            new_string += "9"
        elif char == "3":
            new_string += "0"
    return new_string