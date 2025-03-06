import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Define input and output directories
INPUT_FOLDER = "transmission_tower_images"  # Folder where images are stored
ORG_FOLDER = os.path.join(INPUT_FOLDER, "organized")
THERMAL_FOLDER = os.path.join(ORG_FOLDER, "thermal")
RGB_FOLDER = os.path.join(ORG_FOLDER, "rgb")

# Create necessary folders
os.makedirs(THERMAL_FOLDER, exist_ok=True)
os.makedirs(RGB_FOLDER, exist_ok=True)

def extract_metadata(image_path):
    """Extracts metadata from an image file."""
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        metadata = {}

        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value

            # Extract GPS data
            gps_info = {}
            if "GPSInfo" in metadata:
                for key in metadata["GPSInfo"].keys():
                    gps_tag = GPSTAGS.get(key, key)
                    gps_info[gps_tag] = metadata["GPSInfo"][key]
                metadata["GPSInfo"] = gps_info

        return metadata
    except Exception as e:
        return {"Error": str(e)}

def format_gps(gps_data):
    """Converts GPS coordinates to a string format."""
    if gps_data:
        lat = gps_data.get('GPSLatitude', [0, 0, 0])
        lon = gps_data.get('GPSLongitude', [0, 0, 0])
        return f"{lat[0]}_{lat[1]}_{lat[2]}N_{lon[0]}_{lon[1]}_{lon[2]}E"
    return "NoGPS"

def rename_and_organize_images():
    """Renames and moves images based on metadata."""
    files_detected = os.listdir(INPUT_FOLDER)
    print("Files detected:", files_detected)

    for filename in files_detected:
        file_path = os.path.join(INPUT_FOLDER, filename)

        if not os.path.isfile(file_path):
            continue  # Skip folders

        metadata = extract_metadata(file_path)
        print(f"Metadata for {filename}: {metadata}")  # Debugging line

        timestamp = metadata.get("DateTimeOriginal", "Unknown").replace(":", "").replace(" ", "_")
        gps_str = format_gps(metadata.get("GPSInfo", {}))

        new_filename = f"{timestamp}_{gps_str}.jpg"
        dest_folder = THERMAL_FOLDER if "_T" in filename else RGB_FOLDER
        new_path = os.path.join(dest_folder, new_filename)

        shutil.move(file_path, new_path)
        print(f"Moved: {filename} → {new_path}")

# Run the function
rename_and_organize_images()
print("🎉 Image organization complete!")
