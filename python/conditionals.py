#
# Example file for working with conditional statements
#

def main():
  x, y = 1000, 100

  # conditional flow uses if, elif, else  
  if x < y:
      st = "x is less than y"
  elif x > y: 
      st = "x is greater than y"
  else:
      st = "x is the same as y"

  print(st)
  
  # conditional statements let you use "a if C else b"
  st = "x greater than y" if x > y else "x is same or less than y"

  print(st)

if __name__ == "__main__":
  main()

