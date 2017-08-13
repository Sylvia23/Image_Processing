from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()
root.title("Hashing Tool")
root.geometry("600x300")

def getfile():
    filename = askopenfilename() 
    print(filename)

frame = Frame(root)
frame.pack()
button = Button(frame, text="Choose File", fg="black", command=getfile)
button.pack( side = BOTTOM)

root.mainloop()