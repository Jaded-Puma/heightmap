#!/usr/bin/env python3

### Render a map generated without recursion
### by Esteban RPM (Jaded Puma)

# MIT License

import pygame, os
import heightmap2d

### MAIN ###
def main():
	
	# generate height map
	heightmap = heightmap2d.generate(512, 255, 0.71)
	
	# color map on screen
	for x_pos in range(screen_size):
	    for y_pos in range(screen_size): 
	        
	        if heightmap[x_pos][y_pos] > 510:
	            colorVal = (127, 255, 0)
	        elif heightmap[x_pos][y_pos] < 0:
	            colorVal = (0, 0, 0)
	        elif heightmap[x_pos][y_pos] < 255:
	            colorVal = (0, 0, heightmap[x_pos][y_pos])
	        else:
	            colorVal = (heightmap[x_pos][y_pos]/2-127, heightmap[x_pos][y_pos]/2, 0)
	        screen.set_at((x_pos, y_pos), colorVal)

	# draw screen
	pygame.display.flip()
	
	# run app window
	program_run = True
	while program_run:
	
	    clock.tick(FPS)
	
	    ### events ###
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            program_run = False

# entry point
if __name__ == '__main__':
	# configuration
	screen_size = 512
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	screen = pygame.display.set_mode((screen_size, screen_size))
	clock = pygame.time.Clock()
	FPS = 5
	bgColor = (255, 0, 0)
	
	# run app
	main()
