# MIT License

import math, random

### Generates a heightmap without recursion
def generate(size, max_height, factor_height):
	# get next power of 2
	next_power = math.ceil(math.log2(size))
	screen_w = screen_h = 2**next_power
	
	# setup iterations from screens
	iterations = int(round(math.log(screen_w-1, 2), 0))
	
	# heightmap setup
	heightmap = []
	heightmap.append([255, 255])
	heightmap.append([255, 255])
	
	print(f'{heightmap}\n')
	
	# configurations for heightmap
	# factor_height = 0.71 # controls the roughness
	factor_count = 1.0 
	
	# iterate through map
	for pass_iter in range(iterations):
	    loop_passes = 2**pass_iter
	    
	    for pass_y in range(loop_passes):
	        y_offset = pass_y * 2
	        
	        for pass_x in range(loop_passes):
	            x_offset = pass_x * 2
	
	            if pass_y == 0:
	                heightmap.insert(x_offset+1, [])
	
				# square + diamond step
	            c1 = heightmap[x_offset][y_offset]
	            c2 = heightmap[x_offset+2][y_offset]
	            c3 = heightmap[x_offset+2][y_offset+1]
	            if x_offset == 0:
	                c4 = heightmap[x_offset][y_offset+1]
	            else:
	                c4 = heightmap[x_offset][y_offset+2]
	
	            random_height =  int(max_height * factor_count)
	
	            mid_point = ((c1 + c2 + c3 + c4) / 4) + random.randint(-random_height, random_height)
	
	            c1c2 = ((c1 + c2) /2)
	            c2c3 = ((c2 + c3) /2)
	            c3c4 = ((c3 + c4) /2)
	            c4c1 = ((c4 + c1) /2)
	            
	            if y_offset == 0:
	                heightmap[x_offset+1].append(c1c2)
	            if x_offset == 0:
	                heightmap[x_offset].insert(y_offset+1, c4c1)
	
				# append points
	            heightmap[x_offset+1].append(mid_point)
	            heightmap[x_offset+1].append(c3c4)
	            heightmap[x_offset+2].insert(y_offset+1, c2c3)
	    # factor count to generate roughness
	    print(f'{factor_count}')
	    factor_count *= factor_height
	    
	# debug for testing accurate map gen
	print_hold = ""
	for y_pos in range(screen_h): 
	    for x_pos in range(screen_w):
	        pass
	        #print_hold += str(heightmap[x_pos][y_pos]) + " "
	    # print print_hold
	    print_hold = ""
	    
	return heightmap
        

