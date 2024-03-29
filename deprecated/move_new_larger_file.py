import glob
import os
import pathlib
import shutil
import sys


def main():
    tempPathName = "newFilesBigger"
    pathlib.Path(tempPathName).mkdir(parents=True, exist_ok=True)

    oldFormat = sys.argv[1]
    newFormat = sys.argv[2]

    oldFiles = glob.glob(f"*{oldFormat}")
    newFiles = glob.glob(f"*{newFormat}")

    # if old file is larger than new file, move it to new folder
    for oldFile in oldFiles:
        # check if new file is exist, if not, ignore, else compare size and move both old and new files if the new file is bigger
        newFile = oldFile.replace(oldFormat, newFormat)
        if newFile in newFiles:
            if os.path.getsize(oldFile) > os.path.getsize(newFile):
                shutil.move(oldFile, tempPathName)
                shutil.move(newFile, tempPathName)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    exit()
