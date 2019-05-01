# PIL
# pip install pillow
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('amir.jpg')

rotate_image = im.rotate(180)

plt.subplot(121)
plt.imshow(im)
plt.subplot(122)
plt.imshow(rotate_image)




plt.show()

