import random

random.seed()

def password_Generator(length):
    possible_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '$', '%', '^', '&', '*', '(', ')', '#', '@', '<', '>', '|', '{', '}',]
    generated_password = []
    for i in range(length): # loops for the desired password length
        rand_num = random.random() # gets a random number between 0 and 1
        if rand_num < 0.5: # checks if its less than 0.5 to append upper case or lower case 
            generated_password.append(random.choice(possible_characters))
        else:
            generated_password.append(random.choice(possible_characters).upper())
    generated_password = "".join(generated_password) # joins the list into a string

    return generated_password
    

print(password_Generator(7))
