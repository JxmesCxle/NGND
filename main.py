from multiprocessing import Process
from playsound import playsound
import turtle
import tkinter
import random
import subprocess
import sys
import winsound
import time
global bomba
global bomb1
#packet speed
pspeed = 2.1

#hacker speed
hspeed = 2

#distance for collison
dist = 30

#bomba = bomb activation
bomba = 0

lk=0
v=0
q=0
i=0
b=0
a=0

#gets systems screen resolution
#root = tkinter.Tk()
#width1 = root.winfo_screenwidth()
#height1 = root.winfo_screenheight()
#root.destroy()
#root.mainloop()



#window setup
win = turtle.Screen()
win.bgpic("space.gif")
win.title("Network Defender")
width1=700
height1=650
win.setup(width=width1 ,height=height1)

#registers pictures
win.register_shape("virus.gif")
win.register_shape("hacker.gif")
win.register_shape("bomb.gif")

#stops screen refreshing
win.tracer(0)


#for fullscreen
#win.setup(width=width1, height=height1)

#-----------------------------------------------------------------------------------------------------
###HACKER###
#gain ten points if touched

hack = turtle.Turtle()
hack.speed(0)
hack.shape("hacker.gif")
hack.color("blue")
hack.penup()


#increases size
hack.turtlesize(2)


#chooses new random x coordinate
hackx=random.randint(-320,320)

#chooses new random y coordinate
#affects time before it respawns
hacky=random.randint(350, 4000)
        

hack.goto(hackx, hacky)





#--------------------------------------------------------------------------------------------------------
###WORM###
#gain ten points if touched

worm = turtle.Turtle()
worm.speed(0)
worm.shape("square")
worm.color("orange")
worm.penup()


#increases size
worm.turtlesize(2)

worm.rt(45)

#chooses new random x coordinate
wormx=random.randint(-320,320)

#chooses new random y coordinate
#affects time before it respawns
wormy=random.randint(350, 7000)
        

worm.goto(wormx, wormy)

#------------------------------------------------------------------------------------------------------

###PACKETS###
#lose 10 points

packets = []
#add a buch of packets

while i < 30:
    packet=turtle.Turtle()
    packet.speed(0)
    packet.shape("circle")
    packet.color("pink")
    packet.penup()
    packet.goto(10, 300)
    packets.append(packet)
    i=i+1
    

    


#-------------------------------------------------------------------------------
###TROJAN###
#gain ten points if touched

trojan = turtle.Turtle()
trojan.speed(0)
trojan.shape("square")
trojan.color("yellow")
trojan.penup()


#increases size
trojan.turtlesize(2)

trojan.rt(90)

#chooses new random x coordinate
trojanx=random.randint(-320,320)

#chooses new random y coordinate
#affects time before it respawns
trojany=random.randint(350, 2100)
        

trojan.goto(trojanx, trojany)

#--------------------------------------------------------------------------------


###VIRUS###
#gain ten points if touched

virus = turtle.Turtle()
virus.speed(0)
virus.shape("triangle")
virus.color("red")
virus.penup()


#increases size
virus.turtlesize(2)


#chooses new random x coordinate
virusx=random.randint(-320,320)

#chooses new random y coordinate
#affects time before it respawns
virusy=random.randint(350, 2100)
        

virus.goto(virusx, virusy)

#-------------------------------------------------------------------------------
###BOMB###
#removes all current sprites on screen with a 10x score multiplier

bomb = turtle.Turtle()
bomb.speed(0)
bomb.shape("bomb.gif")

bomb.color("black")
bomb.penup()


#chooses new random x coordinate
bombx=random.randint(-320,320)

#chooses new random y coordinate
#affects time before it respawns
bomby=random.randint(2000, 3000 )
        
bomb.goto(bombx,bomby)

#bomb writing display
bomb1 = 0

bombs=turtle.Turtle()
bombs.penup()
bombs.goto(0,270)
bombs.pendown()
bombs.hideturtle()


bombs.clear()
bombs.color("white")
bomb2=str(bomb1)
bombtext=("Bombs: "+bomb2)
bombs.write(bombtext, font="Impact 20 italic",align="center")




#----------------------------------------------------------------------------

###the hero (player)###
p1=turtle.Turtle()
p1.speed(0)
p1.shape("arrow")
p1.color("white")

#stops drawing on the screen
p1.penup()


#positions the player at the bottom
p1.rt(-90)
p1.goto(0, -250)

p1.turtlesize(2)
#stops player moving at start
p1.direction = "stop"

#POINTS#=========================================
points = 0

pointd = turtle.Turtle()
pointd.penup()
pointd.goto(-320,270)
pointd.pendown()
pointd.hideturtle()
pointd.clear()
pointd.color("white")
pointss=str(points)
pointtext=("Score: "+pointss)
pointd.write(pointtext, font="Impact 20 italic")

