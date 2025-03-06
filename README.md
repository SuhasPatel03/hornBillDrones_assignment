# 🚀 Transmission Tower Image Processing

This project processes **thermal and RGB images** of transmission towers.  
It extracts metadata, classifies images, detects hotspots, and automates organization.  

---

## 📌 Features
✅ **Organizes images** into `thermal/` and `rgb/` based on metadata  
✅ **Extracts metadata** (timestamp, GPS) and renames files  
✅ **Detects hotspots** in thermal images using OpenCV  
✅ **Creates a ZIP** of organized images for easy upload  
✅ **Generates a CSV report** with image metadata  

---

## 📂 Folder Structure
project-folder/ 
                │── organize_images.py # Classifies and renames images 
                │── hotspot_detection.py # Detects hotspots in thermal images 
                │── automation_script.py # Automates ZIP and CSV generation 
                │── transmission_tower_images/ 
                │ ├── raw_images/ # Original images (before processing) 
                │ ├── organized/ │ │ ├── thermal/ # Processed thermal images 
                │ │ ├── rgb/ # Processed RGB images 
                │ │ ├── hotspots/ # Hotspot-marked images 
                │── organized_images.zip # Final compressed file for upload 
                │── image_metadata.csv # Metadata report 
                │── README.md # Project documentation
