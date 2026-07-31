import cv2

def apply_color_filter(image, filter_type):
    #Apply the specified color filter to the image.

    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    if filter_type == "red_tint":
        # Remove blue and green channels for red tint
        filtered_image[:,:,1] = 0 # Green channel to 0
        filtered_image[:,:,0] = 0 # Blue channel to 0
    
    elif filter_type == "blue_tint":
        # Remove red and green channels for blue tint
        filtered_image[:,:,1] = 0 # Green channel to 0
        filtered_image[:,:,2] = 0 # Red channel to 0

    elif filter_type == "green_tint":
        # Remove blue and red channels for green tint
        filtered_image[:,:,0] = 0 # Blue channel to 0
        filtered_image[:,:,2] = 0 # Red channel to 0

    elif filter_type == "increase_red":
        # Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:,:,2], 150)# Increase red channel

    elif filter_type == "decrease_blue":
        # Decrease the intensity of the blue channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:,:,0], 150) # Decrease blue channel

    elif filter_type == "decrease_green":
            # Decrease the intensity of the blue channel
            filtered_image[:, :, 1] = cv2.subtract(filtered_image[:,:,1], 150) # Decrease blue channel

    elif filter_type == "decrease_red":
            # Decrease the intensity of the blue channel
            filtered_image[:, :, 2] = cv2.subtract(filtered_image[:,:,2], 150) # Decrease blue channel

    return filtered_image


# Load the image
image_path = "L11/example.jpg" # Provide your image path
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    filter_type = "original" # Default filter type

print("Press the following keys to apply filters:")
print("r - RED tint")
print("b - BLUE tint")
print("g - GREEN tint")
print("i - Increase RED intensity")
print("d - Decrease BLUE intensity")
print("f - Decrease Green intensity")
print("o - Decrease Red intensity")
print("q - OUIT")

while True:
    # Apply the selected filter
    filtered_image = apply_color_filter(image, filter_type)
    
    # Display the filtered image
    cv2.imshow("Filtered Image", filtered_image)
    
    # Wait for key press
    key = cv2.waitKey(0)    

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
    elif key == ord('f'):
            filter_type = "decrease_green"
    elif key == ord('o'):
        filter_type = "decrease_red"
    elif key == ord('q'):
        print("Exiting...")
        break
    else:
        print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")


cv2.destroyAllWindows()