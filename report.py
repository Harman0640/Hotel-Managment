import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
from printout import my_cust_PDF


class Report1Class:
    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title("My College Manager\Student Report")


        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        x1 = 200
        w1 = w - x1
        y1 = 50
        h1 = h - y1 - 245
        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1 + 7, x1 - 5, y1 + 165))  # wxh+x+y

        # ------------- widgets ----------------------------------
        mycolor1 = '#EDE8F5'
        mycolor2 = '#7091E6'
        myfont1 = ('Cambria',13,'bold')
        self.window.config(background=mycolor1)

        self.hdlbl = Label(self.window,text='Report',background='grey',font=('Cambria',20,'bold'))

        #------------------ table ---------------------
        self.mytable1 = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11'],height=20)

        self.mytable1.heading('c1',text='Ref no')
        self.mytable1.heading('c2',text='Name')
        self.mytable1.heading('c3',text='Mother Name')
        self.mytable1.heading('c4',text='Gender')
        self.mytable1.heading('c5',text='Postcode')
        self.mytable1.heading('c6',text='Contact')
        self.mytable1.heading('c7',text='Email')
        self.mytable1.heading('c8',text='Nationailty')
        self.mytable1.heading('c9',text='Id-Type')
        self.mytable1.heading('c10',text='Id-Number')
        self.mytable1.heading('c11',text='Address')
        self.mytable1['show']='headings'

        self.mytable1.column('c1',width=100,anchor='center')
        self.mytable1.column('c2',width=100,anchor='center')
        self.mytable1.column('c3',width=100,anchor='center')
        self.mytable1.column('c4',width=100,anchor='center')
        self.mytable1.column('c5',width=100,anchor='center')
        self.mytable1.column('c6',width=100,anchor='center')
        self.mytable1.column('c7',width=200,anchor='center')
        self.mytable1.column('c8',width=100,anchor='center')
        self.mytable1.column('c9',width=90,anchor='center')
        self.mytable1.column('c10',width=100,anchor='center')
        self.mytable1.column('c11',width=100,anchor='center')

        #----------------- buttons ---------------------
        self.b1 = Button(self.window,text='Print',font=myfont1,background='#E3E1D9',command=self.getPrintout)

        # ------------placement -----------------
        self.hdlbl.place(x=0,y=0,width=w,height=70)
        x1 = 40
        y1 =100
        x_diff = 150
        y_diff = 50
        self.mytable1.place(x=x1,y=y1)
        y1+=450
        self.b1.place(x=x1+520,y=y1,width=150,height=40)

        #------call required functions ----------
        self.databaseConnection()
        self.pdata=[]
        self.showAllData()
        self.window.mainloop()

    def getPrintout(self):
        pdf = my_cust_PDF()

        headings = ['Ref ','Name', 'Mother Name','Mobile','Nationality','Id Proof Type','Id Number','Address']

        pdf.page_content(headings, self.pdata)
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')

    def databaseConnection(self):

        try:
            self.conn = pymysql.connect(host='localhost',db='hotel_database',user='root',password='')
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Connection Error","Error in Database Connection : \n"+str(e),parent=self.window)

    def showAllData(self):
        try:
            #rollno	name	phone	gender	dob	address	department	course
            qry = 'select * from customer'
            rowcount = self.curr.execute(qry )
            rowdata = self.curr.fetchall()
            # print("Row Data = ",rowdata)
            self.pdata=[]
            if rowdata:
                for row in rowdata:
                    myr1 = [row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
                    self.mytable1.insert('',END,values=row)
                    self.pdata.append(myr1)
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error in fetching : \n"+str(e),parent=self.window)


#--------- for testing only ------------
if __name__ == '__main__':
    dummy_home=Tk()
    Report1Class(dummy_home)
    dummy_home.mainloop()