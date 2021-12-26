# GAME BRANCH
# I'm trying to work on a game branch and have successfully created the branch.
# Implement these features:
# A class, Enemy, that starts with three lives.
# A method to attack the enemy and reduce its life count by one.
# A method to check the enemy’s life count and either report when the enemy loses a life, or report that the enemy is dead.
# Generate three instances of the enemy in the program and attack the enemies to reduce their life count

# class Enemy
class Enemy:
    lives = 3
    names = ["Snake eyes", "Shark face", "Bad Bandit", "Demon Dan", "Vicious Vic", "Nasty Nick"]
    def __init__ (self, name):
        self.lives = lives
        self.name = name
    def attack(self):
        print("Ouch! That's a hit!")
        self.lives = self.lives - 1
        print(f'You have {self.lives} lives left')
        return self.lives
    def checkLife(self):
        if self.lives == 0:
            print("This enemy is dead!")

# intro
print('In this game you will confront a random number of enemies, each with three lives.\nYour task is to eliminate each enemy to win the game.\n')
# generate enemies
import random
r = random.randint(3, 7)
for i in range(r):
    name = Enemy.names[i]
    print(f'Here comes enemy {name}')
    lives = Enemy.lives
    # name = Enemy()
    print(f'{name} has {lives} lives')

#     for i in range(3):
#         enemy.attack()
#         enemy.checkLife()
# print("Well done, you have defeated three enemies.  Now take a break and relax!")