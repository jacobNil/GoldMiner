# button-demo4.py
# button with an image 
# (otherwise, same as button-demo3.py)

from tkinter import *

def button1Pressed():
    # accesses canvas as a global variable
    global canvas
    canvas.data["count1"] += 1
    redrawAll(canvas)

def button2Pressed():
    global canvas
    canvas.data["count2"] += 1
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    # background (fill canvas)
    canvas.create_rectangle(0,0,300,300,fill="cyan")
    # print counts
    msg = "count1: " + str(canvas.data["count1"])
    canvas.create_text(150,130,text=msg)
    msg = "count2: " + str(canvas.data["count2"])
    canvas.create_text(150,170,text=msg)
    # print buttons in window
    b1 = canvas.data["button1"]
    canvas.create_window(50, 100, window=b1)
    b2 = canvas.data["button2"]
    canvas.create_window(50, 200, window=b2)

def init(root, canvas):
    canvas.data["count1"] = 0
    canvas.data["count2"] = 0
    b1 = Button(canvas, text="button1", command=button1Pressed)
    canvas.data["button1"] = b1
    buttonImage = PhotoImage(file="button.gif")
    b2 = Button(canvas, image=buttonImage, width=50, height=50, bg="yellow", command=button2Pressed)
    b2.image = buttonImage # save image from garbage collector (needed!)
    canvas.data["button2"] = b2
    canvas.pack() # moved canvas packing to here (before button packing!)
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    global canvas # make canvas global for button1Pressed function
    canvas = Canvas(root, width=300, height=300)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(root, canvas)
    # set up events
    #root.bind("<Button-1>", mousePressed)
    #root.bind("<Key>", keyPressed)
    #timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()