from directory_comparison import compare_directories

if __name__ == '__main__':


    # dir1_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\my task\\dir1"
    # dir2_path = "C:\\Users\\Tal Ben Gozi\\Desktop\\my task\\dir2"

    dir3_path = input("Enter directory_1 path: ")
    dir4_path = input("Enter directory_2 path: ")

    print("\nSCRIPT STARTED")
    compare_directories(dir3_path, dir4_path)