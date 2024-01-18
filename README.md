

# Directory Comparison Script

## Overview
The Directory Comparison script is designed to compare two directories, identifying differences in files, considering variations like images and archives.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/talbg/Directory-Comparison.git
   
2. Navigate to the project directory:
      ```bash
      cd Directory-Comparison
    
3. Run the script:

    ```bash
    python directory_comparison.py      

## Dependencies

1. The script relies on the Python library - 'Pillow' For image comparison.

    Install the dependencies using:

     ```bash
    pip install Pillow

2. Ensure your Python version is 3.0 and above.

## Bonus Points
Extensibility
The script is implemented in a modular way, making it easy to extend for future file type comparisons. New file type comparison functions can be added based on specific requirements.

## Performance Optimizations
Considerations have been made for performance optimizations, particularly for large directories. The script minimizes unnecessary file operations and uses efficient comparison methods.
