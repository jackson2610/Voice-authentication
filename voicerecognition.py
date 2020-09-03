from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from VoiceRecognition import voice_recognition

def voiceRec():
    loading.config(text = 'Voice Recognition Active.....')
    if voice_recognition() == False:
        voiceRec

    messagebox.showinfo("Success", "Login Successful")
    loading.config(text = 'Login Sucessful....')

app = Tk()

app.geometry('600x600')
messagebox.showinfo("Info", "Welcome to JTech")

user_Label = Label(app, text="Welcome To JTech", font= "Helvetica 40", fg = 'blue')
user_Label.pack(pady = 20)

vrImg = Image.open('/Users/Robert/Downloads/img_18524.png')
vrImg = vrImg.resize((60, 60), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(vrImg)

btn1 = Button(app, image = img, command = voiceRec, borderwidth = 0)
btn1.pack(pady = 20)

loading = Label(app, text ='')
loading.pack(pady = 20)

app.mainloop()
