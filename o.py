import random
import time

rock = 1
paper = 2
scissor = 3

name = {rock: "Rock", paper: "Paper", scissor:"Scissor"}
rule = {rock:scissor, paper:rock, scissor:paper}

play_score = 0
com_score = 0
def start():
    print ("let's play scissor rock and paper")
    while game():
        pass
    scores()

def game():
    player = move()
    com = random.randint(1,3)
    result(player,com)
    return play_again()

def move():
    while True:
        print
        player = input('1.Rock \n2.Paper \n3.Scissor \nMake a move : ')
        try:
            player = int(player);
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ('Oops I didn\'t understand your input, input 1,2,or 3')

def result(player, com):
    print('1...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('3...')
    time.sleep(0.5)
    print("computer threw {0}".format(name[com]))
    global play_score, com_score
    if player == com:
        print('tie game')
    else:
        if rule[player] ==com:
            print ('your victory')
            play_score += 1
        else:
            print('com laughing at you!')
            com_score += 1

def play_again():
    answer = input('play again? : ')
    if answer in ('y','Y'):
        return answer
    else:
        print('see you again')

def scores():
    global play_score, com_score
    print('High SCore')
    print("Player score "+str(play_score))
    print("computer score "+str(com_score))

if __name__ == '__main__':
    start()
