import cv2

# Load the image
image = cv2.imread("L07\person.jpg")

# Rezive the window to a specific size without resizing the image
cv2.namedWindow('Loading image', cv2.WINDOW_NORMAL) # Create a resizable window
cv2.resizeWindow('Loading image', 800, 500) # Set the window size to 800x500(width x height)

# Display the image in resized window
cv2.imshow('Loading image', image)
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() # Close the window

# Print image properties
import cv2

# Load the image
image = cv2.imread("L07\person.jpg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Resize the grayscale image to 224x224
resized_image = cv2.resize(gray_image,(224, 224))

# Display the image in resized window
cv2.imshow('Processed image',resized_image)

# Wait for a key press
key = cv2.waitKey(0) # Wait indefintely for a key press

# Check if the "S" key was pressed (ASCII for 'S' is 83)
if key == ord('s'):
  # Save the processed image when "S" pressed
  cv2.imwrite('L07\grayscale_rezsize_person.jpg',resized_image)
  print('image saved as grayscale_rezsize_person.jpg')
else:
  print("Image not saved")

# Close the window
cv2.destroyAllWindows() 

# Print image properties
print(f"Image Dimensions:{image.shape}") # Height,Width,Channels