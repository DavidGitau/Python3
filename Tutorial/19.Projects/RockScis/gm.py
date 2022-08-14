import random

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper, or scissors?: ').lower()

    if player == computer:
        print(f'Computer: {computer}')
        print(f"Player: {player}")
        print('Tie!')
        
    elif player == 'rock':
        if computer == 'paper':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You lose!')
        if computer == 'scissors':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You win!')

    elif player == 'scissors':
        if computer == 'paper ':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You win!')
        if computer == 'rock':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You lose!')

    elif player == 'paper':
        if computer == 'rock':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You win!')
        if computer == 'scissors':
            print(f'Computer: {computer}')
            print(f"Player: {player}")
            print('You lose!')
    play_again = input('Play again? (yes/no): ').lower()

    if play_again != 'yes':
        break

print('Bye!')
    