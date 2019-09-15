import random
from random import randint
class Player(object):
    def __init__(self,dice):
        self.dice = dice

    def cast_dice(self):
        self.dice.toss(self)
        self.score = self.dice.get_points(self)

    def get_score(self):
        return self.score


class Dice(object):
    def toss(self):
        self.points = random.randint(1,6)
    
    def get_points(self):
        return self.points

'''class Game(object):
    def __init__(self,dice):
        self.dice = dice

    def sum_dice(self):
        self.dice.toss(self)
        self.restultA = self.dice.get_points(self)
        self.dice.toss(self)
        self.restultB = self.dice.get_points(self)
        self.results = self.restultA + self.restultB
        if self.results == 7:
            result = 'You won with '
        else:
            result = 'You lost with '
        print_words = result + str(self.results) + ' points.' 
        print(print_words)
        self.easteregg(1)
    
    def compare_dice(self, player1,player2):
        player1 = player1
        player2 = player2
        player1.cast_dice()
        player2.cast_dice()
        print(player1.score)
        score1 = player1.get_score()
        score2 = player2.get_score()
        difference = abs(score1 - score2)
        if score1 > score2:
            result = 'Player 1 has won with a difference of '
        elif score1 == score2:
            result = 'It is a tie with a difference of '
        else:
            result = 'Player 2 has won with a difference of '
        print_words = result + str(difference) + ' point(s)'
        print (print_words)
        self.easteregg(2)
    
    def easteregg(self,choice):
        decision = input('Do you want the Easter Egg? Yes or No.')
        if decision == 'Yes':
            number = choice
            if number == 1:
                print ('Shit')
            else:
                print ('Internationale')
        else:
            print('Bye')'''
        
class Sum(object):
    def __init__(self,dice):
        self.dice = dice

    def play(self):
        self.dice.toss(self)
        self.restultA = self.dice.get_points(self)
        self.dice.toss(self)
        self.restultB = self.dice.get_points(self)
        self.results = self.restultA + self.restultB
        if self.results == 7:
            result = 'You won with '
        else:
            result = 'You lost with '
        print_words = result + str(self.results) + ' points.' 
        print(print_words)

    def easteregg(self):
        print ('Shit')


class Compare(object):
    def __init__(self,dice,player1,player2):
        self.dice = dice
        self.player1 = player1
        self.player2 = player2

    def play(self):
        self.player1.cast_dice()
        self.player2.cast_dice()
        print(player1.score)
        score1 = self.player1.get_score()
        score2 = self.player2.get_score()
        difference = abs(score1 - score2)
        if score1 > score2:
            result = 'Player 1 has won with a difference of '
        elif score1 == score2:
            result = 'It is a tie with a difference of '
        else:
            result = 'Player 2 has won with a difference of '
        print_words = result + str(difference) + ' point(s)'
        print (print_words)
    
    def easteregg(self):
        print ('Internationale')


mydice = Dice
choice = int(input('Which game do you want to play, game 1 or game 2?'))
if choice == 1:
    mygame = Sum(mydice)
else:
    player1 = Player(mydice)
    player2 = Player(mydice)
    mygame = Compare(mydice,player1,player2)
mygame.play()
decision = input('Do you want the Easter Egg? Yes or No.')
if decision == 'Yes':
    mygame.easteregg()
else:
    print('Bye')
