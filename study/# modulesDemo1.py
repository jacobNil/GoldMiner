# modulesDemo1.py

# Does not use modules
# Creates a face and displays it
# The face can either smile or frown

from tkinter import *

#######################
# makeFace and drawFace
#######################

def makeFace(canvas, left, top, right, bottom, isSmiley):
    return dict([ ("canvas", canvas),
                  ("left", left),
                  ("top", top),
                  ("right", right),
                  ("bottom", bottom),
                  ("isSmiley", isSmiley)
                  ])

def drawFace(face):
    # extract the values from the "face" dict
    canvas = face["canvas"]
    isSmiley = face["isSmiley"]
    (x0, y0, x1, y1) = (face["left"], face["top"], face["right"], face["bottom"])
    (cx, cy) = ( (x0 + x1)/2, (y0 + y1)/2 )
    (dx, dy) = ( (x1 - x0), (y1 - y0) )
    # draw the head
    canvas.create_oval(x0, y0, x1, y1, fill="yellow")
    # draw the eyes
    eyeRx = dx/8
    eyeRy = dy/8
    eyeCx1 = cx - dx/5
    eyeCx2 = cx + dx/5
    eyeCy = y0 + dy/3
    canvas.create_oval(eyeCx1-eyeRx, eyeCy-eyeRy,
                       eyeCx1+eyeRx, eyeCy+eyeRy,
                       fill="black")
    canvas.create_oval(eyeCx2-eyeRx, eyeCy-eyeRy,
                       eyeCx2+eyeRx, eyeCy+eyeRy,
                       fill="black")
    # draw the nose
    noseRx = eyeRx/2
    noseRy = eyeRy
    noseCx = cx
    noseCy = cy + dy/24
    canvas.create_oval(noseCx-noseRx, noseCy-noseRy,
                       noseCx+noseRx, noseCy+noseRy,
                       fill="black")
    # draw the mouth
    mouthCx = cx
    mouthCy = y0 + dy*4/5
    mouthRx = dx/4
    mouthRy = dy/8
    mx0 = mouthCx - mouthRx
    mx1 = mouthCx + mouthRx
    if (isSmiley):
        # draw arc across bottom half of upper-mouth rectangle
        my0 = mouthCy - 3*mouthRy
        my1 = mouthCy + mouthRy
        canvas.create_arc(mx0, my0, mx1, my1,
                          start=180, extent=180,
                          style="arc", width=mouthRy/4)
    else:
        # draw arc across top half of lower-mouth rectangle
        my0 = mouthCy - mouthRy
        my1 = mouthCy + 3*mouthRy
        canvas.create_arc(mx0, my0, mx1, my1,
                          start=0, extent=180,
                          style="arc", width=mouthRy/4)


#######################
# redrawAll and init
#######################

def redrawAll(canvas):
    canvas.delete(ALL)
    # Draw the demo info
    font = ("Arial", 16, "bold")
    msg = "Modules Demo1:  No Module"
    canvas.create_text(canvas.width/2, 25, text=msg, font=font)
    # Draw the face
    drawFace(canvas.data["face1"])
    drawFace(canvas.data["face2"])

def init(canvas):
    canvas.width = canvas.winfo_reqwidth() - 4
    canvas.height = canvas.winfo_reqheight() - 4
    canvas.data["face1"] = makeFace(canvas,
                                    0, 50,
                                    canvas.width/2, canvas.height,
                                    True) # True = smiley
    canvas.data["face2"] = makeFace(canvas,
                                    canvas.width/2, 50,
                                    canvas.width, canvas.height,
                                    False) # False = frowny
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=300, height=200)
    canvas.pack(fill=BOTH, expand=YES)
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    # root.bind("<Button-1>", leftMousePressed)
    # root.bind("<KeyPress>", keyPressed)
    # timerFired(canvas)
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

run()