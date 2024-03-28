import pygame
import os
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Music Player")


done = False
current_song_index = 0
songs = ["Battlecry.mp3", "Aruarian Dance.mp3", "Just Forget.mp3"]  
current_song = songs[current_song_index]

pygame.mixer.init()


pygame.mixer.music.load(current_song)


font = pygame.font.Font(None, 25)


pygame.mixer.music.play()

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)  
                current_song = songs[current_song_index]
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs) 
                current_song = songs[current_song_index]
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():  
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    screen.fill((0, 0, 0))

   
    

    text = font.render(f"Now playing: {current_song}", True, (0, 250, 250))
    screen.blit(text, (5, 10))

    text = font.render(f"To stop music press Subspace", True, (255, 99, 71))
    screen.blit(text, (5, 50))

    text = font.render(f"To switch music press -> or <-", True, (128, 0, 128))
    screen.blit(text, (5, 100))

    time_seconds = pygame.mixer.music.get_pos() // 1000
    minutes = time_seconds // 60
    seconds = time_seconds % 60 

    text_time = font.render(f"Time of playing: {minutes:02d}:{seconds:02d}", True, (250, 250,0))
    screen.blit(text_time, (150, 250))

    pygame.display.flip()

   
    clock.tick(60)

pygame.quit()
