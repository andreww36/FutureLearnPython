# GAME BRANCH
# I'm trying to work on a game branch...
# Implement these features:
# A class, Enemy, that starts with three lives.
# A method to attack the enemy and reduce its life count by one.
# A method to check the enemy’s life count and either report when the enemy loses a life, or report that the enemy is dead.
# Generate three instances of the enemy in the program and attack the enemies to reduce their life count

# class Enemy
class Enemy:
    lives = 3
    def __init__ (self):
        self.lives = lives
    def attack(self):
        print("Ouch! That's a hit!")
        self.lives = self.lives - 1
        print(f'You have {self.lives} lives left')
        return self.lives
    def checkLife(self):
        if self.lives == 0:
            print("This enemy is dead!")

# intro
print('In this game you will confront three enemies, each with three lives.\nYour task is to eliminate each enemy to win the game.\n')
for i in range(3):
    print('Here comes enemy number ' + str(i + 1))
    lives = Enemy.lives
    enemy = Enemy()
    for i in range(3):
        enemy.attack()
        enemy.checkLife()
print("Well done, you have defeated three enemies.  Now take a break and relax!")