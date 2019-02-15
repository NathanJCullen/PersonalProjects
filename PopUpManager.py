#Version 1.2. Updated to add a text field that displays the name of the file seclected by the user for sound and popup.

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
	soundname.grid(column = 2, row=0)
	soundname.insert(INSERT, soundVar)

def getFileName():
	global fileVar
	filePath = askopenfilename()
	fileVar = ntpath.basename(filePath)
	filename.grid(column = 2, row=2)
	filename.insert(INSERT, fileVar)

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
# root.geometry("600x130")
loop = True

soundlabel = Label(root, text="Browse your PC for the wanted sound")
soundlabel.grid(column=0, row=0, sticky=W)
soundbutton = Button(root, text="Browse", command=getSoundName)
soundbutton.grid(column=1, row= 0, sticky=W)
soundname = Text(root, height=1, width=30)

timelabel = Label(root, text="Please input the time between popups in seconds")
timelabel.grid(column=0, row=1, sticky=W)
entrytime = Entry(root)
entrytime.grid(column=1, row=1)

openlabel = Label(root, text="Brose your pc for the wanted pop up file")
openlabel.grid(column=0, row=2, sticky=W)
filebutton = Button(root, text="Browse", command=getFileName)
filebutton.grid(column=1, row= 2, sticky=W)
filename = Text(root, height=1, width=30)

createbutton = Button(root, text="Create", command=popupaction)
createbutton.grid(column=0, row= 3, columnspan=2)



Button(root, text="Quit Popup", command=stop).grid(column=0, row=4, columnspan=2)

root.mainloop()
