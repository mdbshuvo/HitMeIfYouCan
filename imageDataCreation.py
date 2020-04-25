import numpy
import qimage2ndarray
from PyQt5.QtGui import QPainter, QImage
from PyQt5.Qt import Qt
import cv2
from tqdm import tqdm

# constant from game
screenWidth = 800
screenHeight = 600

fieldHeight = 50
fieldColor = Qt.green
barHeight = 160
barWidth = 20
barPosX = (screenWidth // 2) - (barWidth // 2)
barPosY = screenHeight - fieldHeight - barHeight

player1limitX = (0, barPosX - barWidth)          #player width == bar width
player2limitX = (barPosX + barWidth, screenWidth - barWidth)

player1AngleLimit = (0, 84)
player2AngleLimit = (96, 180)

playerHeight = barHeight // 3 * 2
playerWidth = barWidth

playerY = screenHeight - fieldHeight - playerHeight

playerColor = Qt.black
playerMove = 5

stoneHeight = 10
stoneWidth = 10
stoneColor = Qt.red
stoneY = playerY - stoneHeight

imageCrop = 300
imageResize = (80,30)

# till here


all_data = numpy.load('modelData.npy')
#all_data = all_data[10:20]

img_data = []
output = []

image = QImage(screenWidth, screenHeight, QImage.Format_RGB32)
painter = QPainter(image)

for data in tqdm(all_data):
    target_dist = data[0]
    bar_dist = data[1]
    
    player1X = barPosX - bar_dist
    player2X = player1X + target_dist
    stoneX = player2X + playerWidth - stoneWidth
    
    #draw
    image.fill(Qt.white)

    painter.fillRect(0, screenHeight - fieldHeight,
                           screenWidth, fieldHeight, fieldColor)
    painter.fillRect(barPosX, barPosY, barWidth,
                  barHeight, fieldColor)

    painter.fillRect(player1X, playerY, playerWidth,
                      playerHeight, playerColor)
    painter.fillRect(player2X, playerY, playerWidth,
                      playerHeight, playerColor)
    painter.fillRect(stoneX, stoneY, stoneWidth,
                      stoneWidth, stoneColor)

#    image.save('images\\' + str(data[:2]) + '.jpg')
    arr_image = qimage2ndarray.byte_view(image)
#    cv2.imshow('a', arr_image)
    cropped_image = arr_image[imageCrop:]
    resized_image = cv2.resize(cropped_image, imageResize)
#    cv2.imwrite('images\\' + str(data[:2]) + '.jpg', resized_image)
    
    img_data.append(resized_image)
    output.append([180 - data[2], data[3]])

savedData = [img_data, output]
    
print('saving the data...')
print('Please wait...')
numpy.save('modelImageData.npy', savedData)
print('saved successfully!!')