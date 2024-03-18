from tkinter import *

root = Tk()

root.title("student result")
root.geometry("400x400")

main_frame = Frame(root)
main_frame.pack()

heading_l = Label(main_frame,text="studnet result",font=("Poppins","20"))
heading_l.grid(row=0,column=0,columnspan=2)

s1 = Label(main_frame,text="subject 1")
s1.grid(row=1,column=0,padx=10,pady=10)

s2 = Label(main_frame,text="subject 2")
s2.grid(row=2,column=0,padx=10,pady=10)

s3 = Label(main_frame,text="subject 3")
s3.grid(row=3,column=0,padx=10,pady=10)

s4 = Label(main_frame,text="subject 4")
s4.grid(row=4,column=0,padx=10,pady=10)

s5 = Label(main_frame,text="subject 5")
s5.grid(row=5,column=0,padx=10,pady=10)

s1_v = Entry(main_frame)
s1_v.grid(row=1,column=1,padx=10,pady=10)

s2_v = Entry(main_frame)
s2_v.grid(row=2,column=1,padx=10,pady=10)

s3_v = Entry(main_frame)
s3_v.grid(row=3,column=1,padx=10,pady=10)

s4_v = Entry(main_frame)
s4_v.grid(row=4,column=1,padx=10,pady=10)

s5_v = Entry(main_frame)
s5_v.grid(row=5,column=1,padx=10,pady=10)

btn = Button(main_frame,text="submit",command=lambda:[view_result()])
btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10)

def clear():
    for item in main_frame.winfo_children():
        item.destroy()

def view_result():
    
    s1 = s1_v.get()
    s2 = s2_v.get()
    s3 = s3_v.get()
    s4 = s4_v.get()
    s5 = s5_v.get()
    clear()
    Label(main_frame,text="subject 1  = ").grid(row=1,column=0)
    Label(main_frame,text="subject 2  = ").grid(row=2,column=0)
    Label(main_frame,text="subject 3  = ").grid(row=3,column=0)
    Label(main_frame,text="subject 4  = ").grid(row=4,column=0)
    Label(main_frame,text="subject 5  = ").grid(row=5,column=0)

    Label(main_frame,text=s1).grid(row=1,column=1)
    Label(main_frame,text=s2).grid(row=2,column=1)
    Label(main_frame,text=s3).grid(row=3,column=1)
    Label(main_frame,text=s4).grid(row=4,column=1)
    Label(main_frame,text=s5).grid(row=5,column=1)

    total = int(s1)+int(s2)+int(s3)+int(s4)+int(s5)
    Label(main_frame,text="total  = ").grid(row=6,column=0)
    Label(main_frame,text=total).grid(row=6,column=1)
    
    minimum = min(int(s1),int(s2),int(s3),int(s4),int(s5))
    Label(main_frame,text="minimum = ").grid(row=8,column=0)
    Label(main_frame,text=minimum).grid(row=8,column=1)

    if minimum < 35:
        per = 0
    else:
        per = total / 5
    Label(main_frame,text="per  = ").grid(row=7,column=0)
    Label(main_frame,text=per).grid(row=7,column=1)

    maximum = max(int(s1),int(s2),int(s3),int(s4),int(s5))
    Label(main_frame,text="maximum = ").grid(row=9,column=0)
    Label(main_frame,text=maximum).grid(row=9,column=1)

    if minimum > 35:
        result = "pass"
    else:
        result = "fail"

    Label(main_frame,text="result = ").grid(row=10,column=0)
    Label(main_frame,text=result).grid(row=10,column=1)

    if per > 90:
        grade = "A1"
    elif per > 80:
        grade = "A2"
    elif per > 70:
        grade = "B1"
    elif per > 60:
        grade = "B2"
    elif per > 50:
        grade = "C1"
    elif per > 40:
        grade = "C2"
    elif per > 33:
        grade = "E1"
    else:
        grade = "F"

    Label(main_frame,text="grade = ").grid(row=11,column=0)
    Label(main_frame,text=grade).grid(row=11,column=1)


root.mainloop()
