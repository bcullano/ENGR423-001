#import the tello Library
from tello import Tello

#Create tello controller object
tello = Tello()

#Enter the aircraft into SDK Mode
tello.send_command('command')

#Take off the aircraft
tello.send_command('takeoff')

#Go from (x, y, z) = [0,0,0] to (x, y, z) = [75,75,0] at speed of 50 cm/s and back
tello.send_command('go 100 100 0 50')
tello.send_command('go -100 -100 0 50')

# Rotate 360 degrees clockwise
tello.send_command('cw 360')

#Go up 100cm
tello.send_command('up 100')

#Go down 100cm
tello.send_command('down 100')

#Right 100cm
tello.send_command('right 100')

#Left 100cm
tello.send_command('left 100')

#Forward 100cm
tello.send_command('forward 100')

#Back 100cm
tello.send_command('back 100')

#Flip
tello.send_command('flip f')

#Land the aircraft
tello.send_command('land')
