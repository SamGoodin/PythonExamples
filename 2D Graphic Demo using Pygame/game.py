import pygame
from pygame.locals import *


def main():
    pygame.init()

    # Setup the display with x and y size
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

    # Set the pygame window name
    pygame.display.set_caption("2D Graphic Demo")

    # Set the clock obj for controlling game time
    clock = pygame.time.Clock()

    # Create font obj of size
    font = pygame.font.SysFont('Comic Sans MS', 24)

    # Create text surface obj
    # font.render(text, antialias, color)
    text = "Edit by typing"
    textObj = font.render(text, True, (0, 0, 0))

    image = pygame.image.load('sand.jpg')

    button = pygame.Rect(50, 500, 100, 50)
    btnOnOff = 'On'

    def drawImage(img, x, y):
        screen.blit(img, (x, y))

    def rotateImage(img, angle, x, y):
        rotatedImage = pygame.transform.rotate(img, angle)
        newRect = rotatedImage.get_rect(center=img.get_rect(center=(x, y)).center)
        return rotatedImage, newRect

    def drawRotatedImage(img, angle, x, y):
        rotatedImage, newRect = rotateImage(img, angle, x, y)
        screen.blit(rotatedImage, newRect)

    def rescaleImage(img, xsize=None, ysize=None):
        if xsize and ysize:
            return pygame.transform.scale(img, (xsize, ysize))
        elif xsize and not ysize:
            return pygame.transform.scale(img, xsize)
        elif ysize and not xsize:
            return pygame.transform.scale(img, ysize)
        else:
            return pygame.transform.scale(img, (500, 500))

    def drawScaledImg(img, xpos, ypos, xsize=None, ysize=None):
        image = rescaleImage(img, xsize, ysize)
        drawImage(image, xpos, ypos)

    xSize, ySize, rotation = 1, 1, 5
    # Run until the user asks to quit
    running = True
    drawFunction = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                else:
                    text += event.unicode
                textObj = font.render(text, True, (0, 0, 0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    if drawFunction:
                        btnOnOff = 'On'
                        drawFunction = None
                    else:
                        btnOnOff = 'Off'
                        drawFunction = drawScaledImg

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        pygame.draw.line(screen, (255, 0, 0), (50, 50), (100, 100), 2)
        # To fill shape, remove width from end of parameters
        pygame.draw.rect(screen, (0, 255, 0), (50, 200, 100, 50), 2)
        pygame.draw.ellipse(screen, (0, 0, 255), (150, 75, 160, 100))

        if drawFunction:
            if drawFunction.__name__.__contains__("Scaled"):
                drawFunction(image, 350, 0, xSize, ySize)
                # Stops the image from growing past the window bounds
                if xSize < screen.get_width() and ySize < screen.get_height():
                    xSize += 1
                    ySize += 1
            if drawFunction.__name__.__contains__("Rotated"):
                drawFunction(image, rotation, 350, 0)
                rotation += 1

        screen.blit(textObj, (50, 300))

        pygame.draw.rect(screen, (255, 0, 0), button)
        buttonTxt = font.render(btnOnOff, True, (255, 255, 255))
        screen.blit(buttonTxt, (78, 507))

        # flip will update the contents of the entire display
        #pygame.display.flip()

        # display.update() allows to update a portion of the screen, instead
        # of the entire area of the screen. Passing no args, updates the entire display
        # -can be faster than flip but only updates certain portions of screen
        pygame.display.update()

        # 60 frames per second
        clock.tick(60)

    # Done! Time to quit.
    pygame.quit()


if __name__ == '__main__':
    main()
