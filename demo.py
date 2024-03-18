from tkinter import *
from tkinter import font
import mysql.connector

class page:
    reg = log = em = pss = None

    def __init__(s,main,log,reg,sys):
        s.main = main
        s.reg = reg
        s.log = log
        s.sys = sys

        l2 = Label(s.main, text="Email")
        l2.grid(row=2, column=0)
        s.em = Entry(s.main)
        s.em.grid(row=2, column=1)

        l2 = Label(s.main, text="Password")
        l2.grid(row=3, column=0)
        s.pss = Entry(s.main)
        s.pss.grid(row=3, column=1)

    def log_p(s,un,l1):
        un.destroy()
        l1.destroy()
        s.log.config(text='Login',bg='green',command=lambda:s.login(s.em.get(),s.pss.get()))
        s.reg.config(text='want to register',bg='black',command=s.reg_p)

    def reg_p(s):

        l1 = Label(s.main,text='Username')
        l1.grid(row=1,column=0)
        un = Entry(s.main)
        un.grid(row=1,column=1)
        s.log.config(text='want to login',bg='black',command=lambda:s.log_p(l1,un))
        s.reg.config(text='Register',bg='green',command=lambda:s.register(s.em.get(),un.get(),s.pss.get()))

    def login(s,em,pss):
        print('logged !')
        print(em)
        print(pss)
        s.sys.login(em,pss)

    def register(s,em,nm,pss):
        print('Register !')
        print(nm)
        print(em)
        print(pss)
        s.sys.register(nm,em,pss)

class system:

    rows = con = obj = None

    def __init__(s,main):
        s.main = main
        s.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="contact_book"
        )
        s.obj = s.con.cursor()

    def login(s,em,pss):
        sql ='SELECT * FROM admin WHERE `email`=%s AND `password`=%s'
        s.obj.execute(sql,(em,pss,))
        s.rows = s.obj.fetchall()
        if s.rows!=None:
            print('logged successfully !')
            print(s.rows)

    def register(s,nm,em,pss):
        alrt = Label(s.main,text='',fg='red')
        alrt.grid(row=0,column=0,columnspan=2)
        sql = "SELECT * FROM `user_log` WHERE `name`=%s OR `email`=%s"
        s.obj.execute(sql,(em,nm,))
        rows = s.obj.fetchall()
        if rows!=None:
            alrt.config(text='Username or Email already taken !')
        else:
            sql ="INSERT INTO admin( `name`,  `email`,`password`) VALUES (%s,%s,%s)"
            s.obj.execute(sql,(nm,em,pss))
            s.con.commit()


main = Tk()
main.title('Login main')
main.grid()

log = Button(main,text='Login',bg='green',fg='white',width=15,height=2,command=lambda:pg.login(pg.em.get(),pg.pss.get()))
log.grid(row=4,column=0)

reg = Button(main,text='want to register',bg='black',fg='white',width=20,height=2,command=lambda:pg.reg_p())
reg.grid(row=4,column=1)

sys = system(main)
pg = page(main,log,reg,sys)

main.mainloop()