import cv2
import numpy as np
import os

# Adjustable values to darken or lighten image for enhance_contrast
alpha_value = 155.0  # 155.0 is optimal value so far <<< CHANGE THIS IF NECESSARY
value_2 = 0.0  # 0.0 is optimal value so far <<< CHANGE THIS IF NECESSARY

# Define enhance_contrast
def enhance_contrast(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply contrast stretching
    min_intensity = np.min(gray)
    max_intensity = np.max(gray)
    stretched = cv2.convertScaleAbs(
        gray,
        alpha=alpha_value / (max_intensity - min_intensity),
        beta=-min_intensity * value_2 / (max_intensity - min_intensity),
    )

    return stretched

# Define process_to_tif (or whatever image format you want to convert to)
def process_to_tif(input_path, output_path):
    # Read the TIF image
    image = cv2.imread(input_path)

    # Enhance contrast
    enhanced_image = enhance_contrast(image)

    # Save the enhanced image as TIF
    cv2.imwrite(output_path, enhanced_image)

# Folders
input_folder = "01_Input"
output_folder = "02_Output"

print("=============== START ===============")

# Check whether directories already exist
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print("Folder %s created!" % input_folder)
else:
    print("Folder %s already exists" % input_folder)

if not os.path.exists(output_folder):
    os.mkdir(output_folder)
    print("Folder %s created!" % output_folder)
else:
    print("Folder %s already exists" % output_folder)

# Iterate over subfolders in the input folder
for subfolder_name in os.listdir(input_folder):
    subfolder_path = os.path.join(input_folder, subfolder_name)
    if os.path.isdir(subfolder_path):
        output_subfolder_path = os.path.join(output_folder, subfolder_name)
        os.makedirs(output_subfolder_path, exist_ok=True)
        print(f"Subfolder '{subfolder_name}' created!")

        # Iterate over TIF files in the subfolder
        for filename in os.listdir(subfolder_path):
            if filename.endswith(".tif"):
                input_path = os.path.join(subfolder_path, filename)
                output_path = os.path.join(output_subfolder_path, filename)
                print(f"Processing '{filename}'")
                process_to_tif(input_path, output_path)

print("=============== END ===============")
