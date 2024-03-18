from tkinter import *
from tkinter import font
# import mysql.connector
# from tabulate import tabulate

# make a connection

# con = mysql.connector.connect(host="localhost",user="root",password="",database="practice")
# cur = con.cursor()

# object of tkinter
root = Tk()
root.title("login system")
root.geometry("700x500")

class login_system:
    
     def clear_all(s):
          for item in root.winfo_children():
               item.destroy()

     def clear(s):
          s.r_email_v = s.r_email_v.delete(0,END)
          s.r_name_v = s.r_name_v.delete(0,END)
          s.r_password_v = s.r_password_v.delete(0,END)

     def login_page(s):

          global email_v

          root.config(pady=50)
          s.login_frame = Frame(root,relief="groove",borderwidth=2)
          s.login_frame.pack()

          login_lable = Label(s.login_frame,text="Login",font=("Poppiens","25"),foreground="#CA18C7")
          login_lable.grid(row=0,column=0,columnspan=2)

          email_l = Label(s.login_frame,text="email",font=("Poppiens","10"))
          email_l.grid(row=2,column=0,padx=10,pady=10)

          password_l = Label(s.login_frame,text="password",font=("Poppiens","10"))
          password_l.grid(row=3,column=0,padx=10,pady=5)

          s.email_v = Entry(s.login_frame)
          s.email_v.grid(row=2,column=1,padx=10,pady=5)

          s.password_v = Entry(s.login_frame)
          s.password_v.grid(row=3,column=1,padx=10,pady=5)

          login_btn = Button(s.login_frame,text="login",foreground="white",bg="#CA18C7",width=15,command=lambda:[obj.login_db()])
          login_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=10)

          register_btn = Button(s.login_frame,text="register a new membership",borderwidth=0,foreground="#CA18C7",command=lambda:[obj.clear_all(),obj.register(1)])
          register_btn.grid(row=5,column=1,padx=5,pady=5)

          print()

     def register(s,v):

          s.register_frame = Frame(root,relief="groove",borderwidth=2)
          s.register_frame.pack()
          
          s.login_lable = Label(s.register_frame,text="Register",font=("Poppiens","25"),foreground="#CA18C7")
          s.login_lable.grid(row=0,column=0,columnspan=2)

          s.r_name_l = Label(s.register_frame,text="name",font=("Poppiens","10"))
          s.r_name_l.grid(row=1,column=0,padx=10,pady=10)
          
          s.r_email_l = Label(s.register_frame,text="email",font=("Poppiens","10"))
          s.r_email_l.grid(row=2,column=0,padx=10,pady=10)

          s.r_password_l = Label(s.register_frame,text="password",font=("Poppiens","10"))
          s.r_password_l.grid(row=3,column=0,padx=10,pady=5)

          s.r_name_v = Entry(s.register_frame)
          s.r_name_v.grid(row=1,column=1,padx=10,pady=5)

          s.r_email_v = Entry(s.register_frame)
          s.r_email_v.grid(row=2,column=1,padx=10,pady=5)

          s.r_password_v = Entry(s.register_frame)
          s.r_password_v.grid(row=3,column=1,padx=10,pady=5)

          if v == 1:
               s.register_btn = Button(s.register_frame,text="register",foreground="white",bg="#CA18C7",width=15,command=lambda:[obj.register_db(),obj.clear()])
               s.register_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=10)
          else:
               s.register_btn = Button(s.register_frame,text="update",foreground="white",bg="#CA18C7",width=15,command=lambda:[obj.update_db(),obj.clear_all(),obj.home_page()])
               s.register_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=10)

          if v == 1:
               s.login_btn = Button(s.register_frame,text="i have already registerd",borderwidth=0,foreground="#CA18C7",command=lambda:[obj.clear_all(),obj.login_page()])
               s.login_btn.grid(row=5,column=1,padx=5,pady=5)

          print()


     # data base functions
     def login_db(s):
          email = s.email_v.get()
          password = s.password_v.get()

          sql = "select * from admin where email = %s and password = %s"
          cur.execute(sql,(email,password))
          id = cur.fetchone()
          print(id)

          if id == None:
               error_mes = Label(s.login_frame,text="invalid email or password",foreground="red")
               error_mes.grid(row=1,column=0,columnspan=2)
          else:
               obj.clear_all()
               obj.home_page()

     def register_db(s):

          name = s.r_name_v.get()
          email = s.r_email_v.get()
          password = s.r_password_v.get()

          sql = "insert into admin(name,email,password) values (%s,%s,%s)"
          cur.execute(sql,(name,email,password))
          con.commit()

          print(name)

     def home_page(s):
          main_frame = Frame(root)
          main_frame.pack()

          lab = Label(main_frame,text="ID",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=0)

          lab = Label(main_frame,text="NAME",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=1)

          lab = Label(main_frame,text="EMAIL",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=2)

          lab = Label(main_frame,text="PASSWORD",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=3)

          lab = Label(main_frame,text="update",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=4)

          lab = Label(main_frame,text="delete",relief="groove",borderwidth=3,width=15)
          lab.grid(row=0,column=5)

          sql = "select * from admin"
          cur.execute(sql)
          rows = cur.fetchall()
          i=1
          for row in rows:
               j=0
               for data in row:
                    lab = Label(main_frame,text=data,relief="groove",borderwidth=3,width=15)
                    lab.grid(row=i,column=j)
                    j+=1
               update_btn = Button(main_frame,text="update",bg="green",foreground="white",width=15,command=lambda temp_id = row[0] :[obj.clear_all(),obj.register(2),obj.old_fetch_data(temp_id)])
               update_btn.grid(row=i,column=j)
               del_btn = Button(main_frame,text="delete",bg="red",foreground="white",width=15,command=lambda del_id= row[0]:[obj.delete_db(del_id),obj.clear_all(),obj.home_page()])
               del_btn.grid(row=i,column=j+1)
               i+=1

     def old_fetch_data(s,temp_id):

          s.update_id = temp_id
          sql = "select * from admin where id = %s"
          cur.execute(sql,(temp_id,))
          data = cur.fetchone()
          con.commit()

          s.r_name_v.insert(0,data[1])
          s.r_email_v.insert(0,data[2])
          s.r_password_v.insert(0,data[3])

     def update_db(s):

          name = s.r_name_v.get()
          email = s.r_email_v.get()
          password = s.r_password_v.get()
          print(name)
          print(email)
          print(password)
          sql = "update admin set name = %s ,email = %s ,password = %s where id = %s"
          cur.execute(sql,(name,email,password,s.update_id))
          con.commit()
     
     def delete_db(s,del_id):

          sql = "delete from admin where id = %s"
          cur.execute(sql,(del_id,))
          con.commit()
          print()

obj = login_system()
obj.login_page()


root.mainloop()


