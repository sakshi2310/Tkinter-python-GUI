# import libray

from tkinter import *
from tkinter import font

# object
root = Tk()

# 
class bank_system():
     
     def __init__(s):

          root.title("the bank management system")
          root.geometry("300x300")

          # to give the title of window
          font_underline = font.Font(underline=True)
          heading = Label(root,text="bank management system",font=font_underline,padx=10,pady=20)
          heading.pack()

     # to clear the main window 
     def clear_all(s):
          for item in s.main_area.winfo_children():
               item.destroy()


     # create a main area frame
     def home_page(s):
          s.main_area = Frame(root,width=500,height=500,relief=GROOVE,borderwidth=2,bg="#85C1E9")
          s.main_area.pack()

          home_page_title = Label(s.main_area,text="login page",font=("Bahnschrift" , "10"),bg="#85C1E9")
          home_page_title.grid(row=1,column=0,columnspan=2)

          Label(s.main_area,text="email",bg="#85C1E9").grid(row=2,column=0,padx=(15,5))
          Label(s.main_area,text="password",bg="#85C1E9").grid(row=3,column=0,padx=(15,5))

          email_v = Entry(s.main_area)
          email_v.grid(row=2,column=1,pady=5,padx=(0,15))

          password_v = Entry(s.main_area)
          password_v.grid(row=3,column=1,pady=5,padx=(0,15))

          login_btn = Button(s.main_area,text="login")
          login_btn.grid(row=4,column=0,columnspan=2,padx=15,pady=5)

          sign_btn = Button(s.main_area,text="sign up user ",border=None,bg="#85C1E9",borderwidth=0,activebackground="#85C1E9",command=lambda:[bank.clear_all(),bank.sign_up()])
          sign_btn.grid(row=5,column=1)

     # sign up user
     def  sign_up(s):
          Label(s.main_area,text="account type").grid(row=1,column=0)
          s.account_type = Entry(s.main_area)
          s.account_type.grid(row=1,column=1)

          type =s.account_type.get()
          print(type)
          print()

# if __name__ == "__main__":
bank =  bank_system()
bank.home_page()
root.mainloop()


