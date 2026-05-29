import cv2
import numpy as np

class histogram:
    def __init__(self, img):
        self.image = img

    def histstretch(self, gray=True):
        result = self.image.copy().astype(np.float32)
        if gray:
            result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
            min_val = np.min(result)
            max_val = np.max(result)
            if max_val > min_val:
                result = (result - min_val) * 255 / (max_val - min_val)
        else:
            for i in range(3):
                min_val = np.min(result[:,:,i])
                max_val = np.max(result[:,:,i])
                if max_val > min_val:
                    result[:,:,i] = (result[:,:,i] - min_val) * 255 / (max_val - min_val)
        result = np.clip(result, 0, 255)
        return result.astype(np.uint8)
    
    def histequalization(self, gray=True):
        result = self.image.copy()
        if gray:
            result = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
            result = cv2.equalizeHist(result)
        else:
            hsv = cv2.cvtColor(result, cv2.COLOR_RGB2HSV)
            h, s, v = cv2.split(hsv)
            v = cv2.equalizeHist(v)
            hsv = cv2.merge([h, s, v])
            result = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
        return result.astype(np.uint8)