import pygame
import basic_creatures
 
pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
LIGHT_BLUE = (  0, 204, 204)
ORANGE = (255, 128,   0)
 
size = [400, 300]
screen = pygame.display.set_mode(size)
 
done = False
clock = pygame.time.Clock()

creature = basic_creatures.newCreature(spontaneous_pop=100, death=50, divide=50, mutate=30, number=1, X=size[0], Y=size[1], color=BLUE)
#spontaneous_pop, death, divide, mutate, number, X, Y, color
 
while not done:

    livingCreatures=creature.update()
 
    clock.tick(1000)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True 
 
    screen.fill(LIGHT_BLUE)

    #fix werid error 

    for i in range(len(livingCreatures)):
        # try:
        screen.lock()
        pygame.draw.ellipse(screen, livingCreatures[i][2], (livingCreatures[i][0], livingCreatures[i][1], 20, 20))
        screen.unlock()
        print(livingCreatures[i], screen)
        # except:
        #     pass
    pygame.display.flip()

pygame.quit()