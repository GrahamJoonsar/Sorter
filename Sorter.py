import pygame, random, time

pygame.init()

wwidth = 2000
win = pygame.display.set_mode((wwidth, 500))
pygame.display.set_caption("Sorter")


class Bar:
    def __init__(self, x, y, width, height, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


first = True
bars = []
for i in range(200):
    rnd = random.randint(1, 500)
    bars.append(Bar(i * 10, rnd, 10, 500 - rnd, 5, (i * .25, 200 / (i + 1), 225 - i)))


def sort(list):
    for i in range(len(list) - 1):
        if list[i].height > list[i + 1].height:
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp
            temp = list[i].x
            list[i].x = list[i + 1].x
            list[i + 1].x = temp

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))
    for bar in bars:
        bar.draw()

    pygame.display.update()

    sort(bars)

    if first:
        first = False
        time.sleep(2)

pygame.quit()
