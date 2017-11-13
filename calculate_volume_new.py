# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-05
# This program displays volume of a cylinder 

PI = 3.14

def get_volume(radius,height):
    
    
    volume = 2 * PI * radius**2 * height
    return volume 
    
radius = int(raw_input('Type in radius : '))
height = int(raw_input('Type in height : '))
volume = get_volume(radius, height)
print(str(volume) + "unit^3 ")

