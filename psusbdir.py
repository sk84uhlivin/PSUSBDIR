import os
import sys


def ps3_op():
    try:
        paths = ['MUSIC', 'PICTURE', 'PS3', 'PS3/EXPORT', 'PS3/EXPORT/BACKUP',
                 'PS3/EXPORT/PSV', 'PS3/SAVEDATA', 'PS3/THEME', 'PS3/UPDATE',
                 'VIDEO']
        for path in paths:
            print(f"Making {path}...")
            os.mkdir(path)
    except FileExistsError:
        print(f"Error: {path} already exists. Please delete it and try again.")
        input("Press any key to exit: ")
        exit()


def ps4_op():   # Experimental, can't find proper source for structure.
    try:
        os.mkdir('PS4')
        os.mkdir('PS4/Update')
        os.mkdir('PS4/Music')
        os.mkdir('IMAGES')

    except FileExistsError:
        print("Error: Some of the PS4 directory already exists. Please delete it and try again.")
        input("Press any key to exit: ")
        exit()


def main():
    # Determines if application is a script file or frozen exe.
    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
    elif __file__:
        app_path = os.path.dirname(__file__)

    print("PSUSBDIR by sk84uhlivin")
    print()
    print(f"Target location for directory is {app_path}")
    print()
    confirm = input("Do you wish to proceed? (y/n) ")
    if confirm.lower() == 'n':
        exit()
    else:
        ps3_op()
    print()
    input("Directory successfully made. Press any key to exit: ")


main()
