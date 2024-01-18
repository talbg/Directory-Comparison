
def create_unique_set(files_dir1,files_dir2):
    # Create sets containing the names of the unique files (the names of files present in one directory but not in the other)
    unique_files = files_dir1 - files_dir2
    return unique_files


def print_unique(unique_files_dir1, unique_files_dir2):
    # Print unique files in directory_1 against directory_2 and vise versa
    print(f"\nUnique files in directory_1 but not in directory_2:")
    if not unique_files_dir1:
        print("There are no unique files in directory_1")
    else:
        print("\n".join(f"{idx}. {file}" for idx, file in enumerate(unique_files_dir1, start=1)))

    print(f"\nUnique files in directory_2 but not in directory_1")
    if not unique_files_dir2:
        print("There are no unique files in directory_2")
    else:
        print("\n".join(f"{idx}. {file}" for idx, file in enumerate(unique_files_dir2, start=1)))


def create_common_set(files_dir1,files_dir2):
    common = files_dir1 & files_dir2
    return common