import random
import numpy
import math
import tensorflow as tf
from tqdm import tqdm

SIZE = 100000

max_v = 100
max_angle = 90

min_dis = 15
max_dis = 900

min_bar_dis = 10
max_bar_dis = 400
bar_height = 160

# from game
screenWidth = 800
screenHeight = 600

barHeight = 160
barWidth = 20
barPosX = (screenWidth // 2) - (barWidth // 2)
player1limitX = (0, barPosX - barWidth)
player2limitX = (barPosX + barWidth, screenWidth - barWidth)

# till

step_factor = 5

final_data = []

g = 9.8

positions = []

pos1 = player1limitX[0]

# how much data
step = 5

while pos1 <= player1limitX[1]:
    pos2 = player2limitX[0]
    while pos2 <= player2limitX[1]:
        # near the bar computer needs more data (giving 4x)
#        if pos1 >= barPosX - 40:
#            for i in range(3):
#                positions.append([pos1, pos2])
                
        positions.append([pos1, pos2])
        
        pos2 += step
    pos1 += step
count = 0
for pos1, pos2 in tqdm(positions): 
    target = pos2 - pos1
    bar_dist = barPosX - pos1
    
    minAngle = math.atan((bar_height + 20) / (bar_dist - bar_dist * bar_dist / target)) * 180 / math.pi
    maxAngle = 90 - 0.5 * math.asin(g * target / (max_v * max_v)) * 180 / math.pi
    
    angle = (minAngle + maxAngle) / 2
    
    radian_angle = angle * numpy.pi / 180
    t = numpy.sqrt((2 * target * numpy.tan(radian_angle)) / g)
    velocity = target / (t * numpy.cos(radian_angle))
    
    index = random.randint(0,count)
    final_data.insert(index, [target, bar_dist, angle, velocity])
    count += 1

numpy.save('modelData.npy', final_data)
    
        
    