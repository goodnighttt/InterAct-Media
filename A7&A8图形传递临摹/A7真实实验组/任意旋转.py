import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

original_image = None

def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), borderValue=(0, 0, 0))
    return rotated_image

def save_image(image, original_path):
    directory = os.path.dirname(original_path)
    filename = os.path.basename(original_path)
    new_filename = os.path.splitext(filename)[0] + "_." + "png"
    save_path = os.path.join(directory, new_filename)
    cv2.imwrite(save_path, image)
    print("Image saved successfully at:", save_path)

def update_rotation(angle):
    global original_image
    if original_image is not None:
        angle = float(angle)
        rotated_image = rotate_image(original_image.copy(), angle)
        cv2.imshow("Rotated Image", rotated_image)

def main():
    root = tk.Tk()
    root.title("Image Rotator")
    root.geometry("400x200")  # 设置窗口宽度为400，高度为200

    # Specify image file path
    file_path = "0.png"

    global original_image
    original_image = cv2.imread(file_path)

    # Create slider control
    angle_var = tk.DoubleVar()
    # angle_slider = tk.Scale(root, from_=-180, to=180, resolution=1, orient=tk.HORIZONTAL, variable=angle_var, command=update_rotation)
    # angle_slider = tk.Scale(root, from_=-180, to=180, resolution=0.1, orient=tk.HORIZONTAL, variable=angle_var, command=update_rotation)
    angle_slider = tk.Scale(root, from_=-180, to=180, resolution=0.1, orient=tk.HORIZONTAL, variable=angle_var, command=update_rotation, length=500)
    angle_slider.set(0)
    angle_slider.pack()

    # Show the original image
    cv2.imshow("Original Image", original_image)

    # Run the GUI main loop
    root.mainloop()

    # Save the rotated image
    if original_image is not None:
        rotated_image = rotate_image(original_image, angle_var.get())
        save_image(rotated_image,file_path)

    # Release windows and memory
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

