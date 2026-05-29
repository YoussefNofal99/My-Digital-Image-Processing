import cv2
import numpy as np

class thresholding:
    def __init__(self, img):
        self.image = img

    def globalthresholding(self, thr=127):
        result = self.image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        result = np.where(result >= thr, 255, 0)
        return result.astype(np.uint8)

    def adathresholding(self, bsize=3, c=5):
        result = self.image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        if bsize % 2 == 0:
            bsize -= 1
        result = cv2.adaptiveThreshold(result, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bsize, c)
        return result.astype(np.uint8)

    def autothresholding(self, delta=0.1, maxi=100):
        result = self.image.copy()
        result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
        result = result.astype(np.float32)
        c = np.mean(result)
        for i in range(maxi):
            m1 = result[result >= c]
            m2 = result[result < c]
            if len(m1) == 0 or len(m2) == 0:
                break
            f = 0.5 * (np.mean(m1) + np.mean(m2))
            if abs(c - f) <= delta:
                c = f
                break
            c = f
        result = np.where(result >= c, 255, 0)
        return result.astype(np.uint8)