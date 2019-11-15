"""
Snake Game on a 8x8 LED Matrix made by Gladox114
https://pastebin.com/v0wVd9Sp
"""
import Matrix as M
import Joystick as Joy
#import Display as disp
import random
import time
import threading
import copy

border=True
Map = 1,1,8,8

Joy.setup()
M.setup()

display=[
	"00000000",
	"00000000",
	"00010000",
	"00101000",
	"00010100",
	"00001010",
	"00000100",
	"00000000"]
	
u=[
	"00000000",
	"00000000",
	"00100100",
	"00100100",
	"00100100",
	"00111100",
	"00000000",
	"00000000"]
su=[
	"00000000",
	"00000000",
	"11101001",
	"10001001",
	"11101001",
	"00101001",
	"11101111",
	"00000000"]
ck=[
	"00000000",
	"00000000",
	"11101001",
	"10001010",
	"10001100",
	"10001010",
	"11101001",
	"00000000"]


#terminalMap=[]

snake=[[1,1],[1,2],[2,2]] #X,Y
food=[5,5]			# Jeden zweiten oder dritten display tick anzeigen
#direction="right"	# Jeden Tick nach vorne bewegen
joydir="right"
lastdirection="right"
oldSnake=[]
score=0
lastScore=0

def move(direction):
	global lastdirection
	global oldSnake
	print("lastDir:",lastdirection)
	print("direction:",direction)
	if direction == "right" and lastdirection != "left": # x + 1
		x,y=snake[-1]
		snake.append([x+1,y])
		oldSnake = snake.pop(0)
		#print("old:",oldSnake)
		border()
		#print("thats right")
	elif direction == "left" and lastdirection != "right":
		x,y=snake[-1]
		snake.append([x-1,y])
		oldSnake = snake.pop(0)
		border()
	elif direction == "up" and lastdirection != "down":
		x,y=snake[-1]
		snake.append([x,y-1])
		oldSnake = snake.pop(0)
		border()
	elif direction == "down" and lastdirection != "up":
		x,y=snake[-1]
		snake.append([x,y+1])
		oldSnake = snake.pop(0)
		border()
	else:
		direction = lastdirection
		move(direction)
	lastdirection = direction
#	return lastdirection

#print(move("right"))
#print(snake)
#print(move("right"))
#print(snake)
#print(move("right"))
#print(snake)
#print(move("down"))
#print(snake)


def getdir(x,*y):
	if type(x) == tuple:
		x,y = x
	if y == 1:
		y="down"
	elif y == 2:
		y="up"
	if x == 1:
		x="left"
	elif x == 2:
		x="right"
	if type(x) == str and type(y) == str:
		out=0
	elif type(x) == str:
		out=x
	elif type(y) == str:
		out=y
	else: out=0
	#print("dir:",out)
	return out

if border==False:
	def border():
		if snake[-1][0] > Map[2]: #x
			x,y=snake[-1]
			snake[-1][0] = Map[0]
			#oldSnake = snake.pop(0)
		elif snake[-1][0] < Map[0]:
			x,y=snake[-1]
			snake[-1][0] = Map[2]
			#oldSnake = snake.pop(0)

		if snake[-1][1] > Map[3]: #y
			x,y=snake[-1]
			snake[-1][1] = Map[1] #snake.append([x,1])
			#oldSnake = snake.pop(0)
		elif snake[-1][1] < Map[1]:
			x,y=snake[-1]
			snake[-1][1] = Map[3]
			#oldSnake = snake.pop(0)
elif border==True:
	def border():
		global lose
		if snake[-1][0] > Map[2]: #x
			lose=True
		elif snake[-1][0] < Map[0]:
			lose=True
		if snake[-1][1] > Map[3]: #y
			lose=True
		elif snake[-1][1] < Map[1]:
			lose=True
else:
	print("You need to select an option at the variable border")

	

"""
def randomFood(data):
	k=M.emptyPixels(data)
	print("emptyPixels:",k)
	if k != []:
		rmInt = random.randint(0,len(k)-1)
		return k[rmInt]
	else:
		return "full"
"""
def randomFood2(data):
	allPixels=M.getPixels(data)
	for i in range(0,len(snake)):
		allPixels.remove(snake[i])
	randomInt = random.randint(0,len(allPixels)-1)
	return allPixels[randomInt]

def checkFood(data):
	global food
	global score
	if snake[-1] == food:
		score+=1
		food = randomFood2(data)
		return True
	else: 
		return False

def loseScreen():
	global u
	global su
	global ck
	M.screen(M.conv(u),50)
	M.screen(M.conv(su),50)
	M.screen(M.conv(ck),50)


def ScoreShow(): #Handle Nothing
	print (threading.currentThread().getName(), 'Starting')
	t = threading.currentThread()
	disp.msg("Score: "+str(score),0,0)
	disp.msg(" ")
	print (threading.currentThread().getName(), 'Exiting')

t1 = threading.Thread(target=ScoreShow)

#for i in range(0,4):
while True:
	snake=[[1,1],[1,2],[2,2]] #X,Y
	food=[5,5]			# Jeden zweiten oder dritten display tick anzeigen
	#direction="right"	# Jeden Tick nach vorne bewegen
	joydir="right"
	lastdirection="right"
	oldSnake=[]
	score=0
	lastScore=0
	try:
		#t1.start()
		global lose
		global food
		global display
		global oldSnake
		global display
		global joydir
		global score
		lose = False
		f=copy.deepcopy(display)
		M.screen(M.conv(f),100)
		#t1.start()
		#t2.start()
		#t3.start()
		time.sleep(1)
		display = M.getBlank()
		x,y = food
		M.setPixel(display,x,y,1)
		foodDisp=M.getBlank()
		M.setPixel(foodDisp,x,y,1)
		while True:
			
			
			if checkFood(display)==False: # Check if Head on food and then score 
				if oldSnake != []:
					x,y = oldSnake
					#print("oldSnake",oldSnake,x,y)
					M.setPixel(display,x,y,0)
					oldSnake=[]
			else:
				global food
				if oldSnake != []:
					x,y = oldSnake
					snake.insert(0,[x,y])
				print(food)
				x,y = food
				M.setPixel(display,x,y,1)
				foodDisp=M.getBlank()
				M.setPixel(foodDisp,x,y,1)
			if len(snake) > 4:
				for i in range(0,len(snake[0:-4])):
					if snake[-1]==snake[i]:
						lose=True
			
			
			if lose: # Check if the player failed
				loseScreen()
				break
			
			for i in range(0,len(snake)):
				#print("debug Display",display)
				x,y = snake[i]
				M.setPixel(display,x,y,1)
				
			for b in range(0,5): # 1 range = 0.1sec
				for a in range(0,10): # 1 range = 0.001sec
					for i in range(0,3):
						f = copy.deepcopy(foodDisp)
						M.screenShort(M.conv(f))
					f = copy.deepcopy(display)
					M.screenShort(M.conv(f))
					#time.sleep(0.0001)
				jey = getdir(Joy.location())	#Get JoyDirection
				if jey != 0:
					joydir = jey
			move(joydir)
				
			if score > lastScore:
				#t1.join()
				lastScore = score
			print("Score:",score,"\n",snake,"Food:",food)
			
	except KeyboardInterrupt:
		Joy.destroy()
		break

Joy.destroy()
#disp.clear()
