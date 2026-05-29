import numpy as np
import cv2

class point_operation:
    def __init__(self, img):
        self.image = img

    def add(self, num = 50):
        result = self.image.astype(np.int16) + num
        result[result > 255] = 255
        return result.astype(np.uint8)
    
    def subtract(self, num = 50):
        result = self.image.astype(np.int16) - num
        result[result < 0] = 0
        return result.astype(np.uint8)
    
    def multiply(self, num = 1.5):
        result = self.image.astype(np.float32) * num
        result[result > 255] = 255
        return result.astype(np.uint8)
    
    def divide(self, num = 1.5):
        if num == 0:
            num = 1
        result = self.image.astype(np.float32) / num
        result[result > 255] = 255
        return result.astype(np.uint8)
    
    def addimg(self, img):
        copy = self.image.copy()
        if copy.shape[0] != img.shape[0] or copy.shape[1] != img.shape[1]:
            img = cv2.resize(img, (copy.shape[1], copy.shape[0]))
        result = copy.astype(np.int16) + img.astype(np.int16)
        result[result > 255] = 255
        return result.astype(np.uint8)
    
    def subtractimg(self, img):
        copy = self.image.copy()
        if copy.shape[0] != img.shape[0] or copy.shape[1] != img.shape[1]:
            img = cv2.resize(img, (copy.shape[1], copy.shape[0]))
        result = copy.astype(np.int16) - img.astype(np.int16)
        result[result < 0] = 0
        return result.astype(np.uint8)
    
    def multiplyimg(self, img):
        copy = self.image.copy()
        if copy.shape[0] != img.shape[0] or copy.shape[1] != img.shape[1]:
            img = cv2.resize(img, (copy.shape[1], copy.shape[0]))
        result = copy.astype(np.float32) * img.astype(np.float32)
        result[result > 255] = 255
        return result.astype(np.uint8)
    
    def divideimg(self, img):
        copy = self.image.copy()
        if copy.shape[0] != img.shape[0] or copy.shape[1] != img.shape[1]:
            img = cv2.resize(img, (copy.shape[1], copy.shape[0]))
        img = img.astype(np.float32)
        img[img == 0] = 1
        result = copy.astype(np.float32) / img
        result[result > 255] = 255
        return result.astype(np.uint8)
        
    def complement(self):
        result = 255 - self.image.astype(np.int16)
        return result.astype(np.uint8)