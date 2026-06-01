class color_operation:
    def __init__(self, img):
        self.image = img

    def change(self, num = 50, i=0):
        result = self.image.copy()
        result[:,:,i] = num
        return result
    
    def swap(self, i=0, j = 1):
        result = self.image.copy()
        result[:,:,i], result[:,:,j] = self.image[:,:,j], self.image[:,:,i]
        return result
    
    def eliminate(self, i=0):
        result = self.image.copy()
        result[:,:,i] = 0
        return result
