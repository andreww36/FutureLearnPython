# Implement these features:
# A class, Enemy, that starts with three lives.
# A method to attack the enemy and reduce its life count by one.
# A method to check the enemy’s life count and either report when the enemy loses a life, or report that the enemy is dead.
# Generate three instances of the enemy in the program and attack the enemies to reduce their life count.

# class Enemy
class Enemy:
    lives = 3
    def attack(self):
        while True:
            play = input('Press return key to attack.')
            if play == '':
                break
        r = random.randint(0,1)
        if r == 1:
            print("Ouch! That's a hit!")
            self.lives -= 1
            print(f'This enemy has {self.lives} lives left')
            return 0
        else:
            print("Haha!  Missed!  Try again.")
    def checkLife(self):
        if self.lives == 0:
            print("This enemy is dead!")
            return False

class Player:
    player_lives = 9
    def __init__(self, name):
        self.name = name
    def hi_player(self):
        print(f'Hi {self.name}!')
    def checkPlayerLife(self):
        self.player_lives -= 1
        if self.lives == 0:
            print(f"Hard luck {self.name}, you've lost all your lives.  Better luck next time!")
            quit()
        else:
            print(f'You have {self.player_lives} lives left.')

# intro
import random
print('''In this game you will confront three enemies, each with three lives.
Your task is to eliminate each enemy to win the game.
You will begin with 9 lives.  Each time you miss an enemy, you will lose a life.''')
player = Player(input("OK, so what's your name? "))
player_lives = player.player_lives
print(str(player_lives)) # check line
player.hi_player()
for i in range(3):
    print('Here comes enemy number ' + str(i + 1))
    enemy = Enemy()
    lives = enemy.lives
    print(str(lives)) # check line
    play = True
    while play == True:
        enemy.attack()
        if enemy.attack() != 0:
            player_lives.checkPlayerLife()
        else:
            lives.checkLife()
            if lives.checkLife() == False:
                play = False

print("Well done, you have defeated three enemies.  Now take a break and relax!")