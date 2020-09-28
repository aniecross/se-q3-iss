#!/usr/bin/env python
import json, turtle, requests, time

__author__ = """Anie Cross with help from instructor demo recordings,
Group-B discussion topics, Google search, docs.python.org, stackoverflow.com,
www.101computing.net/real-time-iss-tracker, completed with help from Tutor HPost"""

def list_astronaut():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    result = json.loads(response.text)
    print("There are currently " + str(result["number"]) + " astronauts in space:")
    print("")

    people = result["people"]

    for p in people:
        print(p["name"] + " on board of " + p["craft"])

def iss_location():
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    # This will load the world map picture
    screen.bgpic("map.gif")
    
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()
    plot_indy()

    while True:
        # A request to retrieve the current longitude and latitude of the IIS space station (real time)  
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        result = json.loads(response.text)
            
        # Provides access to required information
        location =result["iss_position"]
        lat = float(location["latitude"])
        lon = float(location["longitude"])
            
        # This will show the information on screen
        print("\nLatitude: " + str(lat))
        print("Longitude: " +str(lon))
        
        # This adds ISS on the map  
        iss.goto(lon, lat)  
        # position updates every 5 seconds
        time.sleep(5)

def plot_indy(): 
    in_loc = turtle.Turtle()
    in_loc.shape('circle')
    in_loc.turtlesize(.3, .3, .3)
    in_loc.color('yellow')     
    in_loc.penup()
    in_loc.goto(-86.159536, 39.778117)
    payload = {'lat': 39.778117, 'lon': -86.159536}
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=payload)
    location = json.loads(response.text)
    next_time = time.ctime(location['response'][0]['risetime'])
    in_loc.write(next_time)
        

def main():
    list_astronaut()
    iss_location()

if __name__ == '__main__':
    main()
    