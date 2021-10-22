from tkinter import*
import datetime
import time
import pygame as pg
from pygame import mixer
import threading
from tkinter import messagebox

root=Tk()
root.title("Alarm Clock")
root.geometry("530x530")
alarmtime= StringVar()
msgi= StringVar()

head = Label(root,text="Alarm Clock",font=('comic sans',20))
head.grid(row=0,columnspan=3,pady=10)
mixer.init()

def ala():
     a= alarmtime.get()

     AlarmT =a
     CurrentTime = time.strftime("%H:%M")

     while AlarmT != CurrentTime:
         CurrentTime = time.strftime("%H:%M")
     if AlarmT==CurrentTime:
         mixer.music.load(r"C:\Users\hp\Downloads\tone.mp3")
         mixer.music.play()
         msg= messagebox.showinfo('Info',f'{msgi.get()}')
         
        
         if msg == 'ok':
             mixer.music.stop()
        
      

    

        
         


Clockimg = PhotoImage(file=r"C:\Users\hp\Desktop\al.png")
img = Label(root,image=Clockimg)
img.grid(rowspan=4,column=0)
inputt= Label(root,text="Input time",font=('comic sans',18))
inputt.grid(row=1,column=1)

altime= Entry(root,textvariable=alarmtime,font=('comic sans',18),width=6)
altime.grid(row=1,column=2)

msg= Label(root,text="Message",font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=2)

msginput = Entry(root,textvariable=msgi,font=('comic sans',18))
msginput.grid(row=3,column=1,columnspan=2)

submit = Button(root,text="SUBMIT",font=('comic sans',18),command=ala)
submit.grid(row=4,column=1,columnspan=2)



root.mainloop()




