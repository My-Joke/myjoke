
from tkinter import *  
from datetime import datetime
from tkinter import messagebox


i=0
j=0

class MyClass:

    def __init__(self, name):
        self.name=name
   
    def err(self):
        attempt.name='ERROR'
        return attempt.format()

    def debug(self):
        attempt.name='DEBUG'
        return attempt.format()

    def trace(self):
        attempt.name="TRACE"
        return attempt.format()

    def format(self):
        current_datetime = datetime.now()
        print (f"that's {attempt.name}.{current_datetime} priority:{attempt.name} "+ '\n')
        return (f"that's {attempt.name}.{current_datetime} priority:{attempt.name}"+ '\n')

attempt=MyClass("here will be name")        
    
def write_File():
    global i, inp
    i+=1
    z=str(message.get())
    if z=="" or z==" ":
        z='press-proof'
    inp=z
def write_File2():
    global j, inp2
    j+=1
    x=str(message2.get())
    if x=="" or x==" ":
        x='csv'
    inp2=x
def file(level,nama="press-proof",rest="csv"):
    if i>0:
        nama = (inp)
    if j>0:
        rest = (inp2)
    file=open(f"{nama}.{rest}", mode="a",newline="")
    file.write(level + '\n')
    file.close()

 
def clicked():       
    file(attempt.err())
def clicked2(): 
    file(attempt.debug())
def clicked3():  
    file(attempt.trace())
        
window = Tk()  
window.title("Создание логгера")  
window.geometry('500x200')  
lbl = Label(window, text="Выберите поиск :" ,font=("Arial Bold", 20)).grid(column=0, row=0)

message = StringVar()
the_input = Entry(textvariable=message).grid(row=5, column=0, padx=5, pady=5)
button_Write = Button(window, text = "Изменить имя файла:", command = write_File).grid(row=6, column=0, padx=5, pady=5)

message2= StringVar()
the_input2 = Entry(textvariable=message2).grid(row=8, column=0, padx=5, pady=5)
button_Write2 = Button(window, text = "Изменить формат файла:", command = write_File2).grid(row=9, column=0, padx=5, pady=5)

btn = Button(window, text="Error", command=clicked, height = 2, width = 10).grid(column=1, row=0, padx=5, pady=5)   
btn2 = Button(window, text="Debug", command=clicked2, height = 2, width = 10).grid(column=2, row=0, padx=5, pady=5) 
btn3 = Button(window, text="Trace", command=clicked3, height = 2, width = 10).grid(column=4, row=0, padx=5, pady=5) 
window.mainloop()


