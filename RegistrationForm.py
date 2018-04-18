#mysql and mysql-connector-python both must be installed
# mysql user: root and password: oracle

from tkinter import*
from PIL import Image,ImageTk
import mysql.connector as mc
import tkinter.messagebox as tm
n=500

class login(Tk):
 def __init__(self,*args,**kwargs):
  Tk.__init__(self,*args,**kwargs)
  container=Frame(self)  
  container.pack(side=TOP, fill=BOTH, expand=1)
  container.grid_rowconfigure(0, weight=1)
  container.grid_columnconfigure(0, weight=1)
 
  self.frames={}

  F=WelcomePage
  frame=F(container,self)
  self.frames[F]=frame
  frame.grid(row=0,column=0,sticky="nsew")
  self.show_frame(WelcomePage)

 def show_frame(self, cont):
  frame=self.frames[cont]
  frame.tkraise()


class WelcomePage(Frame) :

 def __init__(self,parent,controller) :
  Frame.__init__(self,parent)
  
  cnx = mc.connect(user='root', password='oracle', host='127.0.0.1')
  cursor=cnx.cursor()
  cursor.execute("""CREATE DATABASE IF NOT EXISTS python""")
  cnx.commit()
  cnx.close()
  cnx = mc.connect(user='root', password='oracle', host='127.0.0.1', database='python')
  cursor=cnx.cursor()
  cursor.execute("""CREATE TABLE IF NOT EXISTS register(tname varchar(50),tldr varchar(50),contact int(12),members int(2), internet varchar(4))""")
  cnx.commit()
  cnx.close()
  
  load=Image.open("lo.png")
  pic=ImageTk.PhotoImage(load)
  b2=Button(self, image=pic, command=lambda:exit())
  b2.image=pic
  b2.place(relx=0.5, rely=0.1, anchor=CENTER)
  
  t1=Label(self, text="Team Name:")
  t1.place(relx=0.3, rely=0.3, anchor=W)
  self.e1=Entry(self)
  self.e1.place(relx=0.6, rely=0.3, anchor=CENTER)
  
  t2=Label(self, text="Team Leader Name:")
  t2.place(relx=0.3, rely=0.4, anchor=W)
  self.e2=Entry(self)
  self.e2.place(relx=0.6, rely=0.4, anchor=CENTER)

  t3=Label(self, text="Team Leader Contact:")
  t3.place(relx=0.3, rely=0.5, anchor=W)
  self.e3=Entry(self)
  self.e3.place(relx=0.6, rely=0.5, anchor=CENTER)

  t2=Label(self, text="Number of Members:")
  t2.place(relx=0.3, rely=0.6, anchor=W)
  self.e4=Entry(self)
  self.e4.place(relx=0.6, rely=0.6, anchor=CENTER)

  t2=Label(self, text="Do you require internet connection?")
  t2.place(relx=0.4, rely=0.7, anchor=CENTER)

  b3=Button(self, text="Submit", command =lambda: [self.submit(),self.popupmsg()])
  b3.place(relx=0.4, rely=0.8, anchor=CENTER)
  
  load=Image.open("exit.png")
  pic=ImageTk.PhotoImage(load)
  b2=Button(self, image=pic, command=lambda:exit())
  b2.image=pic
  b2.place(relx=0.6, rely=0.8, anchor=CENTER)
  
 def clkexit(self) :
  exit()
  
 def popupmsg(a):
    global n
    popup = Tk()
    popup.wm_title("Successful!")
    label = Label(popup, text="Succesfully Registered!\nRegistration number={}".format(n), justify="left")
    label.place(relx=0.5, rely=0.4, anchor=CENTER)
    n+=1
    b = Button(popup, text="OKAY!",command= popup.destroy)
    b.place(relx=0.5, rely=0.7, anchor=CENTER)
    popup.geometry("400x300")
    popup.mainloop()

 def submit(self):
     cnx = mc.connect(user='root', password='oracle', host='127.0.0.1', database='python')
     cursor=cnx.cursor()
     tn=self.e1.get()
     tl=self.e2.get()
     con=int(self.e3.get())
     mem=int(self.e4.get())
     #em=self.e4.get()
     cursor.execute("""INSERT INTO register VALUES(%s,%s,%s,%s,%s)""",(tn,tl,con,mem,"yes"))
     cnx.commit()
     cnx.close()
     self.e1.delete(0,'end')
     self.e2.delete(0, 'end')
     self.e3.delete(0,'end')
     self.e4.delete(0, 'end')
  
app=login()
app.attributes('-fullscreen', True)
app.mainloop()
