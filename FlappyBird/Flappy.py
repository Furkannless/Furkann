import turtle,time, random

pencere = turtle.Screen()
pencere.title('Flappy Bird - Gevşek Kuş')
pencere.bgcolor('blue')
pencere.bgpic('background.gif')
pencere.setup(width=500, height=700)
pencere.tracer(0)

pencere.register_shape('bird.gif')

bird = turtle.Turtle()
bird.speed()
bird.color('yellow')
bird.shape('bird.gif')
bird.penup()
bird.goto(-100, 0)
bird.dx = 0
bird.dy= 1

puan = 100
yazı = turtle.Turtle()
yazı.speed()
yazı.color('white')
yazı.shape('square')
yazı.hideturtle()
yazı.penup()
yazı.goto(0, 300)
yazı.write('Puan: {}'.format(puan), align='center', font=('Courier', 24,'bold'))



yercekimi = -0.3

def bird_up(x, y):
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8


borular = []
pencere.listen()
pencere.onscreenclick(bird_up)

starting_time = time.time()
while True:
    time.sleep(0.04)
    pencere.update()

    bird.dy = bird.dy + yercekimi

    if (time.time() - starting_time > random.randint(4, 10) ):
        starting_time = time.time()

        boru_üst = turtle.Turtle()
        boru_üst.speed(0)
        boru_üst.color('red')
        boru_üst.shape('square')
        boru_üst.h = random.randint(10, 20)
        boru_üst.shapesize(boru_üst.h, 2, outline=None)
        boru_üst.penup()
        boru_üst.goto(+300, 250)
        boru_üst.dx = -4
        boru_üst.dy = 1

        boru_alt = turtle.Turtle()
        boru_alt.speed(0)
        boru_alt.color('red')
        boru_alt.shape('square')
        boru_alt.h = 40 - boru_üst.h - random.randint(1, 10)
        boru_alt.shapesize(boru_alt.h, 2, outline=None)
        boru_alt.penup()
        boru_alt.goto(+300, -250)
        boru_alt.dx = -4
        boru_alt.dy = 1

        borular.append((boru_üst, boru_alt))


    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)
    if len(borular) > 0 :
        for boru in borular:
            x = boru[0].xcor()
            x = x + boru[0].dx
            boru[0].setx(x)
            x = boru[1].xcor()
            x = x + boru[1].dx
            boru[1].setx(x)
            if boru[0].xcor() < -300:
                boru[0].hideturtle()
                boru[1].hideturtle()
                borular.pop(borular.index(boru))
            if (bird.xcor()+10>boru[0].xcor()-20) and (bird.xcor()+10<boru[0].xcor()+20):
                 if (bird.ycor()+10>boru[0].ycor()-boru[0].h*10) or (bird.ycor()-10<boru[1].ycor()+ boru[1].h*10):
                     puan = puan - 2
                     yazı.clear()
                     yazı.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))
    if puan < 1:
        yazı.clear()
        yazı.write('KAYBETTİNİZ'.format(puan), align='center', font=('Courier', 30, 'bold'))
        yercekimi = -5
        time.sleep(0.9)
        exit()