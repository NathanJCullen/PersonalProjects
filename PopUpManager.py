#My first attempt at GUI was creating a simple application for setting up a pop up of the users choosing.
#When opened the user is met by an interface where they can choose what sound they would like played, what they would like to pop up
#and how often they would like it to pop up in seconds.

from pygame import mixer
from tkinter import *
from tkinter.filedialog import askopenfilename
import webbrowser
import time
import ntpath

soundVar = ""
fileVar = ""

def getSoundName():
	global soundVar
	soundPath = askopenfilename()
	soundVar = ntpath.basename(soundPath)

def getFileName():
	global fileVar
	filePath = askopenfilename()
	fileVar = ntpath.basename(filePath)

def stop():
	root.destroy()

def popupaction():
	
	timeVar = (int(entrytime.get())*1000)
	
	mixer.init()
	mixer.music.load(str(soundVar))
	    
	if loop:
	    root.after(timeVar, popupaction)
	    webbrowser.open(str(fileVar))
	    mixer.music.play()
	else:
		print("Popup stopped")

root = Tk()
root.title("Pop Up Manager")
root.geometry("400x130")
loop = True

soundlabel = Label(root, text="Please input the sound of your popup; Include format")
soundlabel.grid(column=0, row=0, sticky=W)
# entrysound = Entry(root)
# entrysound.grid(column=1, row=0)

timelabel = Label(root, text="Please input the time between popups")
timelabel.grid(column=0, row=1, sticky=W)
entrytime = Entry(root)
entrytime.grid(column=1, row=1)

openlabel = Label(root, text="Please input the file to open on your popup; Inlcude format")
openlabel.grid(column=0, row=2, sticky=W)
# entryopen = Entry(root)
# entryopen.grid(column=1, row=2)

createbutton = Button(root, text="Create", command=popupaction)
createbutton.grid(column=0, row= 3, columnspan=2)

soundbutton = Button(root, text="Browse", command=getSoundName)
soundbutton.grid(column=1, row= 0, sticky=W)

filebutton = Button(root, text="Browse", command=getFileName)
filebutton.grid(column=1, row= 2, sticky=W)

Button(root, text="Quit Popup", command=stop).grid(column=0, row=4, columnspan=2)

root.mainloop()
