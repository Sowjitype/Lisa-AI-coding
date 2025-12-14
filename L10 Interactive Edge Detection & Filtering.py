import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
  plt.figure(figsize=(8, 8))

  if len(image.shape)==2:
    plt.imshow(image, cmap="gray")
  else:
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

  plt.title(title)
  plt.axis("off")
  plt.show()

def interactive_edge_detection(image_path):
  image = cv2.imread(image_path)

  if image is None:
    print("Error: Image not found")
    return
  
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_image("original grayscale image", gray_image)

print("Select an option:")
print("Sobel Edge Detetion")
print("Canny Edge Detetion")
print("Laplacian Edge Detetion")
print("Gaussian Smoothing")
print("Median Filtering")
print("Exit")
print()

while True:
  choice = int(input("Enter your choice (1-6)"))
  if choice == 1:

    sobelx = cv2.Sobel(gray_image, cv2.CV64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_image, cv2.CV64F, 0, 1, ksize=3)
    combined_sobel = cv2.bitwise_or(sobelx.astype(np.unit8), sobely.astype(np.uint8))

    display_image("Sobel Edge Detetion", combined_sobel)

  elif choice == 2:
    print("Adjust thresholds for canny(default 100 and 200)")

    lower_threshold = int(input("Enter lower threshold"))
    upper_threshold = int(input("Enter higher threshold"))

    edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)

    display_image("Canny Egde Detetion")

  elif choice == 3:
    laplacian = cv2.Laplacian(gray_image,cv2.CV_64F)
    display_image("Laplacian Edge Detetion", np.abs(laplacian).astype(np.uint8))

  elif choice == 4:
    print("Adjust Kernel size for gaussion Blur( must be odd number, default 5)")

    kernal_size = int(input("Enter Kenral size(odd number)"))
    blurred = cv2.GaussianBlur(image , (kernal_size, kernal_size), 0)

    display_image("Gaussian Smoothing")