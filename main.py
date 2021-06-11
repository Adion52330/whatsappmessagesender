from tkinter import *
import pywhatkit
from tkinter import messagebox

window = Tk()
window.title('Send the message')

def width():
    txt['width'] = int(txt['width']) + 1

def height():
    txt['height'] = int(txt['height']) + 1

def send():
    if num.get() == "+91" and txt.get(1.0, "end-1c") == "":
        messagebox.showinfo('Nothing', 'Please enter all the values')
    elif num.get() == '+91' or txt.get(1.0, 'end-1c') == "":
        messagebox.showinfo('Nothing', 'Please enter all the values')
    else:
        pywhatkit.sendwhatmsg_instantly(num.get(), txt.get(1.0, "end-1c"))

main_label = Label(window, text="Welcome to whatsapp message sending application!", font=('aharoni', 25))
main_label.grid(row=0, columnspan=7)

dum = Label(window, text="  ")
dum.grid(row=1, column=0)

txt = Text(window, font=('sans serif', 20), height=4, width=30, borderwidth=10, bg='lightyellow')
txt.grid(row=2, columnspan=7)

increase = Button(window, text="Increase width", font=('ink free', 15), borderwidth=5, bg='cyan', command=width)
increase.grid(row=3, column=1)
increase_height = Button(window, text="Increase height", font=('ink free', 15), borderwidth=5, bg='cyan', command=height)
increase_height.grid(row=3, column=5)

frame = Frame(window)
frame.grid(row=4, columnspan=5)

dum = Label(frame, text=" ")
dum.pack()

to = Label(frame, text='To:', font=('atroix', 20))
to.pack()

dum = Label(window, text="  ")
dum.grid(row=4, columnspan=7)

num = Entry(window, font=('aharoni', 20), borderwidth=5, bg='black', fg='#00ff00')
num.insert(0, '+91')
num.grid(row=5, column=0, columnspan=7)

dum = Label(window, text="  ")
dum.grid(row=6, columnspan=7)

sender = Button(window, text="Send The Message", font=('ink free', 20), borderwidth=10, bg='violet', fg='turquoise', command=send)
sender.grid(row=7, columnspan=7)

window.mainloop()