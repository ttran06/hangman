from graphics import *
from time import sleep

win = GraphWin("df", 500, 600)
cir = Text(Point(200, 300), "Hello World")
cir.draw(win)

while win.checkKey() != "q":
    continue

cir.setText("GOODBYE")
cir.setText("Hello")
sleep(5)
