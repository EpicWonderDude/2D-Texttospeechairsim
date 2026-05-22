import pygame
import speech_recognition as sr

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Voice Control Game")

clock = pygame.time.Clock()

running = True
player_pos = pygame.Vector2(1100, 320)
direction = "left"
score = 0

print("Score:", score)


def stringparse(text):

    text = text.lower()

    if "up" in text:
        return "up"

    if "down" in text:
        return "down"

    if "left" in text:
        return "left"

    if "right" in text:
        return "right"

    return None


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard press
        if event.type == pygame.KEYDOWN:

            # Push-to-talk with SPACE
            if event.key == pygame.K_SPACE:

                r = sr.Recognizer()

                try:
                    with sr.Microphone() as source:

                        print("Speak now...")
                        audio = r.listen(source, phrase_time_limit=3)

                    text = r.recognize_google(audio)

                    print("You said:", text)

                    voice_direction = stringparse(text)

                    if voice_direction is not None:
                        direction = voice_direction

                except Exception as e:
                    print("Could not understand audio")
                    print(e)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        direction = "up"

    if keys[pygame.K_DOWN]:
        direction = "down"

    if keys[pygame.K_LEFT]:
        direction = "left"

    if keys[pygame.K_RIGHT]:
        direction = "right"

    if direction == "up" and (
        player_pos.y > 340
        or (490 < player_pos.x < 610)
    ):
        player_pos.y -= 5

    if direction == "up" and player_pos.y <= 20:
        player_pos.y += 5

    if direction == "down" and (
        player_pos.y < 400
        or (500 < player_pos.x < 600)
    ):
        player_pos.y += 5

    if direction == "down" and player_pos.y >= 700:
        player_pos.y -= 5

    if direction == "down" and (
        player_pos.y == 160
        and (0 < player_pos.x < 520)
    ):
        player_pos.y -= 5

    if direction == "down" and (
        player_pos.y == 160
        and (580 < player_pos.x < 1280)
    ):
        player_pos.y -= 5

    if direction == "left":
        player_pos.x -= 5

    if direction == "left" and (
        515 <= player_pos.x <= 525
        and (400 < player_pos.y < 700)
    ):
        player_pos.x += 5

    if direction == "left" and (
        515 <= player_pos.x <= 525
        and (160 < player_pos.y < 340)
    ):
        player_pos.x += 5

    if direction == "left" and (
        515 <= player_pos.x <= 525
        and (0 < player_pos.y < 100)
    ):
        player_pos.x += 5

    if direction == "left" and player_pos.x <= 20:
        player_pos.x += 5

    if direction == "right":
        player_pos.x += 5

    if direction == "right" and (
        575 <= player_pos.x <= 585
        and (400 < player_pos.y < 700)
    ):
        player_pos.x -= 5

    if direction == "right" and (
        575 <= player_pos.x <= 585
        and (0 < player_pos.y < 100)
    ):
        player_pos.x -= 5

    if direction == "right" and player_pos.x >= 1260:
        player_pos.x -= 5

    if direction == "right" and (
        575 <= player_pos.x <= 585
        and (160 < player_pos.y < 340)
    ):
        player_pos.x -= 5

    # -----------------------------
    # Scoring
    # -----------------------------
    if abs(player_pos.x - 1000) < 5:
        score += 1
        print("Score:", score)

    if abs(player_pos.x - 750) < 5:
        score += 1
        print("Score:", score)

    if abs(player_pos.y - 220) < 5:
        score += 1
        print("Score:", score)

    if abs(player_pos.x - 1050) < 5:
        score += 1
        print("Score:", score)

    if abs(player_pos.x - 200) < 5:
        score -= 1
        print("Score:", score)

    if abs(player_pos.y - 620) < 5:
        score -= 1
        print("Score:", score)

    if abs(player_pos.x - 300) < 5:
        score -= 1
        print("Score:", score)

    screen.fill((218, 160, 109))

    pygame.draw.rect(screen, (100, 100, 100),
                     pygame.Rect(0, 320, 9999, 100))

    pygame.draw.rect(screen, (100, 100, 100),
                     pygame.Rect(0, 80, 9999, 100))

    pygame.draw.rect(screen, (100, 100, 100),
                     pygame.Rect(500, 0, 100, 9999))

    # Green zones
    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(1000, 320, 20, 100))

    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(750, 320, 20, 100))

    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(500, 220, 100, 20))

    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(750, 80, 20, 100))

    pygame.draw.rect(screen, (0, 255, 0),
                     pygame.Rect(1050, 80, 20, 100))

    # Red zones
    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(200, 320, 20, 100))

    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(500, 620, 100, 20))

    pygame.draw.rect(screen, (255, 0, 0),
                     pygame.Rect(300, 80, 20, 100))

    triangle_points = [
        (player_pos.x, player_pos.y - 20),
        (player_pos.x - 20, player_pos.y + 20),
        (player_pos.x + 20, player_pos.y + 20)
    ]

    pygame.draw.polygon(screen, (255, 255, 255), triangle_points)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()