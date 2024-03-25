import pygame
import numpy as np
from random import randint

pygame.init()
pygame.font.init() 

Screen_Size = (1280,720)
screen = pygame.display.set_mode(Screen_Size)
pygame.display.set_caption("Top Down Shooter")

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)
plusFont = pygame.font.Font('freesansbold.ttf', 25)

TriDist = 10
Center = (Screen_Size[0]/2, Screen_Size[1]/2)

PlayerPos = Center
PlayerHealth = 100
Speed = 1.5
Dx = 0
Dy = 0

Enemies = [(100, (25, 25))]

Bullets = []
BulletSpeed = 5
BulletCooldown = 0
BulletCooldownMax = 10

HealthPowerups = []

Score = 0

def add_tuple(a, b, sign="+"):
    return tuple(map(lambda i, j: eval(f"{i}{sign}{j}"), a, b))

def Clamp(value, max, min=0):
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value

def draw_triangle_with_target(center, target, radius, color):
    dx = target[0] - center[0]
    dy = target[1] - center[1]
    angle_to_mouse = np.arctan2(dy, dx)

    triangle_points = np.array([[0, -radius / 2],
                                 [radius, 0],
                                 [0, radius / 2]])
    rotation_matrix = np.array([[np.cos(angle_to_mouse), -np.sin(angle_to_mouse)],
                                 [np.sin(angle_to_mouse), np.cos(angle_to_mouse)]])

    rotated_triangle = np.dot(triangle_points, rotation_matrix.T) + center

    pygame.draw.polygon(screen, color, rotated_triangle)

def move_towards(current_pos, target_pos, speed):
    direction = (target_pos[0] - current_pos[0], target_pos[1] - current_pos[1])
    distance = ((target_pos[0] - current_pos[0])**2 + (target_pos[1] - current_pos[1])**2)**0.5
    movement = (direction[0] / distance * speed, direction[1] / distance * speed)
    new_pos = (current_pos[0] + movement[0], current_pos[1] + movement[1])
    
    return new_pos

def move_direction(current_pos, direction, speed):
    direction = ((current_pos[0] + direction[0]) - current_pos[0], (current_pos[1] + direction[1]) - current_pos[1])
    distance = (((current_pos[0] + direction[0]) - current_pos[0])**2 + ((current_pos[1] + direction[1]) - current_pos[1])**2)**0.5
    movement = (direction[0] / distance * speed, direction[1] / distance * speed)
    new_pos = (current_pos[0] + movement[0], current_pos[1] + movement[1])
    
    return new_pos

