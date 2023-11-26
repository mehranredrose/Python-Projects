from random import choice
from config import GAME_CHOICES, RULES


def get_user_choice():
    """
    get and validate player input, in recursive
    """

    user_input = input('Enter your choice please (r, p, s): ')
    if user_input not in GAME_CHOICES:
        print('Oops!! wrong choice, try again ...')
        return get_user_choice()
    return user_input


def get_system_choice():
    """
    random choice from GAME_CHOICES
    """
    return choice(GAME_CHOICES)


def find_winner(user, system):
    """
    returning winner on user and system choices by 
    giving a sort tuple of user and system choices to the RULES dictionary
    and if they had same choices return draw
    """
    match = {user, system}
    if len(match) == 1:
        return 'draw'
    return RULES[tuple(sorted(match))]


def play():
    """
    main playground handler
    """
    result = {'user': 0, 'system': 0}

    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)

        if winner != 'draw':
            if winner == user_choice:
                result['user'] += 1
            else:
                result['system'] += 1
        print(
            f'User:{user_choice}  System:{system_choice} Result:{winner} \nScores =>[User: {result["user"]}, System:{result["system"]}]')

    if result['system'] == 3:
        print('-------------> You Lost! <-------------')
    else:
        print('-------------> You Won! <-------------')

    play_again = input('Do you want to play again (y/n)? ')
    if play_again == 'y':
        play()


if __name__ == '__main__':
    play()
