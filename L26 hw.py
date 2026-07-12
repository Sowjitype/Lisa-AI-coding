import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

HF_API_KEY = "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"

def generate_image_from_text(prompt):
    """
    Generates an image from a text prompt using the Stable Diffusion API.
    """
    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Error generating image: {response.status_code}: {response.text}")

def post_process_image(image):
    """
    Applies post-processing effects to the image.

    Effects include:
      - Increasing brightness by 20%
      - Enhancing contrast by 30%
      - Adding a Gaussian blur for a soft-focus effect
    """
    # Increase brightness
    enhancer = ImageEnhance.Brightness()
    bright_image = enhancer.enhance(1.2)  # 1.2 means a 20% increase in brightness

    # Enhance contrast
    enhancer = ImageEnhance.Contrast()
    contrast_image = enhancer.enhance(1.3)  # 1.3 means a 30% increase in contrast

    # Apply a soft-focus effect using Gaussian blur
    soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=2))

    return soft_focus_image

def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image from text and applies post-processing effects.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a description for the image (or 'exit' to quit):\n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating image...")
            image = generate_image_from_text(user_input)

            print("Applying post-processing effects...\n")
            processed_image = post_process_image(image)
            processed_image.show()  # Display the processed image

            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()

                print()

            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()