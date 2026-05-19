import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(1200, 370)
direction = "left"
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((218, 160, 109))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 320, 9999, 100))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(500, 0, 100, 9999))
    pygame.draw.circle(screen, (255, 0, 0), player_pos, 20)
    pygame.display.flip()
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = "up"
    if keys[pygame.K_DOWN]:
        direction = "down"
    if keys[pygame.K_LEFT]:
        direction = "left"
    if keys[pygame.K_RIGHT]:
        direction = "right"
    if direction == "up" and (player_pos.y > 350 or (player_pos.x > 490 and player_pos.x < 610)):
        player_pos.y -= 5
    if direction == "down" and (player_pos.y < 390 or (player_pos.x > 490 and player_pos.x < 610)):
        player_pos.y += 5
    if direction == "left":
        player_pos.x -= 5
    if direction == "left" and player_pos.x == 520 and (player_pos.y  > 420 and player_pos.y < 690):
        player_pos.x += 5
    if direction == "left" and player_pos.x == 520 and (player_pos.y  < 320 and player_pos.y > 200):
        player_pos.x += 5
        


    if direction == "right":
        player_pos.x += 5
    if direction == "right" and player_pos.x == 580 and (player_pos.y > 420 and player_pos.y < 690):
        player_pos.x -= 5
    if direction == "right" and player_pos.x == 580 and (player_pos.y < 320 and player_pos.y > 20):
        player_pos.x -= 5
    