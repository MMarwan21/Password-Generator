import string
import random

def gen_pass(length=12):
    chars = input("please input what you want your password to include: ").replace(" ", "")
    if len(chars) < 9:
        chars = chars + string.ascii_letters

    rand_symb = input("Please enter a symbol you want to add to the password: ")
    if len(rand_symb) < 1:
        rand_symb = string.punctuation

    characters = chars + rand_symb
    # Guarantee at least one special character
    password = [random.choice(rand_symb)]
    # Fill the rest randomly
    password += [random.choice(characters) for i in range(length - 1)]
    # Shuffle to avoid predictable position
    random.shuffle(password)
    return (password)



new_pass = gen_pass(9)
print(f'Generated password: {new_pass}')