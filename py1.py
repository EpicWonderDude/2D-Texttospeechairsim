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
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 80, 9999, 100))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(500, 0, 100, 9999))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1000, 320, 20, 100))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(750, 320, 20, 100))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 320, 20, 100))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(500, 620, 100, 20))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(300, 80, 20, 100))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(500, 220, 100, 20))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(750, 80, 20, 100))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(1050, 80, 20, 100))
    pygame.draw.circle(screen, (0, 0, 255), player_pos, 20)
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
    
    
    if direction == "up" and (player_pos.y > 340 or (player_pos.x > 490 and player_pos.x < 610)):
        player_pos.y -= 5
    if direction == "up" and player_pos.y == 20:
        player_pos.y += 5
    


    if direction == "down" and (player_pos.y < 400 or (player_pos.x > 500 and player_pos.x < 600)):
        player_pos.y += 5
    if direction == "down" and player_pos.y == 700:
        player_pos.y -= 5
    if direction == "down" and (player_pos.y == 160 and (player_pos.x  > 0 and player_pos.x  < 520)):
        player_pos.y -= 5
    if direction == "down" and (player_pos.y == 160 and (player_pos.x  > 580 and player_pos.x  < 1280)):
        player_pos.y -= 5
    
    
    if direction == "left":
        player_pos.x -= 5
    if direction == "left" and player_pos.x == 520 and (player_pos.y  > 400 and player_pos.y < 700):
        player_pos.x += 5
    if direction == "left" and player_pos.x == 520 and (player_pos.y  < 340 and player_pos.y > 160):
        player_pos.x += 5
    if direction == "left" and player_pos.x == 520 and (player_pos.y  < 100 and player_pos.y > 0):
        player_pos.x += 5
    if direction == "left" and player_pos.x == 20:
        player_pos.x += 5


    if direction == "right":
        player_pos.x += 5
    if direction == "right" and player_pos.x == 580 and (player_pos.y > 400 and player_pos.y < 700):
        player_pos.x -= 5
    if direction == "right" and player_pos.x == 580 and (player_pos.y < 100 and player_pos.y > 0):
        player_pos.x -= 5
    if direction == "right" and player_pos.x == 1260:
        player_pos.x -= 5
    if direction == "right" and player_pos.x == 580 and (player_pos.y  < 340 and player_pos.y > 160):
        player_pos.x -= 5
    