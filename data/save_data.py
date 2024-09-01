import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime
from data.data_manager import DataManager

def save_image(image, path):
    if image is not None:
        if isinstance(image, np.ndarray):
            # Convert dtype to uint8 if necessary
            if image.dtype == np.int64:
                # Normalize and convert int64 to uint8
                image = np.clip(image, 0, 255).astype(np.uint8)
            elif image.dtype == np.float32 or image.dtype == np.float64:
                # Normalize float values to the range [0, 255]
                image = (255 * np.clip(image, 0, 1)).astype(np.uint8)
            elif image.dtype != np.uint8:
                raise TypeError(f"Unsupported dtype: {image.dtype}")

            # Handle grayscale and RGB images
            if image.ndim == 2:  # Grayscale image
                image = Image.fromarray(image, mode='L')
            elif image.ndim == 3 and image.shape[2] in [3, 4]:  # RGB or RGBA image
                image = Image.fromarray(image, mode='RGB' if image.shape[2] == 3 else 'RGBA')
            else:
                raise ValueError(f"Unsupported image shape: {image.shape}")

        elif isinstance(image, Image.Image):
            pass  # Image is already a PIL Image
        else:
            raise TypeError(f"Unsupported image type: {type(image)}")

        # Save the image
        image.save(path)

def save_measured_data(base_path):
    manager = DataManager()
    data = manager.data_for_analisys
    # Get the current date and time for the file name
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    folder_path = os.path.join(base_path, current_time)

    # Create directories to save images
    os.makedirs(os.path.join(folder_path, 'labeled_overlays'), exist_ok=True)
    os.makedirs(os.path.join(folder_path, 'labeled_overlays_white'), exist_ok=True)
    excel_file_path = os.path.join(folder_path, f"measured_data_{current_time}.xlsx")

    # Create a dictionary to hold DataFrames for each sheet
    sheet_data = {}

    # Organize data by name
    for item in data:
        name = item.data_name

        # Save images using the helper function
        save_image(item.labeled_overlays, os.path.join(folder_path, f'labeled_overlays/{name}_overlays.bmp'))
        save_image(item.labeled_overlays_white, os.path.join(folder_path, f'labeled_overlays_white/{name}_overlays_white.bmp'))
        
        # Prepare the row data using zip
        rows = []
        for label, area, distance, neighbor_name in zip(item.labels_names, item.areas, item.nearest_neighbor_distances, item.nearest_neighbor_name):
            row = {
                'label': label,
                'area': area,
                'nearest_neighbor_distance': distance,
                'nearest_neighbor_label': neighbor_name
            }
            rows.append(row)

        # Convert rows to DataFrame
        df = pd.DataFrame(rows)

        # Add DataFrame to the dictionary with the name as the key
        sheet_data[name] = df

    # Write all DataFrames to an Excel file with different sheets
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    # # Save CSV
    # csv_file_path = os.path.join(folder_path, 'measured_data.csv')
    # df = pd.DataFrame(csv_data)
    # df.to_csv(csv_file_path, index=False)