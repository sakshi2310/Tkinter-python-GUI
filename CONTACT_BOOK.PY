# IMPORT LIBARY
from tkinter import *
from tkinter import font

# data base connection 
import mysql.connector
con  = mysql.connector.connect(host = "localhost", user = "root" , database = "contact_book")
cur = con.cursor(buffered=True)

# object of tkinter 
t = Tk()
t.title("contact book")
t.geometry("500x400")


# ************************* start frames ********************************
     # heading frame
font_underline = font.Font(underline=True)
heading = Label(t,text="contact book",font=font_underline,pady=10)
heading.pack()

     #main area frame

main_area = Frame(t,width=800,relief=GROOVE,borderwidth=2)
main_area.pack()
# *********************************** end frame **********************************

# ********************************** start function ******************************

# clear the past window values
def clear_all():
    for item in main_area.winfo_children():
        item.destroy()

# def resize():
#      w = 401
#      h = 401
#      t.geometry(f"{w}x{h}")
# sign in values with using tkinter 
def sign_in_account():
    global name_value
    global email_value
    global password_value
    name_lable = Label(main_area,text="name :")
    name_lable.grid(row=0,column=0)

    email_lable = Label(main_area,text="email:")
    email_lable.grid(row=1,column=0)

    password_label = Label(main_area,text="password:")
    password_label.grid(row=2,column=0)

    name_value = Entry(main_area)
    name_value.grid(row=0,column=1)

    email_value = Entry(main_area)
    email_value.grid(row=1,column=1)

    password_value = Entry(main_area)
    password_value.grid(row=2,column=1)
    
    sign_up_save = Button(main_area,text="register",width=10,height=1,command=lambda:[sign_values_db(),clear_text()])
    sign_up_save.grid(row=3,column=1,columnspan=2,pady=(10,2)) 

    back_home = Button(main_area,text="login",command=lambda:[clear_all(),home_page()])
    back_home.grid(row=4,column=1,columnspan=2,pady=2)
    
# clear the value of entery file in register time
def clear_text():
     name_value.delete(0,END)
     email_value.delete(0,END)
     password_value.delete(0,END)
     
# clear login page value 
def clear_login_text():
     email_login_value.delete(0,END)
     pw_login_value.delete(0,END)

    
# home page for login
def home_page():
     global email_login_value
     global pw_login_value

     email_login_lable = Label(main_area,text="email:")
     email_login_lable.grid(row=1,column=0,pady=10,padx=20)

     pw_login_lable = Label(main_area,text="password:")
     pw_login_lable.grid(row=2,column=0)

     email_login_value = Entry(main_area)
     email_login_value.grid(row=1,column=1)

     pw_login_value = Entry(main_area)
     pw_login_value.grid(row=2,column=1)

     sign_up_btn = Button(main_area,width=10,height=1,text="sign up",bg="#99A3A4",command=lambda:[clear_all(),sign_in_account()])
     sign_up_btn.grid(row=3,column=0,pady=5,padx=5)
     
     login_btn = Button(main_area,text="login",width=10,height=1,bg="#99A3A4", command=lambda:[login_db()])
     login_btn.grid(row=3,column=1)
     
        
# show all options
def options(A):
     
     choise_fun = A
     if choise_fun == 1:
          Label(main_area,text="you have successfully login your account",foreground="green").grid(row=0,column=1)
     elif choise_fun == 2:
          Label(main_area,text="you successfully register a data",foreground="green").grid(row=0,column=1)
     elif choise_fun == 3:
          Label(main_area,text="you successfully delete contact",foreground="green").grid(row=0,column=1)
     elif choise_fun == 4:
         Label(main_area,text="you successfully update your contact",foreground="green").grid(row=0,column=1)
     elif choise_fun == 5:
          Label(main_area,text="you successfully change password",foreground="green").grid(row=0,column=1)


     add_cont_btn = Button(main_area,text="ADD CONTACT", width=20,height=1,command=lambda:[clear_all(),add_contact()])
     add_cont_btn.grid(row=1,column=1,pady=5)

     del_cont_btn = Button(main_area,text="DELETE CONTACT",width=20,height=1,command=lambda:[clear_all(),delete_contact()])
     del_cont_btn.grid(row=2,column=1,pady=5)

     update_cont_btn = Button(main_area,text="UPDATE CONTACT",width=20,height=1,command=lambda:[clear_all(),get_update_id()])
     update_cont_btn.grid(row=3,column=1,pady=5)

     change_password_btn = Button(main_area,text="CHANGE PASSWORD",width=20,height=1,command=lambda:[clear_all(),show_old_password()])
     change_password_btn.grid(row=4,column=1,pady=5)

