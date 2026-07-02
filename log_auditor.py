import os
import shutil
import time

# Configuration
SOURCE_FOLDER = "." 
ARCHIVE_FOLDER = "archive_logs"

# Ensure the archive directory exists
if not os.path.exists(ARCHIVE_FOLDER):
    os.makedirs(ARCHIVE_FOLDER)

print("--- Starting Log Audit Process ---")

# Scan the directory
for filename in os.listdir(SOURCE_FOLDER):
    if filename.endswith(".log"):
        file_path = os.path.join(SOURCE_FOLDER, filename)
        file_age = os.path.getmtime(file_path)
        
        # Archive files older than 24 hours (1 day)
        if (time.time() - file_age) > (1 * 86400):
            shutil.move(file_path, os.path.join(ARCHIVE_FOLDER, filename))
            print(f"Successfully archived: {filename}")
        else:
            print(f"Skipped: {filename} (File is recent)")

print("--- Log Audit Completed Successfully ---")