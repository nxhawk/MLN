import math
import pygame as pg
import sys
import time
from pygame.locals import *

from NeuronNetwork import *

pg.init()  # initialize the game
size = width, height = 1060, 700  # screen size
screen = pg.display.set_mode(size)
pg.display.set_caption("Genetic algorithm car")  # set title
# load background image
background = pg.image.load('resources/bg_reward.png')
font = pg.font.Font(None, 25)  # font setting

num = 100  # samples number per loop
generation = 50  # iteration round number
gen_max_time = 35

cross_ratio = 0.3  # ratio of top performers when crossover
elite_ratio = 0.05  # ratio of elite in all samples

pm = 0.2  # probability of mutation
mutate_range = (-0.2, 0.2)  # range of mutation value -~+

FPS = 60  # fps setting

x_init, y_init = 385, 400  # car's initial position
max_speed = 4  # car's max limit speed
min_speed = 2  # car's min limit speed
min_angle_speed_change_frame_interval = 1


def draw_text(text, pos, color):
    img = font.render(
        text, True, color)
    screen.blit(img, pos)


class Car:
    '''
    Car object
    '''

    def __init__(self) -> None:
        # default position and angle
        self.x = x_init
        self.y = y_init
        self.angle = 45
        self.speed = min_speed

        # live status
        self.is_alive = True

        # three distance indicator lines' end point positions
        self.x1, self.y1 = 0, 0
        self.x2, self.y2 = 0, 0
        self.x3, self.y3 = 0, 0

        # three distances from the track boundary
        self.dis1 = 0
        self.dis2 = 0
        self.dis3 = 0

        # total running distance
        self.distance = 0

        # judge reward line flag
        self.flag_reward = False

        # frame counter, angle can change only when counter enough
        self.counter = 0

    def update_position(self) -> None:
        '''
        update new position and distance to wall
        '''
        if not self.is_alive:
            return

        angle = math.pi * (-self.angle) / 180
        self.x = self.x + self.speed*math.cos(angle)
        self.y = self.y + self.speed*math.sin(angle)
        self.distance += math.sqrt((self.speed*math.cos(angle))
                                   ** 2 + (self.speed*math.sin(angle))**2)

    def detect_track_boundary(self):
        '''
        touch wall or dont any step move 
        '''
        pixel = screen.get_at((int(self.x), int(self.y)))
        # ma mau RGB (0, 0, 0)
        if pixel[0] <= 1 and pixel[1] <= 1 and pixel[2] <= 1:
            self.is_alive = False
        if self.distance <= 0:
            self.is_alive = False

    def detect_mark_line(self, i):
        '''
        detect yellow reward line then reward
        '''
        if screen.get_at((int(self.x), int(self.y))) == (255, 243, 0, 255) or (255, 242, 0, 255):
            if not self.flag_reward:
                self.distance += 1000  # reward
                print('reward', str(i))
                self.flag_reward = True
        else:
            if self.flag_reward:
                self.flag_reward = False

    def draw_indicator_line(self):
        '''
        draw three indicator lines of each car
        '''

        pg.draw.line(screen, (0, 255, 0), (self.x, self.y),
                     (self.x1, self.y1), 1)
        pg.draw.line(screen, (0, 255, 0), (self.x, self.y),
                     (self.x2, self.y2), 1)
        pg.draw.line(screen, (0, 255, 0), (self.x, self.y),
                     (self.x3, self.y3), 1)

    def calculate_three_distance(self):
        '''
        calculate distance from three points to walls
        '''
        if not self.is_alive:
            return

        # get point of current state car and direction
        x = self.x
        y = self.y
        angle = self.angle
        # direction three line follow current direction of car
        ang1 = angle + 55
        ang2 = angle
        ang3 = angle - 55

        # to o to radian
        ang1 = math.pi * ang1 / 180
        ang2 = math.pi * ang2 / 180
        ang3 = math.pi * ang3 / 180

        d = 12  # weight to reduce the distance to a reasonable region
        for i in range(1000):
            x1 = x + i * math.cos(ang1)
            y1 = y - i * math.sin(ang1)
            # detect track boundary black color(wall) (0, 0, 0, 255) or (0,1, 0, 255)
            # tham so thu 4 ko quan trong 3 tham so dau la ma mau rgb
            if x1 < 0 or x1 > width or y1 < 0 or y1 > height:
                continue
            pixel = screen.get_at((int(x1), int(y1)))
            if pixel[0] <= 1 and pixel[1] <= 1 and pixel[2] <= 1:
                self.x1, self.y1 = x1, y1
                self.dis1 = math.sqrt((x - x1)**2 + (y - y1)**2) / d
                break

        for i in range(1000):
            x2 = x + i * math.cos(ang2)
            y2 = y - i * math.sin(ang2)
            # detect track boundary black color(wall) (0, 0, 0, 255) or (0,1, 0, 255)
            # tham so thu 4 ko quan trong 3 tham so dau la ma mau rgb
            if x2 < 0 or x2 > width or y2 < 0 or y2 > height:
                continue
            pixel = screen.get_at((int(x2), int(y2)))
            if pixel[0] <= 1 and pixel[1] <= 1 and pixel[2] <= 1:
                self.x2, self.y2 = x2, y2
                self.dis2 = math.sqrt((x - x2)**2 + (y - y2)**2) / d
                break

        for i in range(1000):
            x3 = x + i * math.cos(ang3)
            y3 = y - i * math.sin(ang3)
            # detect track boundary black color(wall) (0, 0, 0, 255) or (0,1, 0, 255)
            # tham so thu 4 ko quan trong 3 tham so dau la ma mau rgb
            if x3 < 0 or x3 > width or y3 < 0 or y3 > height:
                continue
            pixel = screen.get_at((int(x3), int(y3)))
            if pixel[0] <= 1 and pixel[1] <= 1 and pixel[2] <= 1:
                self.x3, self.y3 = x3, y3
                self.dis3 = math.sqrt((x - x3)**2 + (y - y3)**2) / d
                break

    def draw(self, color='blue'):
        '''
        draw car dot blue big
        '''
        if color == 'blue':
            color = (0, 0, 255)
        elif color == 'yellow':
            color = (255, 255, 0)
        elif color == 'red':
            color = (255, 0, 0)
        pg.draw.circle(screen, color, (int(self.x), int(self.y)), 7, 0)


