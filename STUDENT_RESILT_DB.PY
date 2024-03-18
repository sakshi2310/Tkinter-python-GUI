# IMPORT LIBARY
from tkinter import *
import mysql.connector
from tabulate import tabulate

# objext of tkinter
t = Tk()

t.title("studnet result")
t.geometry("400x300")


# function
sub1 = ''
sub2 = ''
sub3 = ''
sub4 = ''
sub5 = ''
total = 0
def btn_click():
    con = mysql.connector.connect(host="localhost",user = "root",database="result")
    cur = con.cursor()
    name = n.get()
    sub1 = s1.get()
    sub2 = s2.get()
    sub3 = s3.get()
    sub4 = s4.get()
    sub5 = s5.get()  

    total = int(sub1) + int(sub2) + int(sub3) +int(sub4) +int(sub5)
    minimum = min(int(sub1),int(sub2),int(sub3),int(sub4),int(sub5))
    maximum = max(int(sub1),int(sub2),int(sub3),int(sub4),int(sub5))
    
    if minimum > 33:
        per = total / 5 
    else:
        per = 0
    
    if per>33:
        result = "pass"
    else:
        result = "fail"

    if per>90:
        grade = "A1"
    elif per>80:
        grade = "A2"
    elif per>70:
        grade = "B1"
    elif per>60:
        grade = "B2"
    elif per>50:
        grade = "C1"
    elif per>40:
        grade = "C2"
    elif per>33:
        grade = "E1"
    else:
        grade = "F"

    sql = "insert into students (name,sub1,sub2,sub3,sub4,sub5,total,per,min,max,result,grade) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,(name,sub1,sub2,sub3,sub4,sub5,total,per,minimum,maximum,result,grade))
    con.commit()

    n.delete(0,END)
    s1.delete(0,END)
    s2.delete(0,END)
    s3.delete(0,END)
    s4.delete(0,END)
    s5.delete(0,END)

# frame 
frame = Frame(t,width=400,height=250,bd=0,highlightbackground="black",highlightthickness=1)
frame.pack()

# heading
heading = Label(frame,text="student result" ,width=400)
heading.pack(ipady=10)

# markas frame
mark_frame = Frame(t,width=400,height=20)
mark_frame.pack()

#  enter label of marks

name = Label(mark_frame,text="name:")
name.grid(row=0)

sub1 = Label(mark_frame,text="sub1:")
sub1.grid(row=1)

sub2 = Label(mark_frame,text="sub2:")
sub2.grid(row=2)

sub3 = Label(mark_frame,text="sub3:")
sub3.grid(row=3)

sub4 = Label(mark_frame,text="sub4:")
sub4.grid(row=4)

sub5 = Label(mark_frame,text="sub5:")
sub5.grid(row=5)

# enter entry of marks

n = Entry(mark_frame)
n.grid(row=0,column=1,padx=5,pady=10)

s1 = Entry(mark_frame)
s1.grid(row=1,column=1,padx=5,pady=10)

s2 = Entry(mark_frame)
s2.grid(row=2,column=1,padx=5,pady=10)

s3 = Entry(mark_frame)
s3.grid(row=3,column=1,padx=5,pady=10)

s4 = Entry(mark_frame)
s4.grid(row=4,column=1,padx=5,pady=10)

s5 = Entry(mark_frame)
s5.grid(row=5,column=1,padx=5,pady=10)


# submit btn
btn = Button(t,text="submit" ,command=lambda:btn_click())
btn.pack()





t.mainloop()