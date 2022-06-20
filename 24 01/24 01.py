import numpy as np
from PIL import Image

img = Image.open('1.png')
arr = np.array(img, dtype='uint8')



new_im = Image.fromarray(arr)
new_im.save("2.png")