import os

# get the summary of distributions of extensions
extensions = []
for root, dirs, files in os.walk(r"C:\Users\user\Desktop\finetune"):
    print(root)
    print(dirs)
    try:
        for file in files:
            extensions.append(os.path.splitext(file)[1])
    except:
        pass
    print("-"*40)
extensions = set(extensions)
print(extensions)

# count the number of picture files inside a directory.
print("Start counting pictures")
picture_count = 0

for root, dirs, files in os.walk(r"C:\Users\user\Desktop\finetune\valid"):
    try:
        print(root)
        print(dirs)
        for file in files:
            if os.path.splitext(file)[1] in extensions:
                picture_count += 1
            else:
                pass
    except:
        pass
    print("-" * 40)
print(f"number of pictures: {picture_count}")


from PIL import Image
import os

import tensorflow
from tensorflow import keras


# Check and remove corrupted images
def check_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg")):
                try:
                    img_path = os.path.join(root, file)
                    with Image.open(img_path)as img:
                        img.verify() # Verify if image is currenpted
                except (IOError, SyntaxError) as e:
                    print(f"Corrupted image: {file}")
                    os.remove(img_path)  # Optionally remove the corrupted image

check_images(r"C:\Users\user\Desktop\finetune")
