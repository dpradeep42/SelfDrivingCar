import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')#Ttack
car = pygame.image.load('tesla.png')#Car
car = pygame.transform.scale(car, (30, 60))
car_posX = 155
car_posY = 300
focus_distance = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)
    cam_x = car_posX + cam_x_offset + 15
    cam_y = car_posY + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focus_distance))[0]
    down_px = window.get_at((cam_x, cam_y + focus_distance))[0]
    right_px = window.get_at((cam_x + focus_distance, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_posX = car_posX + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_posY = car_posY + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_posX = car_posX + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:
        car_posY = car_posY - 2
    elif direction == 'right' and right_px == 255:
        car_posX = car_posX + 2
    elif direction == 'down' and down_px == 255:
        car_posY = car_posY + 2
    window.blit(track, (0, 0))
    window.blit(car, (car_posX, car_posY))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)
    pygame.display.update()