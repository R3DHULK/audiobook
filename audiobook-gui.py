import tkinter as tk
from tkinter import *
import PyPDF2
import pyttsx3
from tkinter import filedialog
def browse():
    global pdfReader
    file= filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF Files","*.pdf"),("All Files","*.*")))
    pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    pathlabel.config(text=file)#configuring the pathlabel Label
def save():
    global speaker
    speaker = pyttsx3.init()
 
    for page_num in range(pdfReader.numPages):
        text =  pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
root = Tk()#creating GUI window
root.geometry('400x150')#geometry of window
root.configure(bg='green')
root.title("HULK Office: AudioBook")#title of window
Label(root, text="AUDIOBOOK",font="Arial 15",bg='white').pack()
pathlabel = Label(root)
pathlabel.pack()

Button(root,text="Browse A File",command=browse).pack()
Button(root,text="Make Him Say",command=save).pack()

root.mainloop()