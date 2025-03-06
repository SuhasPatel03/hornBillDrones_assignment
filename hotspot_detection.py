import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

THERMAL_FOLDER = "transmission_tower_images/organized/thermal"
OUTPUT_FOLDER = "transmission_tower_images/organized/hotspots"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def detect_hotspots(image_path):
    """Detects bright spots (hotspots) in a thermal image."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  

    if image is None:
        print(f" Error reading {image_path}")
        return

    _, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(image_color, contours, -1, (0, 0, 255), 2) 

    output_path = os.path.join(OUTPUT_FOLDER, os.path.basename(image_path))
    cv2.imwrite(output_path, image_color)
    print(f"Hotspots detected in {os.path.basename(image_path)} → Saved to {output_path}")

def process_thermal_images():
    """Processes all thermal images for hotspot detection."""
    images = [f for f in os.listdir(THERMAL_FOLDER) if f.endswith(('.jpg', '.png'))]

    if not images:
        print(" No thermal images found!")
        return

    for image in images:
        detect_hotspots(os.path.join(THERMAL_FOLDER, image))

process_thermal_images()
print("Hotspot detection complete!")
