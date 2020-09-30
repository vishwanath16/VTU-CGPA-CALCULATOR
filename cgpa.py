from tkinter import *
from tkinter import font
 
def cgpa():
    credit = [float(c1.get()), float(c2.get()), float(c3.get()), float(c4.get()), float(c5.get()), float(c6.get()), float(c7.get()), float(c8.get())]
    credit2 = [float(e1.get()), float(e2.get()), float(e3.get()), float(e4.get()), float(e5.get()), float(e6.get()), float(e7.get()), float(e8.get())]
    res = (sum(credit))/(sum(credit2))
    print(sum(credit), sum(credit2))
    myText.set(res)
 
root = Tk()
root.geometry("650x420")

myText=StringVar();
root.title("CGPA CALCULATOR")
Label(root, text = "Developed by VISHWANATH T S", fg = "RED", font=("Times", 20)).grid(row = 0, sticky='W')
Label(root, text = "Σ(CᵢXGⱼ)", fg = "Black", font=("Times", 20)).grid(row = 1, column = 0, padx=170, sticky='W')
Label(root, text = "Credits Earned", fg = "Black", font=("Times", 20)).grid(row = 1, column = 1, sticky='W')

first = Label(root, text = "First Sem:", fg = "Blue", font=("Times", 15)).grid(row = 3, sticky='W')
second = Label(root, text = "Second Sem:", fg = "Blue", font=("Times", 15)).grid(row = 4, sticky='W')
third = Label(root, text = "Third Sem:", fg = "Blue", font=("Times", 15)).grid(row = 5, sticky='W')
fourth = Label(root, text = "Fourth Sem:", fg = "Blue", font=("Times", 15)).grid(row = 6, sticky='W')
fifth = Label(root, text = "Fifth Sem:", fg = "Blue", font=("Times", 15)).grid(row = 7, sticky='W')
sixth = Label(root, text = "Sixth Sem:", fg = "Blue", font=("Times", 15)).grid(row = 8, sticky='W')
seventh = Label(root, text = "Seventh Sem:", fg = "Blue", font=("Times", 15)).grid(row = 9, sticky='W')
eighth = Label(root, text = "Eighth Sem:", fg = "Blue", font=("Times", 15)).grid(row = 10, sticky='W')
Label(root, text="Result:", font=('None', 20), fg = "green").grid(row=11, sticky=W)
result=Label(root, text="", textvariable=myText, font=('None', 20, 'underline')).grid(row=12, sticky=W)
 
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)
 
e1.grid(row=3, column=1)
e2.grid(row=4, column=1)
e3.grid(row=5, column=1)
e4.grid(row=6, column=1)
e5.grid(row=7, column=1)
e6.grid(row=8, column=1)
e7.grid(row=9, column=1)
e8.grid(row=10, column=1)

c1 = Entry(root)
c2 = Entry(root)
c3 = Entry(root)
c4 = Entry(root)
c5 = Entry(root)
c6 = Entry(root)
c7 = Entry(root)
c8 = Entry(root)
 
c1.grid(row=3, column=0)
c2.grid(row=4, column=0)
c3.grid(row=5, column=0)
c4.grid(row=6, column=0)
c5.grid(row=7, column=0)
c6.grid(row=8, column=0)
c7.grid(row=9, column=0)
c8.grid(row=10, column=0)

 
b = Button(root, text="Calculate", command=cgpa, font=('None', 15), bg="cyan")
b.grid(row=13, column=0,columnspan=2, rowspan=2)
 
 
mainloop()