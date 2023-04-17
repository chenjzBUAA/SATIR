import os
import cv2
import numpy as np

folder_path = 'outputs'
classnum = 8
label_path = 'labels/outputs/'

for filename in os.listdir(folder_path):
    labelimg = np.zeros((480, 720))
    for j in range(classnum + 1):
        if os.path.exists(os.path.join(folder_path, filename, str(j) + '.png')):
            img = cv2.imread(os.path.join(folder_path, filename, str(j) + '.png'), cv2.IMREAD_GRAYSCALE)
            if img.shape == (480, 720):
                labelimg[img == 255] = j + 1
    cv2.imwrite(os.path.join(label_path, filename + '.png'), labelimg.astype('uint8'))
