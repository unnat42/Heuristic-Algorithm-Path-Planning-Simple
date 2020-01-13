# Upgrade by adding obstacle points: Define them 
# Another expansion is to also add diagonal movement. Current Version only has a step movement in either axis at once
# Created by Unnat Antani 

import matplotlib.pyplot as plt
import math


#Define the heuristic distance calculator function 

def calc_dir_heur(new_pos_right,new_pos_left,new_pos_up,new_pos_down,final_pos,obstacle):
    dist = []
   # print(obstacle)
    
    right = ([final_pos[0] - new_pos_right[0],final_pos[1]-new_pos_right[1]])
    for i in range(len(obstacle)):
        # print(obstacle[i])
        if new_pos_right==obstacle[i]:
            dist.append(math.inf)
            break
        if i==(len(obstacle)-1):
             dist.append(math.sqrt((right[0]**2)+(right[1]**2)))  
             
    down = ([final_pos[0] - new_pos_down[0],final_pos[1]-new_pos_down[1]])
    for i in range(len(obstacle)):
        
        if new_pos_down==obstacle[i]:
            dist.append(math.inf)
            break
        if i==(len(obstacle)-1):
            dist.append(math.sqrt((down[0]**2)+(down[1]**2))) 
            
    left = ([final_pos[0] - new_pos_left[0],final_pos[1]-new_pos_left[1]])
    for i in range(len(obstacle)):
        
        if new_pos_left ==obstacle[i]:
            dist.append(math.inf)
            break
        if i==(len(obstacle)-1):
            dist.append(math.sqrt((left[0]**2)+(left[1]**2))) 
    
    up = ([final_pos[0] - new_pos_up[0],final_pos[1]-new_pos_up[1]])
    for i in range(len(obstacle)):
        
        if new_pos_up ==obstacle[i]:
            dist.append(math.inf)
            break
        if i==(len(obstacle)-1):
            dist.append(math.sqrt((up[0]**2)+(up[1]**2)))    
    #print(dist)
    ind_min = dist.index(min(dist))

    if ind_min ==0:
        new_pos = new_pos_right
    elif ind_min == 1:
        new_pos = new_pos_down
    elif ind_min == 2:
        new_pos = new_pos_left
    elif ind_min == 3:
        new_pos = new_pos_up
        
    return new_pos
##########################################################################

x_points = list(range(0,102))
y_points = list(range(0,102))
x = []
y = []
grid = []
k = 0


for i in range(len(x_points)):
    for j in range(len(y_points)):
         grid.append((x_points[i],y_points[j])) 
# print(grid)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

for _ in grid:
    x.append(_[0])
    y.append(_[1])
    
####################Obstacle point generation#####################

obstacle = []
obstacle_x = []
obstacle_y = []

#Deifning Rectangle 
for i in range(30,71,1):
    for j in range(20,41,1):
        obstacle.append([i,j])

#Defining circle with radius 10 and centre at (30,60)        
for i in range(20,41,1):
    for j in range(50,71,1):
        if (((30-i)**2)+((60-j)**2))<=100:
            obstacle.append([i,j])

for _ in obstacle:
    obstacle_x.append(_[0])
    obstacle_y.append(_[1])
    
    

#########################################################
    
    
init_pos = [0,60] # or anything you want
final_pos = [100,0]   #Plug in the final_position or goal position
path = []
path.append(init_pos)

while True:
    new_pos_right = [init_pos[0]+(1),init_pos[1]]
    new_pos_left = [init_pos[0]-(1),init_pos[1]]
    new_pos_up = [init_pos[0],init_pos[1]+(1)]
    new_pos_down = [init_pos[0],init_pos[1]-(1)]
    
    init_pos = calc_dir_heur(new_pos_right,new_pos_left,new_pos_up,new_pos_down,final_pos, obstacle)
    path.append(init_pos)
    if init_pos == final_pos:
        break
    


path_x =[]
path_y = []

for i in path:
    path_x.append(i[0])
    path_y.append(i[1])
    
plt.scatter(x,y,color = 'r')
plt.scatter(obstacle_x,obstacle_y,color = 'g')

plt.scatter(path_x,path_y,color = 'b')

ax.set_xlabel("X-Axis")

ax.set_ylabel("Y-Axis")

plt.show()
    