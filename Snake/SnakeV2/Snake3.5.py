"""
made by Gladox114
https://github.com/Gladox114/Python/upload/master/Snake/
"""
import tkinter as tk
import copy

class Map:
	def __init__(self, master=None, width=500, height=500, color="black", offset=10, Block=20, MapAreaX=500, MapAreaY=500,FrameColor="pink"):
		self.master = master
		self.width = width
		self.height = height
		self.offset = offset
		self.color = color
		self.FrameColor = FrameColor
		self.Block = Block
		self.MapArea = width,height
		#print("init",self.MapArea,MapAreaX,MapAreaY)
		self.food=[]
		
	def BuildMap(self):
		self.frame = tk.Frame(self.master,height=self.MapArea[1]+(self.offset*2)-1,width=self.MapArea[0]+(self.offset*2)-1)
		self.frame.pack(fill="both",expand="true")
		self.canvas = tk.Canvas(self.frame,bg=self.FrameColor,height=self.MapArea[1]+(self.offset*2)-1,width=self.MapArea[0]+(self.offset*2)-1)
		self.canvas.pack(fill="both",expand="true")
		self.f = tk.Canvas(self.canvas,bg=self.color,height=self.MapArea[1]+2,width=self.MapArea[0]+2,highlightthickness=0)
		self.f.pack()
		self.f.place(x=self.offset,y=self.offset)
		self.f.create_rectangle(0,0,self.MapArea[1]+1,self.MapArea[0]+1,outline=self.color,fill=self.color)
		self.c = tk.Canvas(self.canvas,bg=self.color,height=self.MapArea[1],width=self.MapArea[0],highlightthickness=0)
		self.c.place(x=11,y=11)
		self.frame2 = tk.Frame(self.master,bg="blue",height=15)
		self.frame2.pack(fill="both",expand="true",side="bottom")
		"""
		self.v = tk.StringVar(value="Default Value")
		self.Label = tk.Label(self.frame2,textvariable=self.v)
		self.Label.pack(side="bottom")
		self.v.set("Score:")
"""
	def setScores(self,Players):
		self.Label=[]
		self.v = []
		for i in range(Players):
			self.v[i] = tk.StringVar()
			self.Label[i] = tk.Label(self.frame2,textvariable=self.v[i])
			self.v[i].set("Player"+i+" Score: 0")
			
	def text(self,var):
		self.v.set(str("Score:"+str(var)))

	def drawCollision(self,pos,color1="red"):
		x,y=pos
		self.c.create_oval(self.pos(x,y),fill=color1,outline=color1)
		
	def getCanvas(self):
		return self.c,self.frame,self.f
	
	def pos(self,x,y): # Converting the Map into Blocks... Not the Opposite way, It's converting Blocky Positions into Pixel Block Position
		X=x*self.Block # This
		Y=y*self.Block # And this are the left top Corner
		X2=X+self.Block # this
		Y2=Y+self.Block # and this are the right Bottom Corner
		return X,Y,X2,Y2
		
	def checkb(self,listd,a,b,c,d):  # a is the body testing if its equal to b the second body and c and d are the direction or Position to the next bubble body
		if listd[a][0]+1*c==listd[b][0]: # You can do a negative or positiv number with 
			#print("Stringasddddddddddddddddddd",listd[a][0]+1*c,listd[b][0])
			x = (listd[a][0]*self.Block)+(self.Block/2) # Getting the Posittion from the Middle of the Body to the corner of the Body
			y = (listd[a][1]*self.Block)
			x2 = x+self.Block/2
			y2 = y+self.Block
		elif listd[a][0]+1*d==listd[b][0]: # Thats the same but other direction like the all others
			#print("Stringasddddddddddddddddddd",listd[a][0]+1*d,listd[b][0])
			x = (listd[a][0]*self.Block)+(self.Block/2)
			y = (listd[a][1]*self.Block)
			x2 = x-self.Block/2
			y2 = y+self.Block
		elif listd[a][1]+1*c==listd[b][1]: # It's just finding out if the next Body part is on the other site of the Map
			#print("Stringasddddddddddddddddddd",listd[a][1]+1*c,listd[b][1])
			x = (listd[a][0]*self.Block)
			y = (listd[a][1]*self.Block)+(self.Block/2)
			x2 = x+self.Block
			y2 = y+self.Block/2
		elif listd[a][1]+1*d==listd[b][1]: # If the Snake is in y=0 and the other part y=24 by a map of y=0-y=24 then it's True and executing
			#print("Stringasddddddddddddddddddd",listd[a][1]+1*d,listd[b][1])
			x = (listd[a][0]*self.Block)
			y = (listd[a][1]*self.Block)+(self.Block/2)
			x2 = x+self.Block,
			y2 = y-self.Block/2
		else: 
			#print("Nailed")
			#print("Stringasddddddddddddddddddd",listd[a][1],listd[b][1])
			#print("Stringasddddddddddddddddddd",listd[a][1],listd[b][1])
			return False,2
		return True,(x,y,x2,y2)	
	
	def drawSnake(self,snake):
		self.c.itemconfig("snake"+str(id(snake)+snake.lastBlockChain),fill="black",outline="black")
		snake.lastBlockChain+=1
		#print("Removing snake"+str(id(snake)+snake.lastBlockChain))
		#self.snapColor = "white"
		if len(snake.body) > 1:
			i = len(snake.body)-1
			a,coord = self.checkb(snake.body,i,i-1,1,-1) # Check for body behind
			#print(coord)
			if a==True: # If the above is going through a wall then
				self.c.create_rectangle(coord,fill=snake.snapColor,outline=snake.snapColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
				#print("Adding: snake"+str(i+snake.ChainLen))
			else: #        put rectangles through
				number = abs(snake.MapChunks[0]-snake.MapChunks[2]) # Getting the distance to the opposite bubble/wall
				coord = self.checkb(snake.body,i,i-1,-number,number)[1]
				if coord==False or coord==2:
					number = abs(snake.MapChunks[1]-snake.MapChunks[3])
					coord = self.checkb(snake.body,i,i-1,-number,number)[1]
				#print(coord,number,snake.body,snake.MapChunks)
				self.c.create_rectangle(coord,fill=snake.snapColor,outline=snake.snapColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
				#print("Adding: snake"+str(i+snake.ChainLen))
			
			a,coord = self.checkb(snake.body,i-1,i,1,-1) # Check at boddy before the last one for body in front
			if a==True: # If the above is going through a wall then
				self.c.create_rectangle(coord,fill=snake.snapColor,outline=snake.snapColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
				#print("Adding: snake"+str(i+snake.ChainLen))
			else: # put rectangles through
				number = abs(snake.MapChunks[0]-snake.MapChunks[2])
				coord=self.checkb(snake.body,i-1,i,-number,number)[1]
				if coord==False or coord==2:
					number = abs(snake.MapChunks[1]-snake.MapChunks[3])
					coord=self.checkb(snake.body,i-1,i,-number,number)[1]
				self.c.create_rectangle(coord,fill=snake.snapColor,outline=snake.snapColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
				#print("Adding: snake"+str(i+snake.ChainLen))
			self.c.create_oval(self.pos(snake.body[i][0],snake.body[i][1]),fill=snake.bodyColor,outline=snake.bodyColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
			self.c.create_oval(self.pos(snake.body[i-1][0],snake.body[i-1][1]),fill=snake.bodyColor,outline=snake.bodyColor,tags="snake"+str(id(snake)+i+snake.ChainLen))
			#print("Adding: snake"+str(i+snake.ChainLen))
			snake.ChainLen+=1		# If you Playing to loong then it will get a long number and it could maybe lag. If not then I did nothing wrong.
			#print(str(id(snake)+i+snake.ChainLen))
		
	def placeFood(self,*food):
		if food: self.food = food
		if self.food != []:
			x,y,x2,y2 = self.pos(self.food[0],self.food[1])
			self.c.create_oval(x+self.Block*0.25,y+self.Block*0.25,x2-self.Block*0.25,y2-self.Block*0.25,fill="red",outline="red",tags="food")
		else: 
			print("Error: No Food")
			self.food = randomFood()
# ------------------------------
class Snake():
	def __init__(self, Map, body, Joystick, borderbool, direction, snapColor="white", bodyColor="lightblue"):
		super().__init__()
		self.Map = Map
		self.body = body
		self.Joystick = Joystick
		self.Pop = True
		self.borderbool = borderbool
		self.lastdirection = direction
		self.JoyDirection=0
		self.score = 0
		self.snapColor=snapColor
		self.bodyColor=bodyColor
		self.lastBlockChain = 0
		self.ChainLen = 0
		self.startBody = copy.deepcopy(body)
		#print(self.startBody)
		self.startDir = copy.copy(direction)
		self.lose=False
		#print(self.MapArea,self.Block)
		#print(self.Map.MapArea[0:2],int(self.Map.MapArea[0]/self.Map.Block-1))
		#print(int(self.Map.MapArea[1]/self.Map.Block-1))
		self.MapChunks=(0,0,int(self.Map.MapArea[0]/self.Map.Block-1),int(self.Map.MapArea[1]/self.Map.Block-1))
		#print(self.MapChunks[0:4])
		if self.borderbool==False: # Setting the Border Function
			self.border=self.borderOff
		elif self.borderbool==True:
			self.border=self.borderOn()
		#else:
		#	print("You need to select an option at the variable border")
		#self.border = border()
		
	def borderOff(self): # Border Option1	# If the Head is out of Map then change the location of the Head to the other site of the Map
		if self.body[-1][0] > self.MapChunks[2]: #x
			#x,y=self.body[-1]
			self.body[-1][0] = self.MapChunks[0] 
		elif self.body[-1][0] < self.MapChunks[0]:
			x,y=self.body[-1]
			self.body[-1][0] = self.MapChunks[2]

		if self.body[-1][1] > self.MapChunks[3]: #y 
			#x,y=self.body[-1]
			self.body[-1][1] = self.MapChunks[1]
		elif self.body[-1][1] < self.MapChunks[1]:
			#x,y=self.body[-1]
			self.body[-1][1] = self.MapChunks[3]

	def borderOn(self): # Border Option2
		if self.body[-1][0] > self.MapChunks[2]: #x
			self.lose=True
		elif self.body[-1][0] < self.MapChunks[0]:
			self.lose=True
		if self.body[-1][1] > self.MapChunks[3]: #y
			self.lose=True
		elif self.body[-1][1] < self.MapChunks[1]:
			self.lose=True	
	
	def popSnake(self,x): # Using this method so if you get food you can decide if you want to pop(remove) the last body part
		if self.Pop==True:
			#print(x)
			self.body.pop(x)
		else: self.Pop = True
		
	def move(self,direction):
		#print("lastDir:",self.lastdirection)
		#print("direction:",direction)
		if direction == "right" and self.lastdirection != "left": # if it's going to the Left it's not allowed to go Right (Opposite Direction)
			x,y=self.body[-1] # x & y from Head
			self.body.append([x+1,y]) # Add a body Part in the moving direction
			self.popSnake(0) # Remove the last body Part
			self.border() # Executing the border
		elif direction == "left" and self.lastdirection != "right":
			x,y=self.body[-1]
			self.body.append([x-1,y])
			self.popSnake(0)
			self.border()
		elif direction == "up" and self.lastdirection != "down":
			x,y=self.body[-1]
			self.body.append([x,y-1])
			self.popSnake(0)
			self.border()
		elif direction == "down" and self.lastdirection != "up":
			x,y=self.body[-1]
			self.body.append([x,y+1])
			self.popSnake(0)
			self.border()
		else:			# If it wasn't moving then repeat the old Movement
			direction = self.lastdirection 
			self.move(direction) 
		self.lastdirection = direction



# -----------------------------------------

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
import random
def randomFood(Player,someList): # not tested
	localMap = []
	for x in range(0,Player.MapChunks[2]+1):
		for y in range(0,Player.MapChunks[3]+1):
			localMap+=[[x,y]]
	for i in someList:
		localMap.remove(i)
	return localMap[random.randint(0,len(localMap)-1)]

def checkFood(Map,Player,Players): # not tested
	if Map.food!=[]:
		if Player.body[-1]==Map.food:
			Player.score+=1
			Map.text(Player.score)
			someList=[]
			for i in Players:
				for z in i.body:
					x,y=z
					someList+=[[x,y]]
			Map.food = randomFood(Player,someList)
			Player.Pop=False
			print(Map.food)
			Area.placeFood()
			return True
		else: return False
	else:
		someList=[]
		for i in Players:
			for z in i.body:
				x,y=z
				someList+=[[x,y]]
		Map.food = randomFood(Player,someList)
		Area.placeFood()

def collision(body,head): # If Head in a Body part (Other Player or Itself) then return True
		for i in body:
			if i==head: return True 
		return False





root = tk.Tk()
Area=Map(root,1500,500,"black",10,20,1500,500) # Creating Object from Class Map
Area.BuildMap() # Building the Map once

Player1 = Snake(Area,[[6,6],[5,6],[4,6],[3,6]],1,False,"left")
Player2 = Snake(Area,[[2,2],[3,2],[4,2],[5,2]],2,False,"right","yellow","purple")
Playerslist=[Player1,Player2]
Players=[Player1,Player2]


import Joystick as Joy

def Input():
	global stop
	for Player in Players:
		#print(Player.Joystick)
		i=getdir(Joy.location(Player.Joystick))
		if i!=0:
			Player.JoyDirection=i	# This is the Direction. If it's set then it has or gets a string named "left","right","up","down" and you could change that to a keyboard Input
	if stop==False: root.after(1,Input)

def losePlayer(Player,Players,remove=False):
	#print(type(Player.body))
	if remove:
		for i in range(len(Player.body)):
			c=Area.getCanvas()[0]
			c.itemconfig("snake"+str(id(Player)+Player.lastBlockChain),fill="black",outline="black")
			Player.lastBlockChain+=1
	Players.remove(Player)
	#del Player

def start(remove=False): # Main
	global stop
	global food
	for Player in Players: # Executing it for each Player
		Player.move(Player.JoyDirection) 
		Area.drawSnake(Player)
		checkFood(Area,Player,Players)
		for i in Players: # For each Player again
			if i!=Player: # Not the Player itself
				if collision(i.body,Player.body[-1]): # Check if Player Collides with other Player
					if remove==False: Area.drawCollision(Player.body[-1])
					Player.lose=True
			else: 
				if len(Player.body) > 4: # Check if Player Collides with itself
					if collision(i.body[0:-2],Player.body[-1]):
						if remove==False: Area.drawCollision(Player.body[-1]) 
						Player.lose=True
		if Player.lose:
			losePlayer(Player,Players,remove)
			#stop=True
		#print(Player.body)
		if len(Players)<2:
			stop=True

		
	if stop==False: root.after(100,start)
	else: 
		root.after(1000,restartScreen)

def restartScreen():
	global stop
	global Players
	global Playerslist
	Players=copy.copy(Playerslist)
	for i in Players:
		#print(i.startBody)
		i.body = copy.deepcopy(i.startBody)
		i.lastdirection = i.startDir
		i.JoyDirection = i.startDir
		i.lose=False
	#c=Area.getCanvas()[0]
	frame=Area.getCanvas()[1]
	frame.pack_forget()
	Area.BuildMap()
	stop=False
	Area.food=[]
	checkFood()
	start()
	Input()
Area.setScores(len(Playerslist))
Area.food=[5,5]
Area.placeFood()
stop=False
Input()
start()
root.wm_title("Nice Snake Game            not")
root.mainloop()




