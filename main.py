import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading #used for handing the events without errors and excetuing mainloop
import time
import imutils

#creating the play function for controlling the speed
stream= cv2.VideoCapture("v3.mp4")
def play(speed):
    print(f"the speed is {speed} ")

    #playing the video in forward or backward direction according to speed

    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)
    
    #grabs the frame1 and reads the read the stream through stream
    grabbed, frame=stream.read()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=photo
    canvas.create_image(0,0,anchor=tkinter.NW,image=photo)


def pending(decision):
    #Displaying the decision pending image
    src1=cv2.imread("decision pending.jpg")
    frame=cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #waiting for 1.5 seconds
    time.sleep(1.5)

    #Displaying sponser
    src1=cv2.imread("sponser1.jpg")
    frame=cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=photo
    canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
    time.sleep(1.5)

    #Displaying out or Not out based on the decision
    if decision=="out":
        decision_image="out.jpg"
    else:
        decision_image="not out.jpg"
    src1=cv2.imread(decision_image)
    frame=cv2.cvtColor(src1,cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=photo
    canvas.create_image(0,0,anchor=tkinter.NW,image=photo)


#creating out function
def out():
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is out")

def not_out():
    thread=threading.Thread(target=pending,args=("not_out",))
    thread.daemon= 1
    thread.start()
    print("Player is Not out")

window=tkinter.Tk()

#WIDTH AND HEIGHT OF THE MAIN SCREEN 
SET_WIDTH= 712
SET_HEIGHT=475

#TKINTER GUI STARTS HERE
window.title("THIRD UMPIRE REVIEW SYSTEM")
src=cv2.imread("background1.jpg")

#converting the image from BGR TO RGB for actual image
cv_img=cv2.cvtColor(src,cv2.COLOR_BGR2RGB)

#creating the canvas and adding the image intp it
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
#converting into canvas image object
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
#creating the image in the canvas 
image_oncanvas=canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

#creating the buttons
btn=tkinter.Button(window,width=60,text="<<Previous(fast)",command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,width=60,text="<Previous(slow)",command=partial(play,-5))
btn.pack()

btn=tkinter.Button(window,width=60,text="Next(slow)>",command=partial(play,5))
btn.pack()

btn=tkinter.Button(window,width=60,text="Next(fast)>>",command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,width=60,text="Give out",command=out)
btn.pack()

btn=tkinter.Button(window,width=60,text="Give Not out",command=not_out)
btn.pack()

window.mainloop()