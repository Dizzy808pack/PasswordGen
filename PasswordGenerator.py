from tkinter import *
import random
import string

#Functions
def GenPasswd():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return random_string

def click(): 
    passString = GenPasswd()
    password_string.set(passString)
    window.clipboard_append(passString) #adds password to clipboard

#Create Window
fastPass = 0
window = Tk()
window.title('Password Generator v0.1')
window.geometry('300x110')
window.resizable(False, False)
#Intialize Variables
password_string = StringVar()

#Objects Area
input_frame = Frame(master = window, pady= 10)
button = Button(master = input_frame, text='Generate')
password_label = Label(master=input_frame, textvariable= password_string, font=('Calibri 20'))

button.config(command=click, font=('Calibri', 15, 'bold'))

#Packing Everything
button.pack(side='left', padx =10)
password_label.pack(side = 'left')


input_frame.pack(pady = 10)

#Run
window.mainloop()