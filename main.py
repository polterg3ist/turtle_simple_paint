from turtle import Turtle
from user_ui import UserUi


class Application(Turtle):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = UserUi()
        self.step = 10
        self.shape('circle')
        self.speed(0)
        self.width(5)
        self.pendown()
        self.screen = self.getscreen()
        self.do_binds()
        self.screen.listen()
        self.create_ui()

    def create_ui(self):
        self.ht()
        self.ui.init_ui()
        self.st()

    def do_binds(self):
        self.screen.onclick(lambda x, y: self.goto(x, y))
        self.ondrag(lambda x, y: self.goto(x, y))

        self.screen.onkey(lambda: self.color("red"), 'r')
        self.screen.onkey(lambda: self.color("orange"), 'o')
        self.screen.onkey(lambda: self.color("yellow"), 'y')
        self.screen.onkey(lambda: self.color("green"), 'g')
        self.screen.onkey(lambda: self.color("light blue"), 'l')
        self.screen.onkey(lambda: self.color("blue"), 'b')
        self.screen.onkey(lambda: self.color("violet"), 'v')

        self.screen.onkey(lambda: self.width(5), '1')
        self.screen.onkey(lambda: self.width(10), '2')
        self.screen.onkey(lambda: self.width(18), '3')
        self.screen.onkey(lambda: self.width(28), '4')
        self.screen.onkey(lambda: self.width(40), '5')

        self.screen.onkeypress(lambda: self.goto(self.xcor(), self.ycor() + self.step), "Up")
        self.screen.onkeypress(lambda: self.goto(self.xcor(), self.ycor() - self.step), "Down")
        self.screen.onkeypress(lambda: self.goto(self.xcor() - self.step, self.ycor()), "Left")
        self.screen.onkeypress(lambda: self.goto(self.xcor() + self.step, self.ycor()), "Right")

        self.screen.onkey(lambda: self.begin_fill(), 'f')
        self.screen.onkey(lambda: self.end_fill(), "e")


if __name__ == "__main__":
    app = Application()
    app.screen.mainloop()
