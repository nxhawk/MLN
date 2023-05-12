from turtle import *


def cell(n: int, x: float, y: float, fill_color: str):
    """
    draw cell (square) in start (x, y)
    """
    celltu = Turtle()
    celltu.hideturtle()
    celltu.up()
    celltu.goto(x, y)
    celltu.down()
    celltu.begin_fill()
    celltu.fillcolor(fill_color)
    for _ in range(4):
        celltu.fd(400/n)
        celltu.rt(90)
    celltu.end_fill()


def board(n: int):
    """
    draw empty board game size nxn
    """
    x = 100
    y = 450
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                cell(n, x, y, "#baca44")
            else:
                cell(n, x, y, "#eeeed2")
            x += 400/n
        x = 100
        y -= 400/n


def draw_queen(col: int, row: int, n: int):
    """
    Draw the queen in its cell.
    """
    q = Turtle()
    q.hideturtle()
    q.up()
    posX = 100 + (row * 400 / n) - (0.5 * 400 / n)
    posY = 50 + col * (400 / n)
    q.goto(posX, posY)
    q.color("#1f1f1f")
    q.write("♛", align="center", font=("Arial", int((400/n)*0.6), "bold"))


def read_input(win) -> int:
    """
    Input Screen that takes number of queens (n) from the user
    """
    tu = Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300, 375)
    tu.color("#1f1f1f")
    tu.write("N-Queens:", align="center", font=("Arial", "32", "bold"))
    n = win.numinput("N-Queen Problem",
                     "Number Of Queens (Integer):", 1, minval=1, maxval=100)
    tu.goto(300, 260)
    tu.color("#fa4af0")
    tu.write("Processing...", align="center", font=("Arial", "50", "bold"))
    tu.clear()
    return int(n)


def no_solution(n: int):
    """
    Write the text if the problem can't be solved.
    """
    tu = Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300, 350)
    tu.color("#fa2d00")
    tu.write("Sorry!", align="center", font=("Arial", "42", "bold"))
    tu.goto(300, 275)
    tu.color("#1f1f1f")
    tu.write("The Problem Can't Be Solved",
             align="center", font=("Arial", "26", "bold"))
    tu.goto(300, 225)
    tu.write(f"When N = {n}", align="center", font=("Arial", "26", "bold"))


def sc2_solution(gens: int):
    """
    Write the text if the solution is found, it shows the solution's generation.
    """
    tu = Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300, 525)
    tu.color("#00a613")
    tu.write("Solution Found!", align="center", font=("Arial", "30", "bold"))
    tu.goto(300, 475)
    tu.color("#1f1f1f")
    tu.write(f"Found In Generation: {gens}",
             align="center", font=("Arial", "22", "bold"))


def sc2_limit(gens: int, fitness: int):
    """
    Write the text if the is no solution found and exceed the generations limit, it shows the fitness of the fittest
    found chromosome and the number of attempts.
    """
    tu = Turtle()
    tu.up()
    tu.hideturtle()
    tu.goto(300, 525)
    tu.color("#fa2d00")
    tu.write("Limit Reached!", align="center", font=("Arial", "30", "bold"))
    tu.goto(300, 475)
    tu.color("#1f1f1f")
    tu.write(f"Fittest: {fitness}   -   Attempts: {gens}",
             align="center", font=("Arial", "22", "bold"))


def sc2(n: int, chromosome: list[int]):
    """
    Draw board result finded with n queens
    """
    tu = Turtle()
    tu.up()
    tu.hideturtle()
    tu.color("#1f1f1f")
    # draw board game
    board(n)
    # draw solution put nxn queens
    for index, queen in enumerate(chromosome):
        draw_queen(index, queen, n)