while True:
    # Get Mouse Position
    MousePosition = pygame.mouse.get_pos()
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        # Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Dx-=1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Dx+=1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Dy-=1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Dy+=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Dx+=1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Dx-=1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Dy+=1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Dy-=1
        # Bullet Firing
        if pygame.mouse.get_pressed()[0] and BulletCooldown <= 0:
            BulletCooldown = BulletCooldownMax
            direction = (MousePosition[0] - PlayerPos[0], MousePosition[1] - PlayerPos[1])
            distance = ((MousePosition[0] - PlayerPos[0])**2 + (MousePosition[1] - PlayerPos[1])**2)**0.5
            Bullets.append(((PlayerPos, (direction[0] / distance * Speed, direction[1] / distance * Speed), 250)))
    # Firing Cooldown
    if BulletCooldown > 0:
        BulletCooldown-=1

    # Do logical updates here.
    PlayerPos = add_tuple(PlayerPos, add_tuple((Clamp(Dx, 1, -1), Clamp(Dy, 1, -1)), (Speed, Speed), "*"))
    PlayerPos = (Clamp(PlayerPos[0], Screen_Size[0]), Clamp(PlayerPos[1], Screen_Size[1]))

    # Enemy Killing
    for enemy in Enemies:
        index = Enemies.index(enemy)
        Enemies[index] = (enemy[0], move_towards(enemy[1], PlayerPos, Speed))
        enemy = Enemies[index]
        if enemy[0] <= 0:
            if enemy in Enemies:
                Enemies.remove(enemy)
                Score += 100
    
    # Bullet Destruction
    for bullet in Bullets:
        index = Bullets.index(bullet)
        Bullets[index] = (move_direction(bullet[0], bullet[1], BulletSpeed), bullet[1], bullet[2] - 1)
        if Bullets[index][2] <= 0:
            Bullets.remove(Bullets[index])
    
    # Bullet Collision
    for enemy in Enemies:
        for bullet in Bullets:
            rect1 = pygame.Rect(*enemy[1], 25, 25)
            rect2 = pygame.Rect(*bullet[0], 10, 10)
            collide = rect1.colliderect(rect2)
            if collide:
                if bullet in Bullets:
                    Bullets.remove(bullet)
                if enemy in Enemies:
                    index = Enemies.index(enemy)
                    Enemies[index] = (enemy[0]-50, enemy[1])

    # Enemy Attack Collision
    for enemy in Enemies:
        enemyPos = enemy[1]
        rect1 = pygame.Rect(*enemyPos, 25, 25)
        rect2 = pygame.Rect(*PlayerPos, 25, 25)
        collide = rect1.colliderect(rect2)
        if collide:
            PlayerHealth -= 25
            direction = (enemyPos[0] - PlayerPos[0], enemyPos[1] - PlayerPos[1])
            distance = ((enemyPos[0] - PlayerPos[0])**2 + (enemyPos[1] - PlayerPos[1])**2)**0.5
            PlayerPos = add_tuple(PlayerPos, (direction[0] / distance * 50, direction[1] / distance * 50), "-")
            if PlayerHealth <= 0:
                Score = 0
                PlayerPos = Center
                PlayerHealth = 100
                Enemies.clear()
                Bullets.clear()
    
    # Power Up Collision
    for powerUp in HealthPowerups:
        rect1 = pygame.Rect(*powerUp, 25, 25)
        rect2 = pygame.Rect(*PlayerPos, 25, 25)
        collide = rect1.colliderect(rect2)
        if collide:
            HealthPowerups.remove(powerUp)
            Score += 50
            PlayerNewHealth = PlayerHealth + 25
            PlayerHealth = PlayerNewHealth if PlayerHealth < 100 else 100

    # Enemy Spawning
    SpawnMax = 150
    if randint(0, SpawnMax) == SpawnMax and len(Enemies) < 10:
        Side = randint(1, 4)
        if Side == 1: # Top
            Enemies.append((100, (randint(0, Screen_Size[0]), 0)))
        elif Side == 2: # Bottom
            Enemies.append((100, (randint(0, Screen_Size[0]), Screen_Size[1])))
        elif Side == 3: # Left
            Enemies.append((100, (0, randint(0, Screen_Size[1]))))
        elif Side == 4: # Right
            Enemies.append((100, (Screen_Size[0], randint(0, Screen_Size[1]))))
    
    # Health Powerup Spawning
    SpawnMax = 500
    if randint(0, SpawnMax) == SpawnMax and len(HealthPowerups) < 3:
        HealthPowerups.append((randint(25, Screen_Size[0]-25), randint(25, Screen_Size[1]-25)))

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    for enemy in Enemies:
        draw_triangle_with_target(enemy[1], PlayerPos, 25, (255, 0, 0))
    for bullet in Bullets:
        draw_triangle_with_target(bullet[0], add_tuple(bullet[0], bullet[1]), 10, (255, 0, 0))
    for powerUp in HealthPowerups:
        text = plusFont.render("+", True, (0, 255, 0))
        screen.blit(text, powerUp)
    
    draw_triangle_with_target(PlayerPos, pygame.mouse.get_pos(), 25, (0, 255, 255))

    text = font.render("Score: " + str(Score), True, (255, 255, 255))
    screen.blit(text, (10,0))

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)