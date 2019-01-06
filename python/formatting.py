#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current year is %y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Locale is: %c, date: %x and time %X"))



if __name__ == "__main__":
  main();

