import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import  messagebox
from tkinter.ttk import Treeview
from time import strftime
from datetime import datetime

import pymysql
import random

class details:

    #to make independent window
    # def init(self):
    #     self.window = Tk()
    #to make dependent window
    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title("Royal Hotal/Details")

        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        x1 = 200
        w1 = w-x1
        y1 = 50
        h1 = h-y1-245
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1+7,x1-5,y1+165))#wxh+x+y

        # ------------------------variables------------------------------------
        self.var_floor= StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()

        # ----------------------widgets------------------------------
        self.hdlbl = Label(self.window, text='', background='grey', fg='black', relief='ridge',
                           font=('times new roman', 20, 'bold'))
        # --------------------lableframe-----------------------------------------
        lableframeleft = LabelFrame(self.window, bd=2, relief="ridge", text="New Room Add",
                                    font=("times new roman", 12, 'bold'))

        # floor
        lbl_floor = Label(lableframeleft, text='Floor', font=("arial", 12, 'bold'), padx=2, pady=6)
        enty_floor = ttk.Entry(lableframeleft, width=18,textvariable=self.var_floor,font=("times new roman", 13, 'bold'))

        # room no
        lbl_roomno = Label(lableframeleft, text='Room no', font=("arial", 12, 'bold'), padx=2, pady=6)
        enty_roomno = ttk.Entry(lableframeleft, width=18,textvariable=self.var_roomno, font=("times new roman", 13, 'bold'))

        # room type
        lbl_roomtype = Label(lableframeleft, text='Room Type', font=("arial", 12, 'bold'), padx=2, pady=6)
        enty_roomtype = ttk.Entry(lableframeleft, width=18,textvariable=self.var_roomtype, font=("times new roman", 13, 'bold'))


        # ------------- placement -------------------

        self.hdlbl.place(x=0, y=0, width=w, height=30)
        lableframeleft.place(x=5, y=50, width=540, height=350)
        lbl_floor.grid(row=0, column=0, sticky=W,padx=20)
        enty_floor.grid(row=0, column=1)
        lbl_roomno.grid(row=1, column=0, sticky=W,padx=20)
        enty_roomno.grid(row=1, column=1)
        lbl_roomtype.grid(row=2, column=0, sticky=W,padx=20)
        enty_roomtype.grid(row=2, column=1)

        # ----------------btn--------------------------------

        btn_frame = Frame(lableframeleft, bd=2, relief="ridge")
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnadd = Button(btn_frame, text="Save",command=self.saveData, font=("arial", 13, 'bold'), bg='black',
                        fg='white', width=9)
        btnadd.grid(row=0, column=0, padx=1)
        btnupdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 13, 'bold'), bg='black',
                           fg='white', width=9)
        btnupdate.grid(row=0, column=1, padx=1)
        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 13, 'bold'), bg='black',
                           fg='white', width=9)
        btnDelete.grid(row=0, column=2, padx=1)
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 13, 'bold'), bg='black',
                          fg='white', width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # -------------------table frame search system------------------------------

        tableframe = LabelFrame(self.window, bd=2, relief="ridge", text="Show Room Details",
                                font=("times new roman", 12, 'bold'))
        tableframe.place(x=550, y=50, width=600, height=350)

        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.room_table = ttk.Treeview(tableframe,
                                       column=("floor", "roomno",  "roomtype"),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=150)
        self.room_table.column("roomno", width=150)
        self.room_table.column("roomtype", width=150)

        self.room_table.pack(fill=BOTH, expand=1)
        self.fetchdata()
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Connection Error", "Error in Database Connection : \n" + str(e))

    def saveData(self):
        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()

        try:

            qry = 'insert into details values(%s,%s,%s)'
            rowcount = self.curr.execute(qry, (self.var_floor.get(), self.var_roomno.get(),
                                               self.var_roomtype.get()))
            self.conn.commit()
            self.fetchdata()

            if rowcount == 1:

                tkinter.messagebox.showinfo("Success", " Record Saved successfully", parent=self.window)
                # self.clearPage()
            else:
                tkinter.messagebox.showwarning("Failure", "Record not Saved y", parent=self.window)

        except Exception as e:
            tkinter.messagebox.showerror("Query Error", "Error in insertion : \n" + str(e), parent=self.window)

    def update(self):
        try:
            if self.var_floor.get() == "":
                messagebox.showerror("Error", "Please enter floor No")
            else:

                qry = 'update details set floor=%s, roomtype=%s where roomno=%s'
                rowcount = self.curr.execute(qry, (self.var_floor.get(), self.var_roomtype.get(),
                                                   self.var_roomno.get() ))
                self.conn.commit()
                self.fetchdata()
                if rowcount == 1:

                    tkinter.messagebox.showinfo("Success", " Record Updated successfully", parent=self.window)

                else:
                    tkinter.messagebox.showwarning("Failure", " Record not Updated ", parent=self.window)

        except Exception as e:
            tkinter.messagebox.showerror("Query Error", "Error in insertion : \n" + str(e))

    def delete(self):
        delete = tkinter.messagebox.askyesno("Hotel Management System", "Do you want delete this Room Details",
                                             parent=self.window)
        if delete > 0:
            qry = 'delete from details where roomno=%s'
            value = (self.var_roomno.get(),)
            self.curr.execute(qry, value)
        else:
            if not delete:
                return
        self.conn.commit()
        self.fetchdata()
        self.reset()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")


    def fetchdata(self):
        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()
        rowcount = self.curr.execute('select * from details')
        rows = self.curr.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            self.conn.commit()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2]),





#--------- for testing only ------------
if __name__ == '__main__':
    dummy_home=Tk()
    details(dummy_home)
    dummy_home.mainloop()