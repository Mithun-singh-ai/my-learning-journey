import os
import shutil
import time

# जिस फोल्डर में ये स्क्रिप्ट है, उसी को स्कैन करेगी
folder_to_clean = "." 
archive_folder = "archive_logs"

if not os.path.exists(archive_folder):
    os.makedirs(archive_folder)

print("--- Cloud-Auditor Running ---")

for filename in os.listdir(folder_to_clean):
    if filename.endswith(".log"):
        file_path = os.path.join(folder_to_clean, filename)
        file_age = os.path.getmtime(file_path)
        
        # अगर फाइल 1 दिन से पुरानी है
        if (time.time() - file_age) > (1 * 86400):
            shutil.move(file_path, os.path.join(archive_folder, filename))
            print(f"Archived: {filename}")
        else:
            print(f"Skipped: {filename} (Recent file)")

print("--- Audit Complete ---")