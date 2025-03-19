import os
import random
import shutil


def distribute_images(source_dir, destination_dir, classes, train_ratio, valid_ratio, test_ratio):
    # Create destination folders (Training, Validation, Test) for each class
    for class_name in classes:
        os.makedirs(os.path.join(destination_dir, 'train', class_name), exist_ok=True)
        os.makedirs(os.path.join(destination_dir, 'valid', class_name), exist_ok=True)
        os.makedirs(os.path.join(destination_dir, 'test', class_name), exist_ok=True)

    # Loop through each class and distribute the images
    for class_name in classes:
        class_path = os.path.join(source_dir, class_name)

        # List all image files in the class folder
        images = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]

        # Shuffle the images randomly
        random.shuffle(images)

        # Calculate the number of images for each set based on ratios
        total_images = len(images)
        train_count = int(total_images * train_ratio)
        valid_count = int(total_images * valid_ratio)
        test_count = total_images - train_count - valid_count

        # Distribute images to Training, Validation, and Test sets
        train_images = images[:train_count]
        valid_images = images[train_count:train_count + valid_count]
        test_images = images[train_count + valid_count:]

        # Copy images to the respective folders
        for img in train_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(destination_dir, 'train', class_name, img)
            shutil.copy(src_path, dest_path)

        for img in valid_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(destination_dir, 'valid', class_name, img)
            shutil.copy(src_path, dest_path)

        for img in test_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(destination_dir, 'test', class_name, img)
            shutil.copy(src_path, dest_path)


# parameters
source_directory = ""
destination_directory = ""
class_names = ['', '']
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

distribute_images(source_directory, destination_directory, class_names, train_ratio, valid_ratio, test_ratio)

