from tkinter import *
from tkinter import messagebox

from loginpage import LoginClass
from report import Report1Class
from customerpage import CustomerPage
from details import details
from room import Room

import pymysql
from PIL import Image, ImageTk




class HomepageClass:
    def __init__(self):
        self.window = Tk()
        self.window.title("Royal Hotal")

        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))#wxh+x+y
        self.window.state('zoomed')

        #--------------- Frames -----------------
        f1_width=200
        f2_width=w-f1_width
        self.f1 = Frame(self.window,background='#3d5a80')
        self.f2 = Frame(self.window,background='#98c1d9')
        self.f1.place(x=0,y=0,width=f1_width,height=h)
        self.f2.place(x=f1_width,y=0,width=f2_width,height=h)




        #---------------- Menu in frame 1 --------------------------
        x1=0
        y1=227
        b1_width=f1_width-10
        b1_height=40
        y_diff = b1_height
        mycolor1='#F2EFE5'
        myfont1 = ('Cambria',13,'bold')

        # ---------------Heading------------------
        self.hdlbl = Label(self.window, text='Hotel Management System',background='grey',fg='black',relief='ridge',
                           font=('times new roman', 30, 'bold'))

        self.menu=Label(text="MENU",font=('times new roman', 20, 'bold'),bg='black',fg='white',relief="ridge")

        #---------------widgets--------------------
        self.b1 = Button(self.window,text='CUSTOMER',background='grey',fg='black',relief='ridge',
                           font=('times new roman', 15, 'bold'),command=lambda :CustomerPage(self.window))
        self.b2 = Button(self.window, text='ROOM', background='grey', fg='black', relief='ridge',
                         font=('times new roman', 15, 'bold'),command=lambda :Room(self.window))
        self.b3 = Button(self.window, text='DETAILS', background='grey', fg='black', relief='ridge',
                         font=('times new roman', 15, 'bold'),command=lambda :details(self.window))
        self.b4 = Button(self.window, text='REPORT', background='grey', fg='black', relief='ridge',
                         font=('times new roman', 15, 'bold'),command=lambda :Report1Class(self.window))
        self.b5 = Button(self.window, text='LOGOUT', background='grey', fg='black', relief='ridge',
                         font=('times new roman', 15, 'bold'),command=self.quitter)






        #------------- placement -------------------

        self.hdlbl.place(x=0, y=130, width=w, height=60)
        self.menu.place(x=0,y=190,width=200)

        self.b1.place(x=0, y=y1 ,width=200)
        y1 += y_diff
        self.b2.place(x=0, y=y1, width=200)
        y1 += y_diff
        self.b3.place(x=0, y=y1, width=200)
        y1 += y_diff
        self.b4.place(x=0, y=y1, width=200)
        y1 += y_diff
        self.b5.place(x=0, y=y1, width=200)
        y1 += y_diff

        #------------------ logo  in Frame 1----------------------

        # show image
        self.bkimg1 = Image.open("logo_images//logo.jpg").resize((200,130))
        self.bkpimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.f1,image=self.bkpimg1,relief="ridge")
        self.bklbl.place(x=0,y=0)

        #--------------------------------------------------------------------
        # show image
        self.bkimg2 = Image.open("logo_images//TopPic.webp").resize((w,130))
        self.bkpimg2 = ImageTk.PhotoImage(self.bkimg2)
        self.bklbl2 = Label(self.f2, image=self.bkpimg2)
        self.bklbl2.place(x=0, y=0)

        #---------------------------------------------------------------------
        # show image
        self.bkimg3 = Image.open("logo_images//bgimg.jpeg").resize((f2_width,h))
        self.bkpimg3 = ImageTk.PhotoImage(self.bkimg3)
        self.bklbl3 = Label(self.f2, image=self.bkpimg3)
        self.bklbl3.place(x=0, y=190)




        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Logout??", parent=self.window)
        if ans == 'yes':
            self.window.destroy()
            from loginpage import LoginClass
            LoginClass()


if __name__ == '__main__':
    HomepageClass()