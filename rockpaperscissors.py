import random
import sys

def computerinput(list):
    while True:
        playertype = input('Type computer to face a computer and player to face another player:').lower()
        if playertype == 'computer' or playertype == 'player':
            break
        else:
            print('Please try again.')
    if playertype == 'player':
        list.append(getinput(2))
        return
    randomcomputerchoice = random.choice(['rock', 'paper', 'scissors'])
    print('The computer chose {}!'.format(randomcomputerchoice))
    list.append(randomcomputerchoice)
    return

def getinput(player):
    while True:
        try:
            playerrawinput = input('Player {}, please choose rock, paper, or scissors:'.format(player))
            playerinput = playerrawinput.lower()
            if playerinput == 'rock' or playerinput == 'paper' or playerinput == 'scissors':
                break
            else:
                print('There was an error. Please try again.')
                continue
        except ValueError:
            print('Try again.')
            continue
    return playerinput

def compareinputs(list):
    if list[0] == 'rock':
        if list[1] =='rock':
            winner = 'It\'s a tie!'
        elif list[1] == 'paper':
            winner = 'Player 2 wins!'
        elif list[1] == 'scissors':
            winner = 'Player 1 wins!'
    elif list[0] == 'paper':
        if list[1] =='rock':
            winner = 'Player 1 wins!'
        elif list[1] == 'paper':
            winner = 'It\'s a tie!'
        elif list[1] == 'scissors':
            winner = 'Player 2 wins!'
    elif list[0] == 'scissors':
        if list[1] =='rock':
            winner = 'Player 2 wins!'
        elif list[1] == 'paper':
            winner = 'Player 1 wins!'
        elif list[1] == 'scissors':
            winner = 'It\'s a tie!'
    return winner

playagain = True
def main():
    win = False
    playagain = False
    playerinputs = []
    playerinputs.append(getinput(1))
    computerinput(playerinputs)
    winner = compareinputs(playerinputs)
    while True:
        if 'Player 1' in winner:
            playerwinner = playerinputs[0]
            playerloser = playerinputs[1]
            win = True
        elif 'Player 2' in winner:
            playerwinner = playerinputs[1]
            playerloser = playerinputs[0]
            win = True
        while True:
            if win:
                playagain = input('{} beats {}! {} \nWould you like to play again? Type yes or no:'.format(playerwinner.title(), playerloser, winner)).lower()
            else:
                playagain = input('{} \nWould you like to play again? Type yes or no:'.format(winner)).lower()
            if playagain == 'no':
                print('Thanks for playing! The program has ended.')
                sys.exit()
            elif playagain == 'yes': 
                playagain = True
                return
            else:
                print('Invalid input, please try again!')
                continue
while playagain == True:
    main()
