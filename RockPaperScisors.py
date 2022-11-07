game = True

class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0

    def counter(self):
        self.points += 1
        print(f'{self.name} Twój wynik to: {self.points}')


def winner(player1symbol, player2symbol, player1, player2):

    if player1symbol.upper() == 'ROCK' and player2symbol.upper() == 'ROCK':
        print('DRAW!')
    elif player1symbol.upper() == 'PAPER' and player2symbol.upper() == 'PAPER':
        print('DRAW!')
    elif player1symbol.upper() == 'SCISORS' and player2symbol.upper() == 'SCISORS':
        print('DRAW!')
    elif player1symbol.upper() == 'ROCK' and player2symbol.upper() == 'SCISORS':
        print(f'{player1.name} win!')
        player1.counter()
    elif player1symbol.upper() == 'PAPER' and player2symbol.upper() == 'ROCK':
        print(f'{player1.name} win!')
        player1.counter()
    elif player1symbol.upper() == 'SCISORS' and player2symbol.upper() == 'PAPER':
        print(f'{player1.name} win!')
        player1.counter()
    elif player2symbol.upper() == 'ROCK' and player1symbol.upper() == 'SCISORS':
        print(f'{player2.name} win!')
        player2.counter()
    elif player2symbol.upper() == 'PAPER' and player1symbol.upper() == 'ROCK':
        print(f'{player2.name} win!')
        player2.counter()
    elif player2symbol.upper() == 'SCISORS' and player1symbol.upper() == 'PAPER':
        print(f'{player2.name} win!')
        player2.counter()


print('Welcome in Rock Paper Scisors game!')

player1 = Player(name=input('Podaj imię pierwszego gracza: '))

player2 = Player(name=input('Podaj imię drugiego gracza: '))


while game:

    player1symbol = input(f'{player1.name} ROCK, PAPER or SCISORS? ')
    player2symbol = input(f'{player2.name} ROCK, PAPER or SCISORS? ')
    winner(player1symbol, player2symbol, player1, player2)

    next_game = input('Again? (Y or N)')
    if next_game.upper() == 'Y':
        continue
    elif next_game.upper() == 'N':
        break
    else:
        next_game = input('Y or N')
        continue