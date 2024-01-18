import os
from PIL import Image
from image.compare_images import compare_images, file_is_image
from archive.compare_size import file_is_archive, compare_archive_sizes
from name_comparator import create_unique_set, print_unique, create_common_set

def compare_directories(dir1_path, dir2_path):
    print(f"\nComparing directories:  \"{dir1_path}\"  AND  \"{dir2_path}\"")

    # Create sets containing the names of the files in each directory
    files_dir1 = set(os.listdir(dir1_path))
    files_dir2 = set(os.listdir(dir2_path))

    # Create sets containing the names of the unique files (the names of files present in one directory but not in the other)
    unique_files_dir1 = create_unique_set(files_dir1, files_dir2)
    unique_files_dir2 = create_unique_set(files_dir2, files_dir1)
  
    # Print unique files in directory_1 against directory_2 and vise versa
    print_unique(unique_files_dir1, unique_files_dir2)

    # Create sets containing the names of the common files between both directories
    common_files = create_common_set(files_dir1,files_dir2)

    compare_common(dir1_path,dir2_path,common_files)


def compare_common(dir1_path,dir2_path,common_files):
    # Create counters and lists for later summary report
    identical_files, not_identical_files, unsupported_files = 0, 0, 0
    identical_file_names, not_identical_file_names, unsupported_files_names = [],[], []

    # Compare common files
    for file in common_files:
        # Create specific paths for the common file in both directories and send them for comparison
        file_path1 = os.path.join(dir1_path, file)
        file_path2 = os.path.join(dir2_path, file)
        is_identical = compare_common_files(file, file_path1, file_path2) #Check file types and perform specific comparisons
        if is_identical == 1:
            identical_files += 1
            identical_file_names.append(file)
        elif is_identical == -1:
            not_identical_files += 1
            not_identical_file_names.append(file)
        else :
            unsupported_files += 1
            unsupported_files_names.append(file)
        

    print("\nSUMMARY:")
    print(f"Number of common files: {len(common_files)}")
    print(f"\nNumber of identical files: {identical_files}")
    if identical_files > 0:
        print("\nIdentical file names:")
        for name in identical_file_names:
            print(name)

    print(f"\nNumber of not identical files: {not_identical_files}")
    if not_identical_files > 0:
        print("\nNot identical file names:")
        for name in not_identical_file_names:
            print(name)
        
    print(f"\nNumber of unsupported files: {unsupported_files}")
    if unsupported_files > 0:
        print("\nUnsupported file names:")
        for name in unsupported_files_names:
            print(name)


def compare_common_files(file, file_path1, file_path2):
    print(f"\nComparing files with the name: {file}")
    
    # Check file types and perform specific comparisons
    if file_is_image(file_path1) and file_is_image(file_path2):
        return compare_images(file, file_path1, file_path2)
    elif file_is_archive(file_path1) and file_is_archive(file_path2):
        return compare_archive_sizes(file, file_path1, file_path2)
    else:
        print(f"Unsupported file type: {file}")
        return 0


