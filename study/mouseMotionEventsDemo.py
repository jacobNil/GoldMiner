# mouseMotionEventsDemo.py
#
# mouseMotion (when button is not pressed)
# mousePressed, mouseMoved, mouseReleased
# with left or right button
# and with ctrl and shift

from Tkinter import *

def eventInfo(eventName, x, y, ctrl, shift):
    # helper function to create a string with the event's info
    # also, prints the string for debug info
    msg = ""
    if ctrl:  msg += "ctrl-"
    if shift: msg += "shift-"
    msg += eventName
    msg += " at " + str((x,y))
    print msg
    return msg

def mouseMotion(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("mouseMotion", event.x, event.y, ctrl, shift)
    canvas.data["motionPosn"] = (event.x, event.y)
    redrawAll(canvas)

def leftMousePressed(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("leftMousePressed", event.x, event.y, ctrl, shift)
    canvas.data["leftPosn"] = (event.x, event.y)
    redrawAll(canvas)

def leftMouseMoved(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)
    canvas.data["info"] = eventInfo("leftMouseMoved", event.x, event.y, ctrl, shift)
    canvas.data["leftPosn"] = (event.x, event.y)
    redrawAll(canvas)

def leftMouseReleased(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)
    canvas.data["info"] = eventInfo("leftMouseReleased", event.x, event.y, ctrl, shift)
    canvas.data["leftPosn"] = (200, 100)
    redrawAll(canvas)

def rightMousePressed(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("rightMousePressed", event.x, event.y, ctrl, shift)
    canvas.data["rightPosn"] = (event.x, event.y)
    redrawAll(canvas)

def rightMouseMoved(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("rightMouseMoved", event.x, event.y, ctrl, shift)
    canvas.data["rightPosn"] = (event.x, event.y)
    redrawAll(canvas)

def rightMouseReleased(event):
    canvas = event.widget.canvas
    ctrl  = ((event.state & 0x0004) != 0)
    shift = ((event.state & 0x0001) != 0)    
    canvas.data["info"] = eventInfo("rightMouseReleased", event.x, event.y, ctrl, shift)
    canvas.data["rightPosn"] = (400, 200)
    redrawAll(canvas)

def redrawAll(canvas):
    canvas.delete(ALL)
    font = ("Arial", 24, "bold")
    # Draw the "M"
    (cx, cy) = canvas.data["motionPosn"]
    canvas.create_text(cx, cy, text="M", font=font)
    # Draw the "L"
    (cx, cy) = canvas.data["leftPosn"]
    canvas.create_text(cx, cy, text="L", font=font)
    # Draw the "R"
    (cx, cy) = canvas.data["rightPosn"]
    canvas.create_text(cx, cy, text="R", font=font)
    # Draw the event info message
    font = ("Arial", 16, "bold")
    info = canvas.data["info"]
    canvas.create_text(300, 25, text=info, font=font)

def init(canvas):
    canvas.data["motionPosn"] = (300, 300)
    canvas.data["leftPosn"]   = (200, 100)
    canvas.data["rightPosn"]  = (400, 200)
    canvas.data["info"] = "Mouse Events Demo"
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=600, height=300)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", leftMousePressed)
    root.bind("<Button-3>", rightMousePressed)
    canvas.bind("<Motion>", mouseMotion)
    canvas.bind("<B1-Motion>", leftMouseMoved)
    canvas.bind("<B3-Motion>", rightMouseMoved)
    root.bind("<B1-ButtonRelease>", leftMouseReleased)
    root.bind("<B3-ButtonRelease>", rightMouseReleased)
    # root.bind("<Key>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()