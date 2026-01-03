import cv2

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""

    filtered_image = image.copy()

    if filter_type == "original":

        pass

    elif filter_type == "red_tint":
        
        filtered_image[:, :, 1] = 0  
        filtered_image[:, :, 0] = 0  

    elif filter_type == "blue_tint":

        filtered_image[:, :, 1] = 0  
        filtered_image[:, :, 2] = 0  

    elif filter_type == "green_tint":
  
        filtered_image[:, :, 0] = 0  
        filtered_image[:, :, 2] = 0  

    elif filter_type == "increase_red":

        red_channel = filtered_image[:, :, 2]
        filtered_image[:, :, 2] = cv2.add(red_channel, 50)

    elif filter_type == "decrease_blue":

        blue_channel = filtered_image[:, :, 0]
        filtered_image[:, :, 0] = cv2.subtract(blue_channel, 10)

    elif filter_type == "sobel":
 
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  
        

        sobelx_abs = cv2.convertScaleAbs(sobelx)
        sobely_abs = cv2.convertScaleAbs(sobely)
        

        combined_sobel = cv2.bitwise_or(sobelx_abs, sobely_abs)
 
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)

    elif filter_type == "canny":

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
        edges = cv2.Canny(gray_image, 100, 200)

        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image


# Load the image
image_path = "Python/L14/example.jpg" 
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found! Check the file path.")
    exit()  # Exit if image fails to load

# Default filter type
filter_type = "original"

print("Press the following keys to apply filters:")
print("r - RED tint")
print("b - BLUE tint")
print("g - GREEN tint")
print("i - Increase RED intensity")
print("d - Decrease BLUE intensity")
print("c - Canny edge detection")
print("s - Sobel edge detection")
print("q - QUIT")

while True:
    # Apply the selected filter
    filtered_image = apply_color_filter(image, filter_type)
    
    # Display the filtered image
    cv2.imshow("Filtered Image", filtered_image)
    
    # Wait for key press (1ms for smooth loop; 0 = wait indefinitely)
    key = cv2.waitKey(1) & 0xFF  # &0xFF to handle numpad keys

    # Map key presses to filters
    if key == ord('r'):
        filter_type = "red_tint"
    elif key == ord('b'):
        filter_type = "blue_tint"
    elif key == ord('g'):
        filter_type = "green_tint"
    elif key == ord('i'):
        filter_type = "increase_red"
    elif key == ord('d'):
        filter_type = "decrease_blue"
    elif key == ord('s'):
        filter_type = "sobel"
    elif key == ord('c'):
        filter_type = "canny"
    elif key == ord('q'):
        print("Exiting...")
        break
    elif key != -1:  # Only print invalid key if a key was pressed
        print("Invalid key! Use: r/b/g/i/d/c/s/q")

# Clean up windows
cv2.destroyAllWindows()