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
        a = x // 2
        b = y // 2
        result = self.image.copy()
        img = self.image.copy()
        if add:
            img = self.add(sprop, pprop)
        arr = np.ones((x, y), dtype=np.float32)
        arr /= (x * y - 1)
        arr[a, b] = 0
        for ch in range(3):
            # for i in range(a, img.shape[0]-a):
            #     for j in range(b, img.shape[1]-b):
            #         local_region = img[i-a:i+a+1, j-b:j+b+1, ch]
            #         local_mean = np.sum(arr * local_region)
            #         if abs(self.image[i, j, ch] - local_mean) > th:
            #             result[i, j, ch] = np.uint8(local_mean)
            localmean = cv2.filter2D(img[a:-a,b:-b,ch], -1, arr)
            mask =  np.abs(localmean.astype(np.int16) - img[a:-a,b:-b,ch].astype(np.int16)) > th
            result[a:-a, b:-b, ch] = np.where(mask, localmean, img[a:-a,b:-b,ch]).astype(np.uint8)
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

    def averagefilter(self, x=3, y=3, add=False, std=15, mean=0):

        kernel = np.ones((x, y), dtype=np.float32) / (x * y)
        img = self.image.copy()
        if add:
            img = self.add(std, mean)
        result = cv2.filter2D(img, -1, kernel)
        return result.astype(np.uint8)
    
    def add(self, std=15, mean=0):
        result = self.image.copy().astype(np.float32)
        noise = np.random.normal(mean, std, self.image.shape).astype(np.float32)
        result += noise
        result = np.clip(result, 0, 255).astype(np.uint8)
        return result
    
    def imageaverging(self, num=10, std=15, mean=0):
        result = np.zeros_like(self.image, dtype=np.float32)
        for i in range(num):
            noise = self.add(std, mean)
            result += noise.astype(np.float32)
        result /= num
        return result.astype(np.uint8)