#===============================================

#LIVES#=========================================
lives1 = 3

lives = turtle.Turtle()
lives.penup()
lives.goto(210,270)
lives.pendown()
lives.hideturtle()
lives.clear()
lives.color("white")
livess=str(lives1)
livetext=("Lives: "+livess)
lives.write(livetext, font="Impact 20 italic")

#===============================================


#----------------------------------------------------------------------------

#changes p1 direction 

def left():
    p1.direction = "left"

def right():
    p1.direction = "right"

#blow up bomb
def space():
    global bomba
    global bomb1
    if bomb1 >= 1:
        #activates bomb in main loop
        bomba = 1
        
    
    


#listens for keyboard
win.listen()
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")
win.onkeypress(space, "space")



    

###MAIN CODE###

while q < 1:

    if bomba == 1:
    
        bomb1 = bomb1 - 1
        dist = 1100

        bomba = 0


        winsound.PlaySound("explosion.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        bombs.clear()
        bombs.color("white")
        bomb2=str(bomb1)
        bombtext=("Bombs: "+bomb2)
        bombs.write(bombtext, font="Impact 20 italic",align="center")

    
    #updates movements
    win.update()

    # gets player x coordinate
    pos = p1.xcor()

    #stops going off screen (left)
    if pos <= -330:

        #ADDS BOUNCE OFF WALL LEFT
        if a == 0:
            p1.direction = "stop"
            a = 1

        else:
            p1.direction = "right"
            a=0

    #stops going off screen (right)
    if pos >= 330:
        #ADDS BOUNCE OFF WALL Right
        if b == 0:
            p1.direction = "stop"
            b = 1

        else:
            p1.direction = "left"
            b=0
        


    #moves player left
    if p1.direction == "left":
        cx = p1.xcor()
        #player speed
        cx -= +1.2
        p1.setx(cx)

        

    #moves player right
    if p1.direction == "right":
        cx = p1.xcor()
        #player speed
        cx -= -1.2
        p1.setx(cx)
    
   


    #SPEED SYSTEM
    if points >= 1500:
        pspeed = 2.8
        

    if points >= 5000:
        pspeed = 3.3
        hspeed = 2.5
        

    if points >= 7500:
        pspeed = 3.6
        hspeed = 3




    #MOVES VIRUS--------------------------------------------------------------------------------

    #virus y coordinate
    vy = virus.ycor()
    #virus speed
    vy -= 1.2
    #changes virus position downwards
    virus.sety(vy)


    #when virus reaches bottom of page respawn in random place
    if vy < -350:

        #chooses new random x coordinate
        virusx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        virusy=random.randint(350, 1500)
        

        virus.goto(virusx,virusy)


    #===checks for collsion with p1===#

    if virus.distance(p1) < dist:

        #plays virus kill noise
        winsound.PlaySound("virus.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


        #chooses new random x coordinate
        virusx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        virusy=random.randint(350, 1500)

        virus.goto(virusx,virusy)

        #adds 10 points to user
        points = points + 10
        pointd.clear()
        pointd.color("white")
        pointss=str(points)
        pointtext=("Score: "+pointss)
        pointd.write(pointtext, font="Impact 20 italic")


    #--------------------------------------------------------------


        ###TROJAN###

    #trojan y coordinate
    ty = trojan.ycor()
    #trojan speed
    ty -= 1.5
    #changes trojan position downwards
    trojan.sety(ty)


    #when TROJAN reaches bottom of page respawn in random place
    if ty < -350:
        #chooses new random x coordinate
        trojanx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        trojany=random.randint(350, 2500)
        
        #moves trojan to new location
        trojan.goto(trojanx, trojany)


     #===checks for collsion with p1===#

    if trojan.distance(p1) < dist:

        #plays virus kill noise
        winsound.PlaySound("worm.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


        #chooses new random x coordinate
        trojanx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        trojany=random.randint(350, 2500)

        trojan.goto(trojanx,trojany)

        #adds 10 points to user
        points = points + 50
        pointd.clear()
        pointd.color("white")
        pointss=str(points)
        pointtext=("Score: "+pointss)
        pointd.write(pointtext, font="Impact 20 italic")


    #--------------------------------------------------------------------------------------------


    ###WORM###

    #worm y coordinate
    wy = worm.ycor()
    #worm speed
    wy -= 2.5
    #changes trojan position downwards
    worm.sety(wy)


    #when WORM reaches bottom of page respawn in random place
    if wy < -350:
        #chooses new random x coordinate
        wormx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        wormy=random.randint(350, 7000)
        
        #moves worm to new location
        worm.goto(wormx, wormy)


     #===checks for collsion with p1===#

    if worm.distance(p1) < dist:

        #plays worm kill noise
        winsound.PlaySound("worm.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


        #chooses new random x coordinate
        wormx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        wormy=random.randint(350, 7000)

        worm.goto(wormx,wormy)

        #adds 500 points to user
        points = points + 500
        pointd.clear()
        pointd.color("white")
        pointss=str(points)
        pointtext=("Score: "+pointss)
        pointd.write(pointtext, font="Impact 20 italic")


    #----------------------------------------------------------------------------------------------


     ###PACKETS###


    for packet in packets:
        #packet y coordinate
        py = packet.ycor()
        #packetspeed
        py -= pspeed
        #changes trojan position downwards
        packet.sety(py)

        if py < -350:
            #chooses new random x coordinate
            packetx=random.randint(-320,320)

            #chooses new random y coordinate
            #affects time before it respawns
            packety=random.randint(350, 7000)
        
            #moves packet to new location
            packet.goto(packetx, packety)



         #===checks for collsion with p1===#

        if packet.distance(p1) < dist:

            #plays packet kill noise
            winsound.PlaySound("virus.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


            #chooses new random x coordinate
            packetx=random.randint(-320,320)

            #chooses new random y coordinate
            #affects time before it respawns
            packety=random.randint(350, 7000)

            packet.goto(packetx,packety)

            #adds 500 points to user
            if points <= 0:
                points = 0

            else:
                points = points - 10
                pointd.clear()
                pointd.color("white")
                pointss=str(points)
                pointtext=("Score: "+pointss)
                pointd.write(pointtext, font="Impact 20 italic")



        #------------------------------------------------------------------------------------



     ###HACKER###

    #hacker y coordinate
    hy = hack.ycor()
    #hacker speed
    hy -= hspeed
    #changes hacker position downwards
    hack.sety(hy)


    #when hacker reaches bottom of page respawn in random place
    if hy < -350:
        #chooses new random x coordinate
        hackx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        hacky=random.randint(350, 7000)
        
        #moves worm to new location
        hack.goto(hackx, hacky)

        #looses a life
        lives1 = lives1 - 1

        #game over
        if lives1 <= 0:
            lives.clear()
            lives.color("white")
            livess=str(lives1)
            livetext=("Lives: "+livess)
            lives.write(livetext, font="Impact 20 italic")
            ###GAMEOVER###


            go = turtle.Turtle()
            go.hideturtle()
            go.speed(0)
            go.color("red")
            go.clear()
            go.pendown()
            go.write("GAME OVER", font="Impact 40 italic", align="center")
            q=1

            

        lives.clear()
        lives.color("white")
        livess=str(lives1)
        livetext=("Lives: "+livess)
        lives.write(livetext, font="Impact 20 italic")

        


     #===checks for collsion with p1===#

    if hack.distance(p1) < dist:

        #plays worm kill noise
        winsound.PlaySound("hacker.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


        #chooses new random x coordinate
        hackx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        hacky=random.randint(350, 4000)

        hack.goto(hackx,hacky)

        lk = lk + 1
        if lk >= 10:
            go1 = turtle.Turtle()
            go1.hideturtle()
            go1.speed(0)
            go1.color("white")
            go1.clear()
            go1.pendown()
            go1.write("YOU GAINED A LIFE", font="Impact 40 italic", align="center")
            lk = 0
            lives1 = lives1 + 1
            time.sleep(1)
            go1.clear()

            #updates lives
            lives.clear()
            lives.color("white")
            livess=str(lives1)
            livetext=("Lives: "+livess)
            lives.write(livetext, font="Impact 20 italic")
             
#------------------------------------------------------------------------------



        #bomb y coordinate
    by = bomb.ycor()
    #bomb speed
    by -= 1
    #changes bomb position downwards
    bomb.sety(by)


    #when bomb reaches bottom of page respawn in random place
    if by < -350:
        #chooses new random x coordinate
        bombx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        bomby=random.randint(2000, 3000)
        
        #moves trojan to new location
        bomb.goto(bombx, bomby)


     #===checks for collsion with p1===#

    if bomb.distance(p1) < dist:

        #plays bomb grab noise
        winsound.PlaySound("bombcollect.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )


        #chooses new random x coordinate
        bombx=random.randint(-320,320)

        #chooses new random y coordinate
        #affects time before it respawns
        bomby=random.randint(2000, 3000)

        bomb.goto(bombx,bomby)

        #adds 1 bomb to user
        bomb1 = bomb1 + 1
        bombs.clear()
        bombs.color("white")
        bomb2=str(bomb1)
        bombtext=("Bombs: "+bomb2)
        bombs.write(bombtext, font="Impact 20 italic")


    #ends bomb
    if bomba == 0:
        dist = 30


win.mainloop()



