import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Create an image
img = Image.new("RGB", (400, 300), "white")
draw = ImageDraw.Draw(img)


draw.line([200, 50, 200, 250], "blue", 5)  


draw.line([50, 150, 350, 150], "red", 5) 

# Display the image using Matplotlib
plt.imshow(img)
plt.axis("off")  # Hide axes
plt.show() 