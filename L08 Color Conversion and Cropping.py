# Color conversions and cropping
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("L08\example2.jpg")

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
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()