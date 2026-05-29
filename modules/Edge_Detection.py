import cv2
import numpy as np
import ctypes
import numpy
import os

class edge:
    def __init__(self, img):
        self.image = img
        self.i = ctypes.c_int
        self.ptr = ctypes.POINTER(ctypes.c_uint8)
        self.p = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), "help.dll"))

    def sobel(self):
        result = self.image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        x = cv2.Sobel(result, cv2.CV_64F, 1, 0, ksize=3)
        y = cv2.Sobel(result, cv2.CV_64F, 0, 1, ksize=3)
        result = np.sqrt(x**2 + y**2)
        result = np.clip(result, 0, 255)
        result = result.astype(np.uint8)
        return result.astype(np.uint8)
    
    def prewitt(self):
        row, col = self.image.shape[:2]
        temp = self.image.copy()
        temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
        result = np.zeros(temp.shape, dtype=np.float32)
        func = self.p.cprewitt
        func.argtypes = [self.ptr, self.ptr, self.i, self.i]
        func.restype = None
        img = np.ascontiguousarray(temp, dtype=np.uint8)
        pimg = img.ctypes.data_as(self.ptr)
        result = np.ascontiguousarray(result, dtype=np.uint8)
        res = result.ctypes.data_as(self.ptr)
        func(pimg, res, row, col)
        return result.astype(np.uint8)
    
    def roberts(self):
        row, col = self.image.shape[:2]
        temp = self.image.copy()
        temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
        result = np.zeros(temp.shape, dtype=np.float32)
        func = self.p.croberts
        func.argtypes = [self.ptr, self.ptr, self.i, self.i]
        func.restype = None
        img = np.ascontiguousarray(temp, dtype=np.uint8)
        pimg = img.ctypes.data_as(self.ptr)
        result = np.ascontiguousarray(result, dtype=np.uint8)
        res = result.ctypes.data_as(self.ptr)
        func(pimg, res, row, col)
        return result.astype(np.uint8)