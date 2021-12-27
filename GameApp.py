# Implement these features:
# A class, Enemy, that starts with three lives.
# A method to attack the enemy and reduce its life count by one.
# A method to check the enemy’s life count and either report when the enemy loses a life, or report that the enemy is dead.
# Generate three instances of the enemy in the program and attack the enemies to reduce their life count.

# class Enemy
class Enemy:
    lives = 3
    def __init__ (self):
        self.lives = lives
    def attack(self):
        while True:
            play = input('Press return key to attack.')
            if play == '':
                break
        r = random.randint(0,1)
        if r == 1:
            print("Ouch! That's a hit!")
            self.lives = self.lives - 1
            print(f'This enemy has {self.lives} lives left')
            return self.lives
        else:
            print("Haha!  Missed!  Try again.")
    def checkLife(self):
        if self.lives == 0:
            print("This enemy is dead!")
            return False

# intro
import random
print('''In this game you will confront three enemies, each with three lives.
Your task is to eliminate each enemy to win the game.
You will begin with 9 lives.  Each time you miss an enemy, you will lose a life.''')
player_lives = 9
for i in range(3):
    print('Here comes enemy number ' + str(i + 1))
    lives = Enemy.lives
    enemy = Enemy()
    while True:
        enemy.attack()
        player_lives -= 1
        enemy.checkLife()
print("Well done, you have defeated three enemies.  Now take a break and relax!")