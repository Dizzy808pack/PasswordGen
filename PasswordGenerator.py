from tkinter import *
import random
import string

#Functions
def GenPasswd():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return random_string

#generateButton
def GenClick(): 
    CopyAlert()
    passString = GenPasswd()
    password_string.set(passString)
    ClipboarbFunc()


#CopyButton
def CopyPasswdClick():
        if (password_string.get() != ""):
            
            CopyAlert()
            ClipboarbFunc()

#adds password to clipboard
def ClipboarbFunc():
     window.clipboard_clear()
     window.clipboard_append(password_string.get())

#Copy Success Alert
def CopyAlert():
    alert_label = Label(bottom_frame, text= 'Copied to clipboard')
    alert_label.pack()
    alert_label.after(3500, alert_label.destroy)

#Create Window
fastPass = 0
window = Tk()
window.title('Password Generator v0.2')
window.geometry('300x110')
window.resizable(False, False)
#Intialize Variables
password_string = StringVar()

#Objects Area
input_frame = Frame(master = window, pady= 10)
generateButton = Button(master = input_frame, text='Generate')
password_label = Label(master=input_frame, textvariable= password_string, font=('Calibri 20'))
copyButton = Button(master = input_frame, text='🗍', font=('Calibri', 15, 'bold'), command=CopyPasswdClick)

generateButton.config(command=GenClick, font=('Calibri', 15, 'bold'))
bottom_frame = Frame(window, relief='raised')

#Packing Everything
generateButton.pack(side='left', padx =10)
password_label.pack(side = 'left')
copyButton.pack(side = 'right')

input_frame.pack(pady = 10)
bottom_frame.pack(anchor=CENTER)
#Run
window.mainloop()