import pygame
import os
import math
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Clock")


clock_face = pygame.image.load("mainclock.png")
minute_hand = pygame.image.load("rightarm.png")
second_hand = pygame.image.load("leftarm.png")


clock_center = (400, 400)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))


    screen.blit(clock_face, (0, 0))

    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second


    minute_angle = -math.radians((minute+8) * 6) 
    second_angle = -math.radians(second * 6)  


    rotated_minute_hand = pygame.transform.rotate(minute_hand, math.degrees(minute_angle))
    rotated_second_hand = pygame.transform.rotate(second_hand, math.degrees(second_angle))
    clock_face_rect = clock_face.get_rect(center=clock_center)
    screen.blit(clock_face, clock_face_rect)

    minute_hand_rect = rotated_minute_hand.get_rect(center=clock_center)
    second_hand_rect = rotated_second_hand.get_rect(center=clock_center)

    screen.blit(rotated_minute_hand, minute_hand_rect)
    screen.blit(rotated_second_hand, second_hand_rect)

  
    pygame.display.flip()

   
    pygame.time.Clock().tick(60)


pygame.quit()
