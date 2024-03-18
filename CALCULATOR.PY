# IMPORT LIBARY 
from tkinter import *

# OBJECT OF TKINTER

root = Tk()
root.title("calculator")
root.geometry("310x340")

# function 

def btn_click(n):
     
     global first_value
     if input_frame.cget("text") == "0":
        first_value = str(n)
     else:
          first_value = input_frame.cget("text") + str(n)
     input_frame.config(text=first_value)

     

     print(n)
def sign_click(n):
     
     if str(n) == str(10):
          sum = int(input_frame.cget("text")) + int(n)
          print("hy")
     input_frame.config(text=sum)

# create a frame 
frame =Frame(root)
frame.pack()

input_frame = Label(frame,width=37,height=4,text="0",highlightbackground="black",highlightthickness=2)
input_frame.grid(row=0,column=0,ipadx=22.5)

# btn frame 
btn_frame = Frame(root,width=300,height=350,bg="gray")
btn_frame.pack()

# first row

modual_btn = Button(btn_frame,text="%",width=10,height=3,fg="black",bd=0,cursor="hand2")
modual_btn.grid(row=0,column=0,padx=1,pady=1)

ce_btn = Button(btn_frame,text="CE",width=10,height=3,fg="black",bd=0,cursor="hand2")
ce_btn.grid(row=0,column=1,padx=1,pady=1)

clear_btn= Button(btn_frame,text="CE",width=10,height=3,fg="black",bd=0,cursor="hand2")
clear_btn.grid(row=0,column=2,padx=1,pady=1)

num_clear = Button(btn_frame,text="<-",width=10,height=3,fg="black",bd=0,cursor="hand2")
num_clear.grid(row=0,column=3,padx=1,pady=1)


# 2 row

seven_btn = Button(btn_frame,text="7",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(7))
seven_btn.grid(row=1,column=0,padx=1,pady=1)

eight_btn = Button(btn_frame,text="8",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(8))
eight_btn.grid(row=1,column=1,padx=1,pady=1)

nine_btn = Button(btn_frame,text="9",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(9))
nine_btn.grid(row=1,column=2,padx=1,pady=1)

mul_btn = Button(btn_frame,text="x",width=10,height=3,fg="black",bd=0,cursor="hand2")
mul_btn.grid(row=1,column=3,padx=1,pady=1)


# 3 row

four_btn = Button(btn_frame,text="4",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(4))
four_btn.grid(row=2,column=0,padx=1,pady=1)

five_btn = Button(btn_frame,text="5",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(5))
five_btn.grid(row=2,column=1,padx=1,pady=1)

six_btn = Button(btn_frame,text="6",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(6))
six_btn.grid(row=2,column=2,padx=1,pady=1)

sub = Button(btn_frame,text="-",width=10,height=3,fg="black",bd=0,cursor="hand2")
sub.grid(row=2,column=3,padx=1,pady=1)

# 4 row

one_btn = Button(btn_frame,text="1",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(1))
one_btn.grid(row=3,column=0,padx=1,pady=1)

two_btn = Button(btn_frame,text="2",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(2))
two_btn.grid(row=3,column=1,padx=1,pady=1)

three_btn = Button(btn_frame,text="3",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(3))
three_btn.grid(row=3,column=2,padx=1,pady=1)

sum = Button(btn_frame,text="+",width=10,height=3,fg="black",bd=0,cursor="hand2" , command=lambda:sign_click("10"))
sum.grid(row=3,column=3,padx=1,pady=1)

# 5 row

divide_btn = Button(btn_frame,text="/",width=10,height=3,fg="black",bd=0,cursor="hand2")
divide_btn.grid(row=4,column=0,padx=1,pady=1)

zero_btn = Button(btn_frame,text="0",width=10,height=3,fg="black",bd=0,cursor="hand2",command=lambda:btn_click(0))
zero_btn.grid(row=4,column=1,padx=1,pady=1)

point_btn = Button(btn_frame,text=".",width=10,height=3,fg="black",bd=0,cursor="hand2")
point_btn.grid(row=4,column=2,padx=1,pady=1)

equal = Button(btn_frame,text="=",width=10,height=3,fg="black",bd=0,cursor="hand2")
equal.grid(row=4,column=3,padx=1,pady=1)


root.mainloop()