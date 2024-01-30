import os
import sys

MAX_FILE_SIZE_MB = 1.0  # Maximum allowed file size in megabytes

def check_file_size():
    for root, _, files in os.walk("."):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to megabytes

            if file_size_mb > MAX_FILE_SIZE_MB:
                print(f"File {file_path} exceeds the maximum allowed size of {MAX_FILE_SIZE_MB} MB.")
                sys.exit(1)

if __name__ == "__main__":
    check_file_size()
