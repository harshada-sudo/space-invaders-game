#space invaders game
import turtle # module
import math
import random
import winsound

#setup the screen
wn = turtle.Screen()
wn.title("Space Invaders Game")
wn.bgcolor("black")
wn.setup(width =700, height =700)

#draw border
border_pen = turtle.Turtle()
border_pen.speed() #speed of drawing
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

#set score to 0
score = 0

#draw score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.setposition(0,310)
pen.write("Score : 0",align='center',font=('times new roman',15,'normal'))
pen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.penup()
player.setposition(0,-250)
player.setheading(90)

#create enemy
number_of_enemies = 5
enemies = []
for count in range(number_of_enemies):
    enemies.append(turtle.Turtle()) 

for enemy in enemies: 
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

#create player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(stretch_len=0.5,stretch_wid=0.5)
bullet.hideturtle()


bullet_speed = 20
enemy_speed = 2
player_speed = 15

#define bullet states
#ready - ready to fire
#fire - bullet is fired
bullet_state = 'ready'

#define functions
#move player left
def move_left():
    x = player.xcor()
    x -= player_speed

    #boundry checking
    if x < -280:
        x = -280
    player.setx(x)

#move player right
def move_right():
    x = player.xcor()
    x += player_speed

    #boundry checking
    if x > 280:
        x = 280
    player.setx(x)

#fire bullet
def fire_bullet():
    global bullet_state

    #move bullet to just above the player
    if bullet_state == 'ready':
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#collision between enemy and bullet
def is_collision(self,other):
    a = self.xcor() - other.xcor()
    b = self.ycor() - other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2))

    if distance < 15 :
        return True
    else:
        return False

#keyboard binding
turtle.listen()
turtle.onkeypress(move_left,"Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")
#main game loop
while True:
    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        #move enemy back and down
        if enemy.xcor() > 280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -=40
                e.sety(y)
            #change enemy direction
            enemy_speed *= -1    

        if enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemy_speed *= -1

        if is_collision(bullet,enemy):
            winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
            #reset the bullet
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0,-400)

            #reset the enemy
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x,y)

            #update score 
            score += 1
            pen.clear()
            pen.write("Score : {}".format(score),align='center',font=('times new roman',15,'normal'))
                    
        if is_collision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            break

    #move the bullet
    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    #check bullet reached to top border
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = 'ready'

delay = input("press enter to finish")
