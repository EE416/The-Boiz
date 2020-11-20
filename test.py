import cv2
from PIL import Image
from resizeimage import resizeimage
import os

# Arbritrary large starting numbers
dimW = 10000
dimH = 10000

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".png")]:
        # read image
        img = cv2.imread(os.path.join(dirpath, filename))
        if img is not None:
            imgDim = img.shape

        # store dimensions if smaller than current smallest
        if imgDim[0] < dimH:
            dimH = imgDim[0]
        if imgDim[1] < dimW:
            dimW = imgDim[1]
print(f"minH: {dimH}")
print(f"minW: {dimW}")


        


  

#with open(r'.\Covid\1.png', 'r+b') as f:
    #with Image.open(f) as image:
        #cover = resizeimage.resize_cover(image, [200, 100])
        #cover.save('testImage.png', image.format)


