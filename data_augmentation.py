import os
import cv2
import random

# Modify this path to the folder you want to augment
CURRENT_PATH = os.getcwd()

def random_rotate(image, angle_range=(-30, 30)):
    angle = random.uniform(angle_range[0], angle_range[1])
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_image


def random_flip(image, horizontal=True, vertical=False):
    if horizontal and random.random() > 0.5:
        image = cv2.flip(image, 1)
    if vertical and random.random() > 0.5:
        image = cv2.flip(image, 0)
    return image


def random_brightness_contrast(image, brightness_range=(0.2, 1.7), contrast_range=(0.5, 1.5)):
    alpha = random.uniform(contrast_range[0], contrast_range[1])
    beta = random.uniform(brightness_range[0], brightness_range[1])
    augmented_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return augmented_image


def random_hue(image, hue_range=(-10, 10)):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = random.uniform(hue_range[0], hue_range[1])
    # Hue values wrap around
    hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue) % 180
    augmented_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return augmented_image

os.mkdir('augmented')
counter = 0
for file_name in os.listdir(CURRENT_PATH):
    print(file_name[-1:-4:-1])
    if file_name[-1:-4:-1] != "gpj":
        continue
    # Apply random augmentations
    image = cv2.imread(file_name)
    augmented_image = random_rotate(image)
    augmented_image = random_flip(
        augmented_image, horizontal=True, vertical=False)
    augmented_image = random_brightness_contrast(augmented_image)
    augmented_image = random_hue(augmented_image, hue_range=(-5, 5))
    cv2.imwrite(f'augmented/{file_name[:-4]}_augmented.jpg', augmented_image)
    counter += 1