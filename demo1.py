from tkinter import *

root = Tk()
x = 0
def task(x):
    x += 1
    print(x)
#     root.after(2000, task, x)  # reschedule event in 2 seconds

root.after(2000, task, x)
root.mainloop()