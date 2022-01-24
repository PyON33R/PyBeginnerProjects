from random import choice


def play():
    abbreviations = {
        'r' : 'rock',
        'p' : 'paper',
        's' : 'scissor'
    }
    user_choice = input("(r => rock, p => paper, s => scissor) : ")
    computer_choice = choice(['r', 'p', 's'])
    
    winner = win_logic(user_choice, computer_choice)

    if winner:
        print(f"You Picked: {abbreviations[user_choice]}, Computer Picked: {abbreviations[computer_choice]}")
        return f"Winner is: {winner}"
    else:
        play()
    



def win_logic(user_choice, computer_choice):
    # r > s, s > p, p > r

    win_logic_dict = {
        # "this" (cuts) "that" => this : that
        'r' : 's',
        's' : 'p',
        'p' : 'r'
    }

    if user_choice == computer_choice:
        return 'tie'
    elif win_logic_dict.get(user_choice, 'not_exist') == computer_choice:
        return 'user'
    elif win_logic_dict.get(computer_choice, 'not_exist') == user_choice:
        return 'computer'
    else:
        return None
    
print(play())



