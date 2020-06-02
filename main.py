import pygame
import time
import random
 
'''
    SIMPLE SNAKE GAME
    date : 6.4.2020
    author : Truong Dang Duong
    facebook : https://www.facebook.com/duongdzin
    (Something in original snake game is not in there , I'm lazy to do more)
'''
 
BLOCK_SIZE = 20
GAME_MAX_X = 60
GAME_MAX_Y = 60
GAME_HIGHT = BLOCK_SIZE*GAME_MAX_Y
GAME_WIDTH = BLOCK_SIZE*GAME_MAX_X
GAME_SPEED = 0.1
 
game_over = False
snake_x = 4
snake_y = 4
food_x = random.randrange(1, round(GAME_MAX_X/2)-1)
food_y = random.randrange(1, round(GAME_MAX_Y/2)-1)
eat = False
move = 'idle'
can_left = True
can_right = True
can_up = True
can_down = True
 
pygame.init()
dis = pygame.display.set_mode((GAME_HIGHT//2,GAME_WIDTH//2))
pygame.display.set_caption("Snake Game !")
font = pygame.font.SysFont('Tahoma',40)
 
def draw_board(max_x,max_y,size):
    for i in range(round(max_x/2)):
        pygame.draw.rect(dis,(0, 0, 102),[i*size,0*size,size,size])
    for i in range(round(max_x/2)):
        pygame.draw.rect(dis,(0, 0, 102),[i*size,round(max_y/2-1)*size,size,size])
    for i in range(round(max_y/2)):
        pygame.draw.rect(dis,(0, 0, 102),[0*size,i*size,size,size])
    for i in range(round(max_y/2)):
        pygame.draw.rect(dis,(0, 0, 102),[round(max_x/2-1)*size,i*size,size,size])
def draw_block(dis,pos,size):
    pygame.draw.rect(dis,(0,100,0),[pos[0]*size,pos[1]*size,size,size])
def draw_snake(dis,snake,size):
    for i in range(len(snake)):
        if i == 0 or i == 1:
            pygame.draw.rect(dis,(225,0,0),[snake[i][0]*size,snake[i][1]*size,size,size])
        else :
            pygame.draw.rect(dis,(225,225,255),[snake[i][0]*size,snake[i][1]*size,size,size])
        pass
    pass
def show_game_over():
    size = BLOCK_SIZE
    for i in range(GAME_MAX_Y//2):
        if i % 2 == 0 :
                pygame.draw.rect(dis,(255, 0, 0),[0,0,GAME_MAX_X // 2,size])
        else :
                pygame.draw.rect(dis,(0, 102, 0),[0,0,GAME_MAX_X // 2,size])
        time.sleep(0.2)
    pass
 
snake = [[snake_x,snake_y],[snake_x,snake_y]]
while not game_over :
 
    draw_board(GAME_MAX_X,GAME_MAX_Y,BLOCK_SIZE)
 
    old_pos_x = snake_x
    old_pos_y = snake_y
    if eat :
        snake.insert(1,[old_pos_x,old_pos_y])
        eat = False
    old_snake_x = snake_x
    old_snake_y = snake_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_left:
                move = 'left'
            elif event.key == pygame.K_RIGHT and can_right:
                move = 'right'
            elif event.key == pygame.K_UP and can_up:
                move = 'up'
            elif event.key == pygame.K_DOWN and can_down:
                move = 'down'
    if   move == 'left' :
        snake_x -= 1
    elif move == 'right':
        snake_x += 1
    elif move == 'down' :
        snake_y += 1
    elif move == 'up'   :
        snake_y -= 1
 
    if snake_x == GAME_MAX_X/2-1 or snake_y == GAME_MAX_Y/2-1 or snake_x == 0 or snake_y == 0:
        game_over = True
    if snake_x == food_x and snake_y == food_y:
        eat = True
        food_x = random.randrange(1, round(GAME_MAX_X/2)-2)
        food_y = random.randrange(1, round(GAME_MAX_Y/2)-2)
        food = [food_x,food_y]
        while food in snake:
            food_x = random.randrange(1, round(GAME_MAX_X/2)-1)
            food_y = random.randrange(1, round(GAME_MAX_Y/2)-1)
            food = [food_x,food_y]
    else :
        snake[0] = [snake_x,snake_y]
    food = [food_x,food_y]
   
   
    for index in range(len(snake)):
        if index == 0 :
            old_dot = snake[index]
            snake[index] = [snake_x,snake_y]
        else :
            new_dot = snake[index]
            snake[index] = old_dot
            old_dot = new_dot
 
    draw_block(dis,food,BLOCK_SIZE)#Draw Food
    draw_snake(dis,snake,BLOCK_SIZE)#Draw Snake
    pygame.display.update()
    dis.fill((0,0,0))
    time.sleep(GAME_SPEED)
    print('Snake data : %s'%snake)
    print('Snake pos : %s , %s'%(snake_x,snake_y))
    print('Snake Lenght : %s'%len(snake))
    print('Food  %s'%food)
 
#show_game_over()
pygame.quit()
quit()