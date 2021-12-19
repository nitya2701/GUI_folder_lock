#A GUI based dialog box for taking username password
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title('Login Screen')
window.geometry('400x150')

#creating a window(dialog box)
l1 = Label(window, text='Username:', font=(14))
l2 = Label(window, text='Password:', font=(14))
l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=1, column=0, padx=5, pady=5)

#creating variables to display in dialog box
username = StringVar()
password = StringVar()

#creating two textboxes for getting values entered
t1 = Entry(window, textvariable=username, font=(14))
t2 = Entry(window, textvariable=password, font=(14), show='*')
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)

#creating function for login
def login():
    if username.get()=='admin' and password.get()=='admin':
        messagebox.showinfo(title='Login Status', message='Link for final project')
    else:
        messagebox.showerror(title='Login error', message='Username/Password incorrect.')

def cancel():
    status = messagebox.askyesno(title='Question', message='Do you want to close the window?')
    if status==True:
        window.destroy()
    else:
        messagebox.showwarning(title='Warning message', message='Please try again!')


#placing two buttons
b1 = Button(window, command=login, text='Login', font=(14))
b2 = Button(window, command=cancel, text='Cancel', font=(14))
b1.grid(row=2, column=1, sticky=W)
b2.grid(row=2, column=1, sticky= E)


window.mainloop()