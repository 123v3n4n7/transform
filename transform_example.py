from transform import four_point_transform
import numpy as np
import argparse
import cv2  # opencv-python библиотека

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")  # путь к изображению
ap.add_argument("-c", "--coords", help="comma seperated list of source points")  # список из 4 точек представяющих
# область изображения, которую мы хотим получить.
# python3 transform_example.py --image test.png --coords "[(73, 247), (374, 117), (499, 271), (193, 463)]"

args = vars(ap.parse_args())  # возвращает словарь из атрибута

image = cv2.imread(args['image'])
pts = np.array(eval(args['coords']), dtype='float32')  # eval -- выполняет выражение


warped = four_point_transform(image, pts)

cv2.imshow('Original', image)
cv2.imshow('Warped', warped)
cv2.waitKey(0)
