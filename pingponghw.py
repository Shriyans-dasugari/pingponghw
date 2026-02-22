import pgzrun
WIDTH = 800
HEIGHT = 500

ballimage = Actor('ball.png')
score = 0
ballimage.pos = (100,250)
bat = Rect((750,200),(20,60))
speedx = 6
speedy = 3
def update():
    global speedx,speedy
    ballimage.x += speedx
    ballimage.y += speedy   
    if keyboard.down:
        bat.y += 5
    if keyboard.up:
        bat.y -= 5
    if ballimage.bottom > HEIGHT:
        speedy = -speedy
    if ballimage.top < 0:
        speedy = -speedy
    if ballimage.right > WIDTH:
        exit()
    if ballimage.left < 0:
        speedx = -speedx
    if ballimage.colliderect(bat):
        global score
        speedx = -speedx
        score += 10
    
def draw():
    screen.fill('black')
    ballimage.draw()
    screen.draw.filled_rect(bat,'red')
    screen.draw.text('your score is '+ str(score),(300,50),color = "blue", fontsize = 50)



pgzrun.go()
