from turtle import Turtle


class UserUi(Turtle):
    def __init__(self):
        super(UserUi, self).__init__()
        self.square_size = 40
        self.palette_x = -190
        self.palette_y = 330
        self.palette_colors = ["red", "orange", "yellow", "green", "light blue", "blue", "violet"]
        self.pensize_x = 400
        self.pensize_y = 150
        self.background_x = -400
        self.background_y = 80
        self.background_colors = ["black", "white"]
        self.background_hotkeys = ["N", "D"]
        self.penup()
        self.speed(0)

    def draw_square(self, clr):
        self.pendown()
        self.color("black", clr)
        self.begin_fill()

        for _ in range(4):
            self.forward(self.square_size)
            self.left(90)

        self.end_fill()
        self.penup()

    def draw_circle(self, r, clr):
        self.pendown()
        self.color(clr)
        self.begin_fill()
        self.circle(r)
        self.end_fill()
        self.penup()

    def draw_text(self, text, indent, clr="black"):
        self.forward(indent)
        self.pendown()
        self.color(clr)
        self.write(text, font=("Times new Roman", 12, "normal"))
        self.penup()

    def draw_palette(self):
        indent = 3 + self.square_size
        for clr in self.palette_colors:
            self.goto(self.palette_x, self.palette_y)
            self.draw_square(clr)
            self.draw_text(clr[0].upper(), indent)
            self.palette_x += 60

    def draw_pen_size(self):
        base_r = 5
        indent = 30
        for pen_size in range(1, 6):
            r = base_r * pen_size
            self.goto(self.pensize_x, self.pensize_y)
            self.draw_circle(r, "grey")
            self.draw_text(pen_size, indent)
            self.pensize_y -= 40 + r

    def draw_background(self):
        # drawing text 'background'
        self.goto(self.background_x, self.background_y)
        self.draw_text("BG", 3)

        for i in range(2):
            self.background_y -= 50
            self.goto(self.background_x, self.background_y)
            self.draw_square(self.background_colors[i])
            self.draw_text(self.background_hotkeys[i], -20)

    def init_ui(self):
        self.draw_palette()
        self.draw_pen_size()
        self.draw_background()
        self.ht()
