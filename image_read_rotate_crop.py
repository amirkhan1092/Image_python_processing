# PIL
# pip install pillow

import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('amir.jpg')

# im.show()

# rotate_image = im.rotate(180)

# plt.subplot(121)
# plt.imshow(im)
# plt.subplot(122)
# plt.imshow(rotate_image)

# im.save('rotate_image.jpg')
#
from PIL import Image, ImageFilter
#
# # Read image
# im = Image.open('amir.jpg')
# # Display image
# im.show()
#
from PIL import ImageEnhance
#
enh = ImageEnhance.Contrast(im)
enh.enhance(1.8).show("30% more contrast")
#
#
#
#
# plt.show()

