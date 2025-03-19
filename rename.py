import os
import random
import string


def generate_random_name(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def random_rename_image_files(folder_path):
    os.chdir(folder_path)

    # Get a list of all files in the folder
    files = os.listdir()

    # Filter only image files (you can add more extensions if needed)
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    for filename in image_files:
        # Generate a random name
        new_name = generate_random_name() + os.path.splitext(filename)[1]

        # Rename the image file
        os.rename(filename, new_name)


# Replace "/path/to/your/folder" with the actual path to your folder
folder_path = ""
random_rename_image_files(folder_path)

