from directory_comparison import compare_directories

if __name__ == '__main__':

    dir1_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\task\\dir1"
    dir2_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\task\\dir2"

    # dir3_path = input("Enter directory Path one")
    # dir4_path = input("Enter directory Path Two")

    print("\nSCRIPT STARTED")
    compare_directories(dir1_path, dir2_path)