import pygame
import random
x=pygame.init()

#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)



#creating window
screen_width=500
screen_height=400
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sona Snake Game")

#gmae specific variables

clock = pygame.time.Clock()

font=pygame.font.SysFont(None,20)


def text_screen(text,color,x,y):
    screen_text = font.render(text,True, color)
    gameWindow.blit(screen_text, [x,y] )

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to Snakes", black ,250,250)
        text_screen("press space bar to play", black, 250, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type== pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(60)


#creating game loop
def gameloop():
    exit_game = False
    game_Over = False
    snake_x = 45
    snake_y = 55
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    velocity_x = 0
    velocity_y = 0

    snk_list = []
    snk_length = 1

    snake_size = 10
    fps = 30
    init_velocity = 2
    score = 0

    with open("high_score.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_Over:
            with open("high_score.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            text_screen("Game over ! press enter to continue",red,50,100)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x =snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=20
                food_x = random.randint(0, screen_width-10)
                food_y = random.randint(0, screen_height-10)
                snk_length+=5
                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill(white)
            text_screen("Score : " + str(score)+ "High Score :" + str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x,food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]


            if head in snk_list[:-1]:
                game_Over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_Over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)




    pygame.quit()
    quit()


welcome()
gameloop()