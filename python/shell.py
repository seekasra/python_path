#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive

def main():
  # make a duplicate of an existing file
  if path.exists("text.txt"):
    # get the path to the file in the current directory
    src = path.realpath("text.txt")
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    shutil.copy(src, dst)
    # check if the newly created file exists.
    #print("New file exists: " + str(path.exists("text.txt.bak")))
    
    # copy over the permissions, modification times, and other info
    #shutil.copystat(src, dst)

    # rename the original file
    #os.rename("text.txt", "new.txt")

    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files

      
if __name__ == "__main__":
  main()

