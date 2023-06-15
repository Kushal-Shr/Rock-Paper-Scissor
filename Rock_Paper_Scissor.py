import random

print('\n---Welcome to Rock Paper Scissor game---\n')

def game():
    chose_lst = []
    choices = ['Rock', 'Paper', 'Scissor']
    computer_choice_lst = random.choices(choices)
    computer_choice = computer_choice_lst[0]

    print(f'You can choose:\n1 --> Rock\n2 --> Paper\n3 --> Scissor\n')

    choice = int(input('Enter your choice 1, 2 or 3 :'))

    print(f'\nYou chose : {choices[choice - 1]}')
    print(f'Computer chose : {computer_choice}\n')

    draw = [[choices[0], choices[0]], [choices[1], choices[1]], [choices[2], choices[2]]]
    win = [[choices[0], choices[2]], [choices[1], choices[0]], [choices[2], choices[1]]]

    chose_lst.append(choices[choice - 1])
    chose_lst.append(computer_choice)

    if chose_lst in draw:
        print('The game is drawn...')

    elif chose_lst in win:
        print('You won the game...')

    else:
        print('You lost the game...')

game()

while True:
    print('\nSelect\n1 --> Continue the game\n2 --> Exit...')
    continue_or_exit = int(input('\nEnter 1 to Continue the game or 2 to Exit :'))

    if continue_or_exit == 1:
        game()

    elif continue_or_exit == 2:
        print('Thanks For Playing...')
        break