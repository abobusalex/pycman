from typing import Tuple
import pygame
import random

BLACK = (18, 0, 51)

def check_if_block(x,y, f):
    return (True if f[y][x] != 1 else False)

def worms_new_pos(f, Worms):
    for worm in Worms:
        
        a = True
        while a:
            where = random.randint(0,4)
            if where == 0 and f[worm.posy - 1][worm.posx] in (0,3,5): # up
                f[worm.posy - 1][worm.posx] = worm.no
                f[worm.posy][worm.posx] = 3
                worm.posy -= 1
                a = False
            if where == 1 and f[worm.posy + 1][worm.posx] in (0,3,5): # down
                f[worm.posy + 1][worm.posx] = worm.no
                f[worm.posy][worm.posx] = 0
                worm.posy += 1
                a = False
            if where == 2 and f[worm.posy][worm.posx - 1] in (0,3,5): # left
                f[worm.posy][worm.posx - 1 ] = worm.no
                if worm.no == 6:
                    f[worm.posy][worm.posx] = 0
                else:
                    f[worm.posy][worm.posx] = 3
                worm.posx -= 1
                a = False
            if where == 3 and f[worm.posy][worm.posx + 1] in (0,3,5): # right
                f[worm.posy][worm.posx + 1 ] = worm.no
                
                if worm.no == 8:
                    f[worm.posy][worm.posx] = 0
                else:
                    f[worm.posy][worm.posx] = 3
                    
                worm.posx += 1
                a = False

    for i in f:
        print(i)

class Worm:

    def __init__(self, name, img, screen, no):
        self.img = img
        self.name = name
        self.screen = screen
        self.no = no
        self.image = pygame.image.load(img)

    def first_place(self, field):

        a = [1,5,6,7,8]
        a.remove(self.no)

        f = True
        while f:
            self.posx = random.randint(0, len(field[0] ) - 1)
            self.posy = random.randint(0, len(field) - 1)
            # print(self.name, self.posx, self.posy)
            # print(field[self.posy][self.posx])

            if field[self.posy][self.posx] not in a:
                break

        # print(self.name, self.posx, self.posy)
        # print(field[self.posy][self.posx])
        field[self.posy][self.posx] = self.no

    def draw(self,x,y):
        self.screen.blit(self.image, (x,y))


def main():
     
    pygame.init()
    pygame.mixer.music.load('imgs/audio.mp3')
    pygame.mixer.music.play(999999)
    gua = pygame.mixer.Sound('imgs/gua.mp3')


    clock = pygame.time.Clock()
    logo = pygame.image.load("imgs/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("PycmanSolid")
     
    block = pygame.image.load("imgs/block.png")
    screen = pygame.display.set_mode((400,600))

    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Score', False, (100,40, 55))


    field = [[1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,0,1,0,1,1,0,1],
             [1,0,0,0,1,0,1,0,1,0,0,1],
             [1,0,0,0,1,0,1,0,1,0,1,1],
             [1,0,1,0,1,0,0,0,1,0,0,1],
             [1,0,1,0,1,0,1,1,1,1,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,1,0,1,1,1,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,0,1,0,0,1,1,1],
             [1,0,0,0,1,0,0,0,0,0,0,1],
             [1,1,1,0,1,0,1,0,1,1,0,1],
             [1,0,0,0,0,0,1,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1,1,1]]

    running = True
    image = pygame.image.load("imgs/logo32x32.png")
    gold =  pygame.image.load("imgs/gold.png")

    green = Worm("green","imgs/green.png", screen, 6) # 6
    green.first_place(field)

    blue = Worm("blue","imgs/blue.png", screen,7) # 7
    blue.first_place(field)

    red = Worm("red","imgs/red.png", screen ,8 )    #8
    red.first_place(field)


    player = Worm("player","imgs/logo32x32.png", screen , 5) # 5 
    score = 0
    player.first_place(field)

    for i in field:
        print(i)
    

    while running:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    if check_if_block(player.posx, player.posy + 1, field):
                        player.posy += 1
                        worms_new_pos(field,[green,blue,red])

                if event.key == pygame.K_UP:
                    if check_if_block(player.posx, player.posy - 1 , field):
                        player.posy -= 1
                        worms_new_pos(field,[green,blue,red])

                if event.key == pygame.K_LEFT:
                    if check_if_block(player.posx - 1, player.posy, field):
                        player.posx -= 1
                        worms_new_pos(field,[green,blue,red])

                if event.key == pygame.K_RIGHT:
                    if check_if_block(player.posx + 1, player.posy, field):
                        player.posx += 1
                        worms_new_pos(field,[green,blue,red])



        screen.fill(BLACK)

        if field[player.posy][player.posx] in [1,6,7,8]:
            running = False


        for y in range(0, len(field) ):
                for x in range(0, len(field[0]) ):
                    if field[y][x] == 1:
                    # if x == 0 or y == 0 or x == 32*11 or y == 32*15:
                        screen.blit(block, (x*32,y*32))
                    if field[y][x] == 0:
                        screen.blit(gold, (x*32,y*32))

        if field[player.posy][player.posx] == 0:
            score += 100
            print("score ", score)
            gua.play()
            textsurface = myfont.render('Score {}'.format(score), False, (100,40, 55))

            field[player.posy][player.posx] = 3

        player.draw(player.posx*32, player.posy*32)
        green.draw(green.posx*32, green.posy*32)
        blue.draw(blue.posx*32, blue.posy*32)
        red.draw(red.posx*32, red.posy*32)

        screen.blit(textsurface,(50,500))

        pygame.display.flip()
        pygame.time.delay(100)


if __name__=="__main__":
    main()