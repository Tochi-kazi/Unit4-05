# Created by : Tochukwu Iroakazi
# Created on : oct-2017
# Created for : ICS3UR-1 
# Daily Assignment - Unit3-05
# This program displays volume of a cylinder 



def get_volume(units):
    
    
    volume = 2 * 3.14 * radius**2 * height
    print(volume)
    
radius = int(raw_input('Type in radius : '))
height = int(raw_input('Type in height : '))
units = get_volume(radius)
units = get_volume(height)
