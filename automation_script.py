import os
import shutil
import zipfile
import pandas as pd

# Define directories
BASE_FOLDER = "transmission_tower_images/organized"
THERMAL_FOLDER = os.path.join(BASE_FOLDER, "thermal")
RGB_FOLDER = os.path.join(BASE_FOLDER, "rgb")
HOTSPOT_FOLDER = os.path.join(BASE_FOLDER, "hotspots")
OUTPUT_ZIP = "organized_images.zip"
METADATA_CSV = "image_metadata.csv"

def create_zip():
    """Compresses organized images into a ZIP file for easy upload."""
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in [THERMAL_FOLDER, RGB_FOLDER, HOTSPOT_FOLDER]:
            if os.path.exists(folder):
                for root, _, files in os.walk(folder):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, BASE_FOLDER))
    print(f"Images compressed into {OUTPUT_ZIP}")

def generate_metadata_csv():
    """Creates a CSV report containing metadata of all images."""
    data = []
    for folder in [THERMAL_FOLDER, RGB_FOLDER]:
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                size_kb = round(os.path.getsize(file_path) / 1024, 2)
                category = "Thermal" if "thermal" in folder else "RGB"
                data.append({"Filename": filename, "Category": category, "Size (KB)": size_kb})

    # Convert data to CSV
    df = pd.DataFrame(data)
    df.to_csv(METADATA_CSV, index=False)
    print(f"Metadata saved in {METADATA_CSV}")

def cleanup_empty_folders():
    """Removes empty folders after processing."""
    for folder in [THERMAL_FOLDER, RGB_FOLDER, HOTSPOT_FOLDER]:
        if os.path.exists(folder) and not os.listdir(folder):
            os.rmdir(folder)
            print(f"🗑️ Removed empty folder: {folder}")

# Run the functions
create_zip()
generate_metadata_csv()
cleanup_empty_folders()

print("Automation complete! Your images are ready for upload.")
