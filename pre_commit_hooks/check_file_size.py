import argparse
import os
from typing import Sequence

MAX_FILE_SIZE_MB = 1.0  # Maximum allowed file size in megabytes

def check_file_size(filenames: Sequence[str]) -> int:
    retv = 0
    for file_path in filenames:
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to megabytes
        if file_size_mb > MAX_FILE_SIZE_MB:
            print(f"File {file_path} exceeds the maximum allowed size of {MAX_FILE_SIZE_MB} MB.")
            retv = 1
    return retv

def main(argv:Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    args = parser.parse_args(argv)
    return check_file_size(args.filenames)

if __name__ == "__main__":
    raise SystemExit(main())
