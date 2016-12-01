# imagesDemo1.py
# view in canvas
# read from file
# with transparent pixels
# get size, resize (zoom and subsample)

# image resized, made transparent with:
# http://www.online-image-editor.com/

from tkinter import *

def redrawAll(canvas):
    canvas.delete(ALL)
    # Draw a background rectangle to highlight the transparency
    # of the images
    canvas.create_rectangle(0, 10, canvas.width, 190, fill="cyan")
    # Draw the demo info
    font = ("Arial", 16, "bold")
    msg = "Image Demo #1 (read from file)"
    canvas.create_text(canvas.width/2, 25, text=msg, font=font)
    # Draw the original size image on the left
    image = canvas.data["image"]
    imageSize = ( (image.width(), image.height()) )
    msg = "Full-size " + str(imageSize)
    canvas.create_text(canvas.width/5, 50, text=msg, font=font)
    canvas.create_image(canvas.width/5, 100, anchor=N, image=image)
    # Draw a half-size image in the middle
    image = canvas.data["halfImage"]
    imageSize = ( (image.width(), image.height()) )
    msg = "Half-size " + str(imageSize)
    canvas.create_text(canvas.width/2, 50, text=msg, font=font)
    canvas.create_image(canvas.width/2, 100, anchor=N, image=image)
    # Draw a double-size image on the right
    image = canvas.data["doubleImage"]
    imageSize = ( (image.width(), image.height()) )
    msg = "Double-size " + str(imageSize)
    canvas.create_text(canvas.width*4/5, 50, text=msg, font=font)
    canvas.create_image(canvas.width*4/5, 100, anchor=N, image=image)

def init(canvas):
    canvas.width = canvas.winfo_reqwidth()-4
    canvas.height = canvas.winfo_reqheight()-4
    image = PhotoImage(file="sampleImage1.gif")
    canvas.data["image"] = image
    halfImage = image.subsample(2,2)
    canvas.data["halfImage"] = halfImage
    doubleImage = image.zoom(2,2)
    canvas.data["doubleImage"] = doubleImage
    redrawAll(canvas)

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=1000, height=500)
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