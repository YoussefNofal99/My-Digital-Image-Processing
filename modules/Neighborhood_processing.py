import os
import ctypes
import cv2
import numpy as np

class Linear_filter:
    def __init__(self, img):
        self.image = img

    def averagefilter(self, x=3, y=3):
        kernel = np.ones((x, y), dtype=np.float32) / (x * y)
        result = cv2.filter2D(self.image, -1, kernel)
        return result.astype(np.uint8)
    
    def laplacianfilter(self, k=True):
        if k:
            kernel = np.array([[0, -1, 0], 
                               [-1, 4, -1], 
                               [0, -1, 0]])
        else:
            kernel = np.array([[1, -2, 1], 
                               [-2, 4, -2], 
                               [1, -2, 1]])
        result = self.image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        result = cv2.filter2D(result, cv2.CV_64F, kernel)
        result = np.absolute(result)
        result = np.clip(result, 0, 255)
        return result.astype(np.uint8)
    
class Non_linear_filters:
    def __init__(self, img):
        self.image = img
        self.i = ctypes.c_int
        self.ptr = ctypes.POINTER(ctypes.c_uint8)
        self.p = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)), "help.dll"))

    def medianfilter(self, x=3):
        if x % 2 == 0:
            x -= 1
        return cv2.medianBlur(self.image, x)
    
    def maxfilter(self, x=3, y=3):
        row, col = self.image.shape[:2]
        result = self.image.copy()
        a = x // 2
        b = y // 2
        func = self.p.cmax
        func.argtypes = [self.ptr, self.ptr, self.i, self.i, self.i, self.i]
        func.restype = None
        img = np.ascontiguousarray(self.image, dtype=np.uint8)
        pimg = img.ctypes.data_as(self.ptr)
        result = np.ascontiguousarray(result, dtype=np.uint8)
        res = result.ctypes.data_as(self.ptr)
        func(pimg, res, row, col, a, b)
        return result.astype(np.uint8)
    
    def minfilter(self, x=3, y=3):
        row, col = self.image.shape[:2]
        result = self.image.copy()
        a = x // 2
        b = y // 2
        func = self.p.cmin
        func.argtypes = [self.ptr, self.ptr, self.i, self.i, self.i, self.i]
        func.restype = None
        img = np.ascontiguousarray(self.image, dtype=np.uint8)
        pimg = img.ctypes.data_as(self.ptr)
        result = np.ascontiguousarray(result, dtype=np.uint8)
        res = result.ctypes.data_as(self.ptr)
        func(pimg, res, row, col, a, b)
        return result.astype(np.uint8)
    
    def modefilter(self, x=3, y=3):
        row, col = self.image.shape[:2]
        result = self.image.copy()
        a = x // 2
        b = y // 2
        func = self.p.cmode
        func.argtypes = [self.ptr, self.ptr, self.i, self.i, self.i, self.i]
        func.restype = None
        img = np.ascontiguousarray(self.image, dtype=np.uint8)
        pimg = img.ctypes.data_as(self.ptr)
        result = np.ascontiguousarray(result, dtype=np.uint8)
        res = result.ctypes.data_as(self.ptr)
        func(pimg, res, row, col, a, b)
        return result.astype(np.uint8)
