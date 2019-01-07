# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
      print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  print(str(theJSON["metadata"]["count"])+ " events recorded!")

  # for each event, print the place where it occurred
  #for ft in theJSON["features"]:
  #    print(ft["properties"]["place"])

  # print the events that only have a magnitude greater than 4
  for ft in theJSON["features"]:
      if ft["properties"]["mag"] > 4.5:
          print(ft["properties"]["place"] + " with the mag of : %2.1f" % ft["properties"]["mag"])
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
      print("recieved error, cannot parse results")


if __name__ == "__main__":
  main()

