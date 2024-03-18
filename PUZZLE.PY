from tkinter import *

root = Tk()

class puzzle:
     def __init__(s):
        root.title("puzzle game")
        root.geometry("240x210")

     def logic(s,btn_no):
          btn1 = s.b1.cget("text")
          # btn2 = s.b2.cget("text")
          # btn2 = s.b3.cget("text")
          btn1 = s.b1.cget("text")
          if btn_no == 1 :
               if s.b2.cget("text") == "":
                    s.b1.config(text="")
                    s.b2.config(text=btn1)
               elif s.b4.cget("text") == "":
                    s.b1.config(text="")
                    s.b4.config(text=btn1)

          if btn_no == 2:
               print(s.b1.cget("text"))
               print(s.b2.cget("text"))
               btn2 = s.b2.cget("text")
               if s.b1.cget("text") == "":
                    s.b1.config(text=btn2)       
                    s.b2.config(text="")
               elif s.b3.cget("text") == "":
                    s.b3.config(text=btn2)
                    s.b2.config(text="")
               elif s.b5.cget("text") == "":
                    s.b5.config(text=btn2)
                    s.b2.config(text="")

          if btn_no == 3:
               print(s.b3.cget("text"))
               print(s.b2.cget("text"))
               btn3 = s.b3.cget("text")
               if s.b2.cget("text") == "":
                    s.b2.config(text=btn3)
                    s.b3.config(text="")
               elif s.b6.cget("text") == "":
                    s.b6.config(text=btn3)
                    s.b3.config(text="")

          if btn_no == 4:
               print(s.b4.cget("text"))
               print(s.b5.cget("text"))
               btn4 = s.b4.cget("text")
               if s.b5.cget("text") == "":
                    s.b5.config(text=btn4)
                    s.b4.config(text="")
               elif s.b7.cget("text") == "":
                    s.b7.config(text=btn4)
                    s.b4.config(text="")
               elif s.b1.cget("text") == "":
                    s.b1.config(text=btn4)
                    s.b4.config(text="")

          if btn_no == 5:
               print(s.b5.cget("text"))
               print(s.b4.cget("text"))
               btn5 = s.b5.cget("text")
               if s.b4.cget("text") == "":
                    s.b4.config(text=btn5)
                    s.b5.config(text="")
               elif s.b6.cget("text") == "":
                    s.b6.config(text=btn5)
                    s.b5.config(text="")
               elif s.b8.cget("text") == "":
                    s.b8.config(text=btn5)
                    s.b5.config(text="")
               elif s.b2.cget("text") == "":
                    s.b2.config(text=btn5)
                    s.b5.config(text="")

          if btn_no == 6:
               print(s.b6.cget("text"))
               print(s.b5.cget("text"))
               btn6 = s.b6.cget("text")
               if s.b5.cget("text") == "":
                    s.b5.config(text=btn6)
                    s.b6.config(text="")
               elif s.b9.cget("text") == "":
                    s.b9.config(text=btn6)
                    s.b6.config(text="")
               elif s.b3.cget("text") == "":
                    s.b3.config(text=btn6)
                    s.b6.config(text="")

          if btn_no == 7:
               print(s.b7.cget("text"))
               print(s.b8.cget("text"))
               btn7 = s.b7.cget("text")
               if s.b8.cget("text") == "":
                    s.b8.config(text=btn7)
                    s.b7.config(text="")
               elif s.b4.cget("text") == "":
                    s.b4.config(text=btn7)
                    s.b7.config(text="")
     
          if btn_no == 8:
               btn8 = s.b8.cget("text")
               if s.b7.cget("text") == "":
                    s.b7.config(text=btn8)
                    s.b8.config(text="")
               elif s.b9.cget("text") == "":
                    s.b9.config(text=btn8)
                    s.b8.config(text="")
               elif s.b5.cget("text") == "":
                    s.b5.config(text=btn8)
                    s.b8.config(text="")

          if btn_no == 9:
               btn9 = s.b9.cget("text")
               if s.b8.cget("text") == "":
                    s.b8.config(text=btn9)
                    s.b9.config(text="")
               elif s.b6.cget("text") == "":
                    s.b6.config(text=btn9)
                    s.b9.config(text="")

          if s.b1["text"] == '1' and s.b2['text'] == '2' and s.b3['text'] == '3' and s.b4['text'] == '4' and s.b5['text'] == '5' and s.b6['text'] == '6' and s.b7['text'] == '7' and s.b8['text'] == '8':
               print("win")
               win = Label(root,text="you are win")
               win.grid(row=4,column=1,columnspan=3)
          


     def btn_design(s):
          s.b1 = Button(root,text="5",width=10,height=4,command=lambda:game.logic(1))
          s.b1.grid(row=0,column=1)
          s.b2 = Button(root,text="3",width=10,height=4,command=lambda:game.logic(2))
          s.b2.grid(row=0,column=2)
          s.b3 = Button(root,text="1",width=10,height=4,command=lambda:game.logic(3))
          s.b3.grid(row=0,column=3)

          s.b4 = Button(root,text="4",width=10,height=4,command=lambda:game.logic(4))
          s.b4.grid(row=1,column=1)
          s.b5 = Button(root,text="8",width=10,height=4,command=lambda:game.logic(5))
          s.b5.grid(row=1,column=2)
          s.b6 = Button(root,text="7",width=10,height=4,command=lambda:game.logic(6))
          s.b6.grid(row=1,column=3)

          s.b7 = Button(root,text="2",width=10,height=4,command=lambda:game.logic(7))
          s.b7.grid(row=2,column=1)
          s.b8 = Button(root,text="6",width=10,height=4,command=lambda:game.logic(8))
          s.b8.grid(row=2,column=2)
          s.b9 = Button(root,text="",width=10,height=4,command=lambda:game.logic(9))
          s.b9.grid(row=2,column=3)
          
        
    

game = puzzle()
game.btn_design()
root.mainloop()



          
      



