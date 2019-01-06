#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #file = open("text.txt", "w+") #plus means create the file if not exists


  # Open the file for appending text to the end
  file = open("text.txt", "r")

  # write some lines of data to the file
  #for i in range(10,20):
      #file.write("This is line: "+ str(i) + "\r\n")

  
  # close the file when done

  
  #file.close()
  # Open the file back up and read the contents
  if file.mode == 'r':
      contents = file.read()
      print(contents)
    
if __name__ == "__main__":
  main()

