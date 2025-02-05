#trying to import content from google drive

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_path = "/content/drive/MyDrive/Photo/cars.jpg"  
img = mpimg.imread(image_path)


plt.imshow(img)
plt.axis('on')  
plt.show()