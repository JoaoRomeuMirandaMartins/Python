from JTools import rotate, repos, Jdisplay
import pygame
pygame.init()
inter = Jdisplay(pygame.display.set_mode([255, 255]), (0, 0, 0))
pygame.joystick.init()
pygame.display.set_caption("Joystick")
pygame.joystick.Joystick(0).init()
def arrowP(pos, angle, progress):
    progress = 8 - int(progress * 18)
    if progress > -2:
        shape = [[-5, progress], [-5,8], [5, 8], [5, progress]]
        shapeRed = [[-5, progress], [5, progress], [5, -2], [10, -2], [0, -10], [-10, -2], [-5, -2]]
    else:
        shape = [[-10, -2], [-5, -2], [-5, 8], [5, 8], [5, -2], [10, -2], [((10.0 + progress) * 1.25), progress], [((10.0 + progress) * -1.25), progress]]
        shapeRed = [[((10.0 + progress) * 1.25), progress], [0, -10], [((10.0 + progress) * -1.25), progress]]
    pygame.draw.polygon(inter.screen, (255, 0, 0), repos(rotate(shapeRed, angle), pos))
    pygame.draw.polygon(inter.screen, (0, 0, 255), repos(rotate(shape, angle), pos))
    pygame.draw.circle(inter.screen, (0, 255, 0), pos, 14, 1)
done = True
while done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = False
    pygame.draw.polygon(inter.screen, (255, 255, 255), [[10, 10], [10, 88], [88, 88], [88, 10]], 1)
    arrowP((50 + int(pygame.joystick.Joystick(0).get_axis(0) * 25), 50 + int(pygame.joystick.Joystick(0).get_axis(1) * 25)), 0.785398163397 * pygame.joystick.Joystick(0).get_axis(3), (1.0 - (pygame.joystick.Joystick(0).get_axis(2) + 1) * 0.5))
    inter.tick()
pygame.display.quit()
