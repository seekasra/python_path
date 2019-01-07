#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  name = os.name
  print(name)

  # Check for item existence and type
  print("Item exists " + str(path.exists("./text.txt")))
  print("Item is file " + str(path.isfile("./text.txt")))
  print("Item is dir " + str(path.isdir("./text.txt")))
  
  # Work with file paths
  print("Item path: " + str(path.realpath("./text.txt")))
  print("Item path: " + str(path.split(path.realpath("./text.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("text.txt")) #convert a modification time into a real time
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("text.txt")))
  


  
if __name__ == "__main__":
  main()

