

# Directory Comparison

## Overview
The Directory Comparison script is designed to compare two directories, identifying differences in files, considering variations like images and archives.

This script operates under the assumption that files come with extensions, as specified in the task description. 
In scenarios where file extensions are not present, a more advanced file type detection mechanism, like 'python-magic' library, could be employed. However, for the purposes of this task and to keep the implementation concise.

## Approach

**File Comparison**
1. Identifying Unique Files
The script begins by obtaining the list of files in each directory and comparing them to find files that exist in one directory but not the other. This comparison is based on file names.

2. Common Files
For files that exist in both directories, the script performs specific checks based on their file types.


**Image Comparison**

For files identified as images, the script uses the Pillow library to compare them. Pillow allows pixel-level comparison, checking if the images are identical or not.


**Archive Comparison**

For files identified as archives (zip, tar, etc.), the script compares their sizes. This provides a quick check to determine if the archives have the same size, implying potential identical content.


**Unsupported File Types**

Files with unsupported types are flagged, and the script prints a message indicating the unsupported file types. Currently, the script supports image and archive file types.


**Extensibility**

The script is designed in a modular way, allowing for easy extensibility for future file type comparisons. New file type comparison functions can be added based on specific requirements. This modular approach enhances the script's flexibility and maintainability.


**Performance Optimizations**

Considerations have been made for performance optimizations, especially for large directories. The script minimizes unnecessary file operations and utilizes efficient comparison methods to enhance overall performance.

This approach ensures that the script is robust, extendable, and capable of handling various file types efficiently.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/talbg/Directory-Comparison.git
   
2. Navigate to the project directory:
      ```bash
      cd Directory-Comparison
                     
3. Run the script:
   ```bash
   python main.py

4. The program ask you to fill in the first path and afterwords the second.
   you can use my test files from above just change the path according to your system or give a path of your own files. 

* if using my test files:

      dir1_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\my task\\dir1"
      dir2_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\my task\\dir2"
       
Update the paths according to your system. For example:
         
         dir1_path = "path/to/your/dir1"
         dir2_path = "path/to/your/dir2"

## Dependencies

1. The script relies on the Python library - 'Pillow' For image comparison.

    Install the dependencies using:

     ```bash
    pip install Pillow

2. Ensure your Python version is 3.0 and above.
