import cv2
import numpy as np

class Salt_and_pepper_noise:
    def __init__(self, img):
        self.image = img

    def add(self, sprop=0.1, pprop=0.1):
        result = self.image.copy()
        h, w = self.image.shape[:2]
        salt = int(h * w * sprop)
        x = np.random.randint(0, h, salt)
        y = np.random.randint(0, w, salt)
        result[x, y] = [255, 255, 255]
        pepper = int(h * w * pprop)
        x = np.random.randint(0, h, pepper)
        y = np.random.randint(0, w, pepper)
        result[x, y] = [0, 0, 0]
        return result.astype(np.uint8)
    
    def outlierfilter(self, th=30, x=3, y=3, add=False, sprop=0.1, pprop=0.1):
        row, col = self.image.shape[:2]
        a = x // 2
        b = y // 2
        c = x - a - 1
        d = y - b - 1
        result = self.image.copy()
        img = self.image.copy()
        if add:
            img = self.add(sprop, pprop)
        if x == 1 and y == 1:
            return img
        arr = np.ones((x, y), dtype=np.float32)
        arr /= (x * y - 1)
        arr[a, b] = 0
        for ch in range(3):
            localmean = cv2.filter2D(img[a:row-c,b:col-d,ch], -1, arr)
            mask =  np.abs(localmean.astype(np.int16) - img[a:row-c,b:col-d,ch].astype(np.int16)) > th
            result[a:row-c, b:col-d, ch] = np.where(mask, localmean, img[a:row-c,b:col-d,ch]).astype(np.uint8)
        return result.astype(np.uint8)
    
    def averagefilter(self, x=3, y=3, add=False, sprop=0.1, pprop=0.1):
        kernel = np.ones((x, y), dtype=np.float32) / (x * y)
        img = self.image.copy()
        if add:
            img = self.add(sprop, pprop)
        result = cv2.filter2D(img, -1, kernel)
        return result.astype(np.uint8)
    
    def medianfilter(self, x=3, add=False, sprop=0.1, pprop=0.1):
        img = self.image.copy()
        if add:
            img = self.add(sprop, pprop)
        return cv2.medianBlur(img, x)
    
class Gaussian_noise:
    def __init__(self, img):
        self.image = img

    def add(self, std=15, mean=0):
        result = self.image.copy().astype(np.float32)
        noise = np.random.normal(mean, std, self.image.shape).astype(np.float32)
        result += noise
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result
    
    def averagefilter(self, x=3, y=3, add=False, std=15, mean=0):
        kernel = np.ones((x, y), dtype=np.float32) / (x * y)
        img = self.image.copy()
        if add:
            img = self.add(std, mean)
        result = cv2.filter2D(img, -1, kernel)
        return result.astype(np.uint8)
    
    def imageaverging(self, num=10, std=15, mean=0):
        result = np.zeros_like(self.image, dtype=np.float32)
        for i in range(num):
            noise = self.add(std, mean)
            result += noise.astype(np.float32)
        result /= num
        return result.astype(np.uint8)
