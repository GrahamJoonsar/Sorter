import pygame, random, time

pygame.init()

# Window settings
wwidth = 2000
win = pygame.display.set_mode((wwidth, 500))
pygame.display.set_caption("Sorter")


# Class for making the bars
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
# Generates bars with random height and color
for i in range(200):
    rnd = random.randint(1, 500)
    bars.append(Bar(i * 10, rnd, 10, 500 - rnd, 5, (i * .25, 200 / (i + 1), 225 - i)))


swaps = 0
# Sorts the bars
def sort(list):
    global swaps
    swaps = 0
    for i in range(len(list) - 1):
        # Checks if the bar to the right is smaller than the current bar
        if list[i].height > list[i + 1].height:
            # Switches the indexes of the Bars
            temp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = temp
            # Switches the X values of the bars
            temp = list[i].x
            list[i].x = list[i + 1].x
            list[i + 1].x = temp
            swaps += 1

end = False
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

    # Pause at the start
    if first:
        first = False
        time.sleep(2)
    if swaps == 0 and end == False:
        end = True
        time.sleep(2)
        for b in range(len(bars)):
            bars[b].color = (b * .25, 200 / (b + 1), 225 - b)
            pygame.display.update()


pygame.quit()
