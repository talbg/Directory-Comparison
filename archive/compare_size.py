import os
from archive.file_extensions import archive_extensions
def file_is_archive(file_path):
    # Check if a file is one of the common archive formats
    return any(file_path.lower().endswith(ext) for ext in archive_extensions)

def compare_archive_sizes(file, archive_path1, archive_path2):
    try:
        # Compare sizes of archive files
        size1 = os.path.getsize(archive_path1)
        size2 = os.path.getsize(archive_path2)

        if size1 == size2:
            print(f"Archives {file} have the same size")
            return True
        else:
            print(f"Archives {file} have different sizes")
            return False
    except (OSError, FileNotFoundError) as e:
        print(f"Error comparing archive sizes: {e}")
        return False