import cv2
import numpy as np
from .Image_segmentation import thresholding

class morphology:
    def __init__(self, img):
        self.image = img
        self.seg = self.__seg()

    def __seg(self):
        seg = thresholding(self.image)
        result = seg.globalthresholding()
        return result

    def dilation(self, x=3, y=3, img=None):
        if img is None:
            img = self.seg
        kernel = np.ones((x, y), np.uint8)
        result = cv2.dilate(img, kernel, iterations=1)
        return result

    def erosion(self, x=3, y=3, img=None):
        if img is None:
            img = self.seg
        kernel = np.ones((x, y), np.uint8)
        result = cv2.erode(img, kernel, iterations=1)
        return result

    def internal(self, x=3, y=3):
        result = self.seg - self.erosion(x, y)
        return result

    def external(self, x=3, y=3):
        result = self.dilation(x, y) - self.seg
        return result

    def gradient(self, x=3, y=3):
        result = self.dilation(x, y) - self.erosion(x, y)
        return result
    
    def closing(self, x=3, y=3):
        result = self.erosion(x, y, self.dilation(x, y))
        return result

    def opening(self, x=3, y=3):
        result = self.dilation(x, y, self.erosion(x, y))
        return result