import random
import string


class Password:
    def __init__(self, difficulty, length):
        self.difficulty = difficulty
        self.length = length

    def generator(self):
        if self.difficulty == 'EASY':
            characters = string.ascii_lowercase
            password = ''.join(random.choice(characters) for i in range(self.length))

        elif self.difficulty == 'MEDIUM':
            characters = string.ascii_letters + string.digits
            password = ''.join(random.choice(characters) for i in range(self.length))

        elif self.difficulty == 'HARD':
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(self.length))

        return print(password)


print('Password generator')

while True:

    password = Password((input('Choose difficulty of your password [easy, medium, hard]: ')).upper(),
                    int(input("What's length?")))
    password.generator()
    next_password = (input('Do you want to generate next password? [Y or N]')).upper()
    if next_password == 'Y':
        continue
    elif next_password == 'N':
        break
    else:
        next_password = input('Y or N?')









