import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(1200, 370)
direction = "left"
while running:#

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, 320, 9999, 100))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(500, 0, 100, 9999))
    pygame.draw.circle(screen, (255, 00, 00), player_pos, 30)
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
    if direction == "up":
        player_pos.y -= 5
    if direction == "down":
        player_pos.y += 5
    if direction == "left":
        player_pos.x -= 5
    if direction == "right":
        player_pos.x += 5
