#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  #while(x<5):
  #  print(x)
  #  x = x + 1

  # define a for loop
  #for x in range(5,10):
  #  print(x)

  # use a for loop over a collection
  #days = ["monday", "tuesday", "wednesday"]
  #for d in days:
  #    print(d)
    
 
  # use the break and continue statements
  for x in range(5,10):
    #if x == 7: break
    if (x % 2 == 0): continue
    print(x)

  #using the enumerate() function to get index 
  days = ["monday", "tuesday", "wednesday"]
  for i,d in enumerate(days):
      print(i,d) #prints the index count as well as the value
    

if __name__ == "__main__":
  main()