def sort_car_nets(cars: list[Car], nets: list[NeuronNetwork]):
    '''
    sort car by this fitness (big -> small)
    '''
    for i in range(len(cars) - 1):
        for j in range(i + 1, len(cars)):
            if cars[i].distance < cars[j].distance:
                cars[i], cars[j] = cars[j], cars[i]
                nets[i], nets[j] = nets[j], nets[i]

    return cars, nets


def create_car_agents():
    '''
    create mutil cars
    '''
    cars = []
    for _ in range(num):
        car = Car()
        cars.append(car)
    return cars


def main():
    '''
    main func
    '''
    fps = 0
    count = 0
    start = time.time()
    begin = time.time()
    last_round_time = begin
    current_gen = 1
    clock = pg.time.Clock()

    run = True
    pause = False

    # create gen 1
    cars = create_car_agents()
    nets = [NeuronNetwork() for _ in range(num)]

    # main loop
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = not pause

        if pause:
            continue

        # calculate fps
        count += 1
        now = time.time()
        if now - start > 0.1:
            fps = count / (now - start)
            start = now
            count = 0

        screen.blit(background, (0, 0))  # draw background

        for i in range(len(cars)):
            if cars[i].is_alive:
                cars[i].calculate_three_distance()
                angle, speed = nets[i].feedforward(
                    [cars[i].dis1, cars[i].dis2, cars[i].dis3])  # get network's output

                # update car's properties
                # speed = abs(speed)*10
                if speed < min_speed:
                    speed = min_speed
                if speed > max_speed:
                    speed = max_speed

                if cars[i].counter >= min_angle_speed_change_frame_interval:
                    cars[i].counter = 0
                    cars[i].angle += angle * 180 / 30
                    cars[i].speed = speed
                else:
                    cars[i].counter += 1

                cars[i].update_position()  # update position
                # detect reward line and start line
                cars[i].detect_mark_line(i)
                cars[i].detect_track_boundary()  # detect collide
                nets[i].score = cars[i].distance  # update network's score

        # change to dead if time beyond 30 seconds
        if time.time() - last_round_time > gen_max_time:
            for i in range(len(cars)):
                if cars[i].is_alive:
                    cars[i].distance = 0
                    cars[i].is_alive = False

        cars, nets = sort_car_nets(cars, nets)  # sort cars by distance

        alive = 0  # survive numbers
        for i in range(len(cars)):
            if i == 0:
                cars[i].draw('yellow')  # No.1 car marked yellow
            else:
                cars[i].draw('blue')  # draw car itself
            if cars[i].is_alive:
                alive += 1  # calculate alive members
                cars[i].draw_indicator_line()  # draw three indicator lines

        # draw params on the screen
        draw_text("Gen: " + str(current_gen), (900, 10), (0, 0, 255))
        draw_text("All: " + str(len(cars)), (900, 30), (0, 0, 255))
        draw_text("Alive: " + str(alive), (900, 50), (0, 0, 255))
        draw_text("Top1 distance: " +
                  str(int(cars[0].distance)), (900, 70), (0, 0, 255))
        draw_text("Total time: " +
                  str(int(time.time() - begin)), (900, 90), (0, 0, 255))
        draw_text("This round time: " +
                  str(int(time.time() - last_round_time)), (900, 110), (0, 0, 255))
        draw_text("Fps:" + str(round(fps, 5)), (10, 10), (0, 0, 255))
        mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()  # get mouse's position
        draw_text('pos_x:' + str(mouse_pos_x) + '  pos_y:' +
                  str(mouse_pos_y), (10, 30), (0, 0, 255))
        draw_text(str(screen.get_at((mouse_pos_x, mouse_pos_y))),
                  (10, 70), (0, 0, 255))
        draw_text("Press 'p' to pause!", (10, 50), (0, 0, 255))

        # pg.display.flip() #  redraw window
        pg.display.update()

        # when this gen was over
        if alive == 0:
            # top elites' networks
            elites = get_elites(nets, elite_ratio)

            # next generation's networks list
            next_gen_nets = []

            # add this generation's elites directly to next generation
            next_gen_nets.extend(elites)

            # create hybrid children and add them to next generation until enough
            for _ in range(num - len(elites)):
                child = crossover(nets, cross_ratio)
                next_gen_nets.append(child)

            # mutate next generation's each network including elites and children
            next_gen_nets = mutate(next_gen_nets, pm, mutate_range)

            # recreate new cars
            cars = create_car_agents()

            nets = next_gen_nets
            last_round_time = time.time()

            # quit when gen was enough
            current_gen += 1
            if current_gen > generation:
                run = False

    pg.quit()


if __name__ == '__main__':
    main()
