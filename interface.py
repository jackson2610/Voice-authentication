from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from voicerecognition import voice_recognition

def voiceRec():
    if voice_recognition() == False:
        callback.after(100, voiceRec)

    messagebox.showinfo("Success", "Login Successful")


app = Tk()
w = 500
h = 500
app.geometry('%dx%d+0+0' % (w,h))
messagebox.showinfo("Info", "Welcome to JTech")

user_Label = Label(app, text="Welcome To JTech", font= "Arial 40")
user_Label.pack()


btn1 = Button(app, text = "Voice Recognition", command = voiceRec)
btn1.pack()

btn2 = Button(app, text = "Facial Recognition")
btn2.pack()

app.mainloop()
