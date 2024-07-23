def encode(password):
    new_string=''
    for i in password:
        new_string+=str(int(i)+3)
    return new_string

def decode(password):
    pass