"""
Made By Gladox114

"""

from PIL import Image, ImageTk
import tkinter as tk
import random
root = tk.Tk()
class snake:
	def __init__(self):
		
		self.body = [[2,2],[3,2]]
		self.lastdirection = "right"
		
	#def move(self,direction=self.lastdirection,grow=False)
	
	#def right(self):
	

	"""
		for i in range(len(self.body)):
			self.body.append([self.x,self.y])
			self.lastbody = self.body.pop()
"""

Block = 20
Map = 500


snake=[[2,1],[2,2],[2,3],[3,3]]
food=[10,12]
score=0

offset=10

frame = tk.Frame(root,height=Map+(offset*2)-1,width=Map+(offset*2)-1)
frame.pack(fill="both",expand="true")
canvas = tk.Canvas(frame,bg="pink",height=Map+(offset*2)-1,width=Map+(offset*2)-1)
canvas.pack(fill="both",expand="true")
f = tk.Canvas(canvas,bg="black",height=Map+2,width=Map+2,highlightthickness=0)
f.pack()
f.place(x=offset,y=offset)
f.create_rectangle(0,0,Map+1,Map+1,outline="red",fill="black")

c = tk.Canvas(canvas,bg="black",height=Map,width=Map,highlightthickness=0)
c.place(x=11,y=11)


def pos(x,y):
	X=x*Block
	Y=y*Block
	X2=X+Block
	Y2=Y+Block
	return X,Y,X2,Y2
	
def checkb(listd,a,b,c,d):  # a is the body testing if its equal to b the second body and c and d are the direction or Position to the next bubble body
	if listd[a][0]+1*c==listd[b][0]:
		#print("Very Long text here so how se goeng?")
		x = (listd[a][0]*Block)+(Block/2)
		y = (listd[a][1]*Block)
		x2 = x+Block/2
		y2 = y+Block
	elif listd[a][0]+1*d==listd[b][0]:
		x = (listd[a][0]*Block)+(Block/2)
		y = (listd[a][1]*Block)
		x2 = x-Block/2
		y2 = y+Block
	elif listd[a][1]+1*c==listd[b][1]:
		x = (listd[a][0]*Block)
		y = (listd[a][1]*Block)+(Block/2)
		x2 = x+Block
		y2 = y+Block/2
	elif listd[a][1]+1*d==listd[b][1]:
		#if d==-24: print("ooooooooooooooooo")
		x = (listd[a][0]*Block)
		y = (listd[a][1]*Block)+(Block/2)
		x2 = x+Block,
		y2 = y-Block/2
	else: return False,2
	return True,(x,y,x2,y2)

# -------- Drawing Snake ---------
lastBlockChain=0
def drawSnake2():
	global lastBlockChain
	global ChainLen
	c.itemconfig("snake"+str(lastBlockChain),fill="black",outline="black")
	lastBlockChain+=1
	print("Removing snake"+str(lastBlockChain))
	global Block
	snapcolor = "white"
	if len(snake) > 1:
		i = len(snake)-1
		a,coord = checkb(snake,i,i-1,1,-1) # Check for body behind
		if a==True: # If the above is going through a wall then
			c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
			print("Adding: snake"+str(i+ChainLen))
		else: # put rectangles through
			number = abs(MapChunks[0]-MapChunks[2])
			coord = checkb(snake,i,i-1,-number,number)[1]
			c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
			print("Adding: snake"+str(i+ChainLen))
		
		a,coord = checkb(snake,i-1,i,1,-1) # Check at one boddy before the last one for body in front
		if a==True: # If the above is going through a wall then
			c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
			print("Adding: snake"+str(i+ChainLen))
		else: # put rectangles through
			number = abs(MapChunks[0]-MapChunks[2])
			coord=checkb(snake,i-1,i,-number,number)[1]
			c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
			print("Adding: snake"+str(i+ChainLen))
		c.create_oval(pos(snake[i][0],snake[i][1]),fill="lightblue",outline="lightblue",tags="snake"+str(i+ChainLen))
		c.create_oval(pos(snake[i-1][0],snake[i-1][1]),fill="lightblue",outline="lightblue",tags="snake"+str(i+ChainLen))
		print("Adding: snake"+str(i+ChainLen))
		ChainLen+=1
		print(len(snake))
	
	
ChainLen = 0
"""
def drawSnake():
	global Block
	global ChainLen
	snapcolor = "white"
	if len(snake) > 1:
		for i in range(len(snake)):
			if i != 0 and i != len(snake)-1:
				#print(i,len(snake))
				# ------Body (Middle) ---
				
				
				a,coord = checkb(snake,i,i-1,1,-1) # Check for body behind
				if a==True: # If the above is going through a wall then
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
				else: # put rectangles through
					number = abs(MapChunks[0]-MapChunks[2])
					coord = checkb(snake,i,i-1,-number,number)[1]
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))	
						
						
				a,coord = checkb(snake,i,i+1,1,-1) # Check for body in front
				if a==True: # If the above is going through a wall then
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
				else: # put rectangles through
					number = abs(MapChunks[0]-MapChunks[2])
					coord=checkb(snake,i,i+1,-number,number)[1]
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
			# -------- Body Last----
			elif i==0: 
				a,coord = checkb(snake,i,i+1,1,-1) # Check for body in front
				if a==True: # If the above is going through a wall then
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
				else: # put rectangles through
					number = abs(MapChunks[0]-MapChunks[2])
					coord=checkb(snake,i,i+1,-number,number)[1]
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
			else:
				a,coord = checkb(snake,i,i-1,1,-1) # Check for body behind
				if a==True: # If the above is going through a wall then
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
				else: # put rectangles through
					number = abs(MapChunks[0]-MapChunks[2])
					coord = checkb(snake,i,i-1,-number,number)[1]
					c.create_rectangle(coord,fill=snapcolor,outline=snapcolor,tags="snake"+str(i+ChainLen))
					print("Adding: snake"+str(i+ChainLen))
			
	for i in range(len(snake)):
		c.create_oval(pos(snake[i][0],snake[i][1]),fill="lightblue",outline="lightblue",tags="snake"+str(i+ChainLen))
	ChainLen=0
"""
# --------------------------------
def Food():
	if food != []:
		x,y,x2,y2 = pos(food[0],food[1])
		c.create_oval(x+Block*0.25,y+Block*0.25,x2-Block*0.25,y2-Block*0.25,fill="red",outline="red",tags="food")


def randomFood():
	global MapChunks
	localMap = []
	for x in range(0,MapChunks[2]+1):
		for y in range(0,MapChunks[3]+1):
			localMap+=[[x,y]]
	return localMap[random.randint(0,len(localMap)-1)]

def checkFood():
	global score
	global food
	if snake[-1]==food:
		score+=1
		food = randomFood()
		Food()
		return True
	else: return False


def checkCollision():
	if len(snake) > 4:
		for i in range(0,len(snake)-1):
			if snake[-1]==snake[i]:
				c.create_oval(pos(snake[i][0],snake[i][1]),fill="red",outline="red",tags="snake")
				return True
	else: return False

#---------------------- Key Controlls ---------------------
if True: # Because then I can hide the Controlls
	import Joystick as Joy
	Joy.setup()
	border=False
	joydir="right"
	lastdirection="right"
	MapChunks=0,0,int(Map/Block-1),int(Map/Block-1)
	
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
			if snake[-1][0] > MapChunks[2]: #x
				x,y=snake[-1]
				snake[-1][0] = MapChunks[0]
				#oldSnake = snake.pop(0)
			elif snake[-1][0] < MapChunks[0]:
				x,y=snake[-1]
				snake[-1][0] = MapChunks[2]
				#oldSnake = snake.pop(0)

			if snake[-1][1] > MapChunks[3]: #y
				x,y=snake[-1]
				snake[-1][1] = MapChunks[1] #snake.append([x,1])
				#oldSnake = snake.pop(0)
			elif snake[-1][1] < MapChunks[1]:
				x,y=snake[-1]
				snake[-1][1] = MapChunks[3]
				#oldSnake = snake.pop(0)
	elif border==True:
		def border():
			global lose
			if snake[-1][0] > MapChunks[2]: #x
				lose=True
			elif snake[-1][0] < MapChunks[0]:
				lose=True
			if snake[-1][1] > MapChunks[3]: #y
				lose=True
			elif snake[-1][1] < MapChunks[1]:
				lose=True
	else:
		print("You need to select an option at the variable border")

	Pop = True
	
	def popSnake(x):
		global Pop
		if Pop==True:
			snake.pop(x)
		else: Pop = True

	def move(direction):
		global lastdirection
		global oldSnake
		print("lastDir:",lastdirection)
		print("direction:",direction)
		if direction == "right" and lastdirection != "left": # x + 1
			x,y=snake[-1]
			snake.append([x+1,y])
			popSnake(0)
			border()
		elif direction == "left" and lastdirection != "right":
			x,y=snake[-1]
			snake.append([x-1,y])
			popSnake(0)
			border()
		elif direction == "up" and lastdirection != "down":
			x,y=snake[-1]
			snake.append([x,y-1])
			popSnake(0)
			border()
		elif direction == "down" and lastdirection != "up":
			x,y=snake[-1]
			snake.append([x,y+1])
			popSnake(0)
			border()
		else:
			direction = lastdirection
			move(direction)
		lastdirection = direction
#----------------------------------------------------------

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        
        load = Image.open("Snake/crying.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=-260, y=-100)

lose = False

def Input():
	global joydir
	global lose
	i = getdir(Joy.location())
	if i != 0:
		joydir = i
	if lose==False: root.after(10,Input)

def tick():
	global joydir
	global Pop
	global lose
	move(joydir)
	drawSnake2()
	if checkFood()==True:
		Pop=False
	if checkCollision()==True:
		lose=True
	#print(snake,food)
	if lose==False: root.after(100,tick)

def timeManager():
	root.after(10,Input)
	root.after(1000,tick)

timeManager()
drawSnake()
#snake.append([3,4])
#snake.pop(0)
Food()
app = Window(root)
root.wm_title("Nice Snake Game            not")
root.mainloop()
