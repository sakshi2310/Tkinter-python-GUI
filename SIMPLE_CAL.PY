from tkinter import *;

# object of tkinter
t = Tk()
t.title("simple calc")
t.geometry("500x300")

# function start 

def clickbtn(n):
     c = str(n)
     if n == 1:
       sum =str(int(val1.get())+int(val2.get()))
       ans1.config(text=sum)
     elif n == 2:
         sub = str(int(val1.get())-int(val2.get()))
         ans1.config(text=sub)
     elif n == 3:
         mul = str(int(val1.get())*int(val2.get()))
         ans1.config(text=mul)
     elif n == 4:
         div = str(int(val1.get())/int(val2.get()))
         ans1.config(text=div)

# function end

# ENTRY BOX
v1 = Label(t,text="value 1 = ")
v1.grid(row=0)
v2 = Label(t,text="value 2 = ")
v2.grid(row=1)

val1 = Entry()
val1.grid(row=0,column=1)

val2 = Entry()
val2.grid(row=1,column=1)

# ANS VALUE
ans1 = Label(t,text="0")
ans1.grid(row=2)

# ans = Entry(state=DISABLED)
# ans.grid(row=2,column=1)

# BUTTON 

sum = Button(t,text="+",command=lambda:clickbtn(1),width=3,height=1)
sum.grid(row=0,column=3)

sub = Button(t,text="-",command=lambda:clickbtn(2),width=3,height=1)
sub.grid(row=0,column=4)

sub = Button(t,text="*",command=lambda:clickbtn(3),width=3,height=1)
sub.grid(row=1,column=3)

sub = Button(t,text="/",command=lambda:clickbtn(4),width=3,height=1)
sub.grid(row=1,column=4)


t.mainloop()