import cv2
import numpy as np
import os

# Value to darken image
alpha_value = 155.0 # 155.0 is optimal value so far <<< CHANGE THIS IF NECESSARY

def enhance_contrast(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply contrast stretching
    min_intensity = np.min(gray)
    max_intensity = np.max(gray)
    stretched = cv2.convertScaleAbs(gray, alpha = alpha_value / (max_intensity - min_intensity),
                                    beta=-min_intensity * alpha_value / (max_intensity - min_intensity))

    return stretched

def convert_tif_to_png(input_path, output_path):
    # Read the TIF image
    image = cv2.imread(input_path)

    # Enhance contrast
    enhanced_image = enhance_contrast(image)

    # Save the enhanced image as PNG
    cv2.imwrite(output_path, enhanced_image)

# Folders
input_folder = "01_Input"
output_folder = "02_Output"

# Check whether directory already exists
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print("Folder %s created!" % input_folder)
else:
    print("Folder %s already exists" % input_folder)

# Check whether directory already exists
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print("Folder %s created!" % output_folder)
else:
    print("Folder %s already exists" % output_folder)

# Iterate over TIF files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".tif"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename[:-4] + ".png")  # Change file extension to PNG
        print(filename[:-4] + ".png created!")
        convert_tif_to_png(input_path, output_path)
