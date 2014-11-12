#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "chartreuse")
		self.up.grid(row=0,column=1)
		
		self.down = Button(self.myContainer1)
		self.down.configure(text="Down", background= "white")
		self.down.grid(row = 1,column = 1)
		
		self.left = Button(self.myContainer1)
		self.left.configure(text="Left", background= "gray")
		self.left.grid(row = 0,column = 0)
		
		self.right = Button(self.myContainer1)
		self.right.configure(text="Right", background= "red")
		self.right.grid(row = 0,column = 2)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
		self.down.bind("<Button-1>", self.moveDown)
		self.left.bind("<Button-1>", self.moveLeft)
		self.right.bind("<Button-1>", self.moveRight)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
                drawpad.move(player,0, -10)
        
        def moveDown(self, event):   
		global player
		global drawpad
                drawpad.move(player, 0, 10)
                
        def moveLeft(self, event):   
		global player
		global drawpad
                drawpad.move(player, -10, 0)
                
        def moveRight(self, event):   
		global player
		global drawpad
                drawpad.move(player, 10, 0)
    
         
        # Animate function that will bounce target left and right, and trigger the collision detection
          
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)    
	    # Insert the code here to make the target move, bouncing on the edges
	    drawpad.move(target,direction,0)       
	    if tx2 > drawpad.winfo_width():
	        direction = -4
	    elif tx1 < 0:
	        direction = 4   
            
            #  This will trigger our collision detect function
            didWeHit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            if didWeHit == False:
                drawpad.after(1, self.animate)
            else:
                pass
        # that determines whether to run drawpad.after(1,self.animate) or not
	# Use a function to do our collision detection
	
        def collisionDetect(self):
            
                global target
		global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                # using x1,y1,x2,y2 = drawpad.coords(object)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                px1,py1,px2,py2 = drawpad.coords(player)
                # Do your if statement - remember to return True if successful!                
		if (px1 > tx1 and px2 < tx2) and (py1 > ty1 and py2 < ty2) :
		    return True
		else:
		    return False
myapp = MyApp(root)

root.mainloop()