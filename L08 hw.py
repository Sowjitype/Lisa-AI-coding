# Color conversions and cropping
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("L08\Tomato-red.png")

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Cropping the image
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
cropped_image = image[100:500, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()

# Rotating and Adjust Image Brightness
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("L08\Tomato-red.png")
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# Rotate the image by 45 degree around its center
(h, w) = image.shape[:2]
center = (w//3, h//2)
M = cv2.getRotationMatrix2D(center,10,1.0) # rotate by 45 degrees
rotated = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to adoid negative or overflow
brightness_matrix = np.ones(image.shape,dtype="uint8")*50
brighter= cv2.add(image,brightness_matrix)

brightness_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brightness_rgb)
plt.title("Brighter Image")
plt.show()