# add the contact 

def add_contact():
    global a_name_value
    global a_email_value
    global a_contact_value
    
    a_name_lable = Label(main_area,text="name")
    a_name_lable.grid(row=1,column=0)
    
    a_email_lable = Label(main_area,text="email")
    a_email_lable.grid(row=2,column=0)
    
    a_contact_lable = Label(main_area,text="contact")
    a_contact_lable.grid(row=3,column=0)
    
    a_name_value = Entry(main_area)
    a_name_value.grid(row=1,column=1)
    
    a_email_value = Entry(main_area)
    a_email_value.grid(row=2,column=1)
    
    a_contact_value = Entry(main_area)
    a_contact_value.grid(row=3,column=1)
    
    contact_add_btn = Button(main_area,text="register",height=1,command=lambda:[add_contact_db(),clear_all(),options(2)])
    contact_add_btn.grid(row=4,column=0,columnspan=2,pady=5)
    
    back_btn = Button(main_area,text="back button",command=lambda:[clear_all(),options(0)])
    back_btn.grid(row=5,column=0,columnspan=2)
    
    Label(main_area,text="").grid(row=6,column=0,columnspan=2)

def delete_contact():
    
    global del_id
    Label(main_area,text="enter the id which you ant to delete..").grid(row=1,column=0,columnspan=2)
    
    del_id = Entry(main_area)
    del_id.grid(row=2,column=0,columnspan=2)
    
    del_contact_btn = Button(main_area,text="DELETE",command=lambda:[del_contact_db(),clear_all(),options(3)])
    del_contact_btn.grid(row=3,column=0,columnspan=2,pady=5)
    
    back_btn = Button(main_area,text="back button",command=lambda:[clear_all(),options(0)])
    back_btn.grid(row=5,column=0,columnspan=2)
    
    Label(main_area,text="").grid(row=6,column=0,columnspan=2)


def get_update_id():
    global update_id
    update_mes = Label(main_area,text="enter the id which you want to update")
    update_mes.grid(row=1,column=0,columnspan=2)
    
    update_id = Entry(main_area)
    update_id.grid(row=2,column=0,columnspan=2)
    
    update_btn = Button(main_area,text="submit",command=lambda:[update_contact(),set_update_value()])
    update_btn.grid(row=3,column=0,columnspan=2)
    
    back_btn = Button(main_area,text="back button",command=lambda:[clear_all(),options(0)])
    back_btn.grid(row=4,column=0,columnspan=2)
    
    Label(main_area,text="").grid(row=5,column=0,columnspan=2)

def update_contact():
     global u_name_lable
     global u_name_value
     global u_email_value
     global u_contact_value
     
     u_name_lable = Label(main_area,text="name")
     u_name_lable.grid(row=6,column=0,pady=(10,0))
     
     u_email_lable = Label(main_area,text="email")
     u_email_lable.grid(row=7,column=0)
     
     u_contact_lable = Label(main_area,text="contact")
     u_contact_lable.grid(row=8,column=0)
     
     u_name_value = Entry(main_area,width=30)
     u_name_value.grid(row=6,column=1,pady=(10,0))
     
     u_email_value = Entry(main_area,width=30)
     u_email_value.grid(row=7,column=1)
     
     u_contact_value = Entry(main_area,width=30)
     u_contact_value.grid(row=8,column=1)
     
     update_btn = Button(main_area,text="UPDATE",height=1,command=lambda:[update_contact_db(),clear_all(),options(4)])
     update_btn.grid(row=9,column=0,columnspan=2,pady=5)
     
     Label(main_area,text="").grid(row=11,column=0,columnspan=2)
     
def set_update_value():
     update_cid = update_id.get()
     print(update_cid)
     
     sql = "select * from contacts where id = %s"
     cur.execute(sql,(update_cid,))
     data = cur.fetchone()
     print(data)
     con.commit()
     u_name_value.insert(0,data[1])
     u_email_value.insert(0,data[2])
     u_contact_value.insert(0,data[3])
     
     Label(main_area,text="").grid(row=11,column=0,columnspan=2)
        
