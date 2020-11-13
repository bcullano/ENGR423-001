from tello import Tello
import msvcrt

tello = Tello()
tello.send_command('command')

#Check Battery
def battery():
	tello.send_command('battery?')

#Square
def sq():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	for i in range(4):
		tello.send_command('forward 50')
		tello.send_command('cw 90')
	tello.send_command('land')

#Circle
def circ():
	tello.send_command('takeoff')
	tello.send_command('down 40')
	tello.send_command('curve 60 -60 0 0 -120 0 20')
	tello.send_command('curve -60 60 0 0 120 0 20')
	tello.send_command('land')

#Pentagon
def pent():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	for i in range(5):
		tello.send_command('forward 50')
		tello.send_command('cw 72')
	tello.send_command('land')

#Hexagon
def hex():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	for i in range(6):
		tello.send_command('forward 50')
		tello.send_command('cw 60')
	tello.send_command('land')

#Lawn Mower
def mow():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	for i in range(2):
		tello.send_command('forward 75')
		tello.send_command('cw 90')
		tello.send_command('forward 30')
		tello.send_command('cw 90')
		tello.send_command('forward 75')
		tello.send_command('ccw 90')
		tello.send_command('forward 30')
		tello.send_command('ccw 90')
	tello.send_command('left 120')
	tello.send_command('land')

#Expanding Square
def expand():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	dist = 20 
	for i in range(4):
		dist += 20
		tello.send_command('forward '+str(dist))
		tello.send_command('cw 90')
	tello.send_command('land')

#Sector
def sector():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	for i in range(3):
		tello.send_command('forward 75')
		tello.send_command('cw 120')
		tello.send_command('forward 25')
		tello.send_command('cw 105')
	tello.send_command('forward 40')
	tello.send_command('land')

#Keyboard Input
def free():
	tello.send_command('takeoff')
	while True:
		direction = msvcrt.getch()
		if direction.lower() == 'w':
			tello.send_command('forward 20')
		elif direction.lower() == 's':
			tello.send_command('back 20')
		elif direction.lower() == 'a':
			tello.send_command('left 20')
		elif direction.lower() == 'd':
			tello.send_command('right 20')
		elif direction.lower() == 'i':
			tello.send_command('up 20')
		elif direction.lower() == 'k':
			tello.send_command('down 20')
		elif direction.lower() == 'j':
			tello.send_command('ccw 45')
		elif direction.lower() == 'l':
			tello.send_command('cw 45')
		elif direction.lower() == 'q':
			tello.send_command('land')
			break
		else:
			print('Unavailable action')


#Obstacle Avoidance
def avoid1():
	tello.send_command('takeoff')
	tello.send_command('down 50')
	tello.send_command('forward 30')
	tello.send_command('up 75')
	tello.send_command('forward 100')
	tello.send_command('land')

def avoid2():
	tello.send_command('takeoff')
	tello.send_command('forward 40')
	tello.send_command('up 60')
	tello.send_command('forward 100')
	tello.send_command('down 125')
	tello.send_command('forward 30')
	tello.send_command('up 50')
	tello.send_command('forward 70')
	tello.send_command('left 20')
	tello.send_command('up 60')
	tello.send_command('left 100')
	tello.send_command('land')

#Action Input
while True:
	drone_action = raw_input('Enter action: ')
	if drone_action.lower() == 'square':
		sq()
	elif drone_action.lower() == 'circle':
		circ()
	elif drone_action.lower() == 'pentagon':
		pent()
	elif drone_action.lower() == 'hexagon':
		hex()
	elif drone_action.lower() == 'lawn'or drone_action.lower() == 'mower'or drone_action.lower() == 'lawn mower':
		mow()
	elif drone_action.lower() == 'expand'or drone_action.lower() == 'expanding square':
		expand()
	elif drone_action.lower() == 'sector':
		sector()
	elif drone_action.lower() == 'keyboard'or drone_action.lower() == 'free':
		free()
	elif drone_action.lower() == 'obstacle1':
		avoid1()
	elif drone_action.lower() == 'obstacle2':
		avoid2()
	elif drone_action.lower() == 'battery':
		battery()
	elif drone_action.lower() == 'quit':
		tello.send_command('land')
		break
	else:
		print('Action not available.')