def show_old_password():
     global old_password_entry
     global old_pw_btn
     global old_pw
     
     old_pw = Label(main_area,text="enter the old password")
     old_pw.grid(row=1,column=0,columnspan=2)
     
     old_password_entry = Entry(main_area)
     old_password_entry.grid(row=2,column=0,columnspan=2)
     
     old_pw_btn = Button(main_area,text="submit",command=lambda:[view_new_pass(),new_pw_page()])
     old_pw_btn.grid(row=3,column=0,columnspan=2)
     
     Label(main_area,text="").grid(row=5,column=0,columnspan=2)
     
def view_new_pass():
     # if old_pw_btn['status'] == NORMAL:
     #      old_pw_btn['status'] = DISABLED
     old_password = old_password_entry.get()
     sql = "select * from admin where password =%s"
     cur.execute(sql,(old_password,))
     pass_data = cur.fetchone()
     print(pass_data)
     
     if pass_data == None:
          error_pass = Label(main_area,text="invalid password",foreground="red")
          error_pass.grid(row=0,column=0)

def new_pw_page():
          global new_pw_value
          global conform_pw_value
          new_pw_l = Label(main_area,text="enter the new password")
          new_pw_l.grid(row=5,column=0)

          conform_pw_l = Label(main_area,text="enter the confim password")
          conform_pw_l.grid(row=6,column=0)

          new_pw_value = Entry(main_area)
          new_pw_value.grid(row=5,column=1)
          
          conform_pw_value = Entry(main_area)
          conform_pw_value.grid(row=6,column=1)
               
          change_password_btn = Button(main_area,text="change password" ,width=15,command=lambda:[new_pw_db(),options(5)])
          change_password_btn.grid(row=7,column=0,columnspan=2,pady=10)

     
# ********************************** end function ********************************

# ********************************* start  data base function ****************************

def sign_values_db():
    name = name_value.get()
    email  = email_value.get()
    password = password_value.get()
    sql = "insert into admin (name,email,password) values(%s,%s,%s)"
    cur.execute(sql,(name,email,password))
    con.commit()


def login_db():
     global id
     email_login = email_login_value.get()
     pw_login = pw_login_value.get()
     
     sql = "select * from admin where email = %s and password = %s"
     cur.execute(sql,(email_login,pw_login))
     id = cur.fetchone()
     if id == None:
        error_mes = Label(main_area,text="invalid email or password",foreground="red")
        error_mes.grid(row=0,column=0,columnspan=2)
        
        print("invalid password")
        clear_login_text()
        Label(main_area,text="").grid(row=11,column=0,columnspan=2)
     else:
          clear_all()
          options(1)
          print("login successfully")
     con.commit()
     Label(main_area,text="").grid(row=11,column=0,columnspan=2)
    
def add_contact_db():
    name = a_name_value.get()
    email = a_email_value.get()
    contact = a_contact_value.get()
    contact_id = id[0]
    
    sql = "insert into contacts (name,email,contact,contact_id) values (%s,%s,%s,%s)"
    cur.execute(sql, (name,email,contact,contact_id))
    con.commit()

def del_contact_db():
    delete_id = del_id.get()
    sql = "delete from contacts where id=%s"
    cur.execute(sql,(delete_id,))
    con.commit()
    
    
def update_contact_db():
    name = u_name_value.get()
    email = u_email_value.get()
    contact = u_contact_value.get()
    update_cid = update_id.get()
    
    sql = "update contacts set name = %s , email = %s, contact = %s where id =%s"
    cur.execute(sql ,(name,email,contact,update_cid))
    con.commit()
    
def new_pw_db():

     new_pw = new_pw_value.get()
     print(new_pw)
     conform_pw = conform_pw_value.get()
     change_id = id[0]
     print(change_id)
     sql = "update admin set password = %s where id = %s"
     cur.execute(sql,(new_pw,change_id,))
     con.commit()



     

     print("hy")
# ********************************* end data base function *******************************

# *********************************** start first page ****************************
home_page()
# t.after(2000,lambda:resize())
# *********************************** end first page ******************************

t.mainloop()