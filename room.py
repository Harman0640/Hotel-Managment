import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import messagebox
from time import strptime
from datetime import datetime
from tkinter.ttk import Treeview

import pymysql
import random

class Room:


    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title("Royal Hotel/RoomBooking")

        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        x1 = 200
        w1 = w-x1
        y1 = 50
        h1 = h-y1-245
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1+7,x1-5,y1+165))#wxh+x+y

        #------------------------variables------------------------------------
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailiable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ----------------------widgets------------------------------
        self.hdlbl = Label(self.window, text='RoomBooking', background='grey', fg='black', relief='ridge',
                           font=('times new roman', 20, 'bold'))
        # --------------------lableframe-----------------------------------------
        lableframeleft = LabelFrame(self.window, bd=2, relief="ridge", text="RoomBooking Details",
                                    font=("times new roman", 12, 'bold'))

        # -------------------lables and entrys-----------------------------------

        # cust_contact
        lbl_cust_contact=Label(lableframeleft, text='Customer Contact', font=("arial", 12, 'bold'), padx=2, pady=6)
        enty_contact = ttk.Entry(lableframeleft,textvariable=self.var_contact, width=18,  font=("times new roman", 13, 'bold'))

        #fetchdata button
        btnfetchdata = Button(lableframeleft,command=self.fetch_contact, text="Fetch ", font=("arial", 13, 'bold'), bg='black',
                           fg='white', width=9, )
        btnfetchdata.place(x=320,y=4)

        # check_in_date
        check_in_date = Label(lableframeleft, text='check_in Date:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtcheck_in_date = ttk.Entry(lableframeleft,textvariable=self.var_checkin, width=29, font=("arial", 13, 'bold'))

        # check_out_date
        check_out_date = Label(lableframeleft, text='check_out Date:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtcheck_out_date = ttk.Entry(lableframeleft,textvariable=self.var_checkout, width=29, font=("arial", 13, 'bold'))

        # room type
        label_roomtype = Label(lableframeleft, font=("arial", 12, 'bold'), text='Room Type:', padx=2, pady=6)
        combo_roomtype = ttk.Combobox(lableframeleft,textvariable=self.var_roomtype, width=27, state='readonly',
                                    font=("arial", 13, 'bold'))

        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()
        self.curr.execute("select roomtype from details")
        id = self.curr.fetchall()
        combo_roomtype['value'] = id
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3, column=1)

        # available room
        lblroomavailiable = Label(lableframeleft, text='Room Available', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtroomavailiable = ttk.Entry(lableframeleft,textvariable=self.var_roomavailiable, width=29, font=("arial", 13, 'bold'))

        combo_roomno = ttk.Combobox(lableframeleft, textvariable=self.var_roomavailiable, width=27, state='readonly',
                                      font=("arial", 13, 'bold'))

        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()
        self.curr.execute("select roomno from details")
        rows= self.curr.fetchall()
        combo_roomno['value'] = rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)

        # meal
        lblmeal = Label(lableframeleft, text='Meal:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtmeal = ttk.Entry(lableframeleft,textvariable=self.var_meal, width=29, font=("arial", 13, 'bold'))

        # no of days
        lblNoOfDays = Label(lableframeleft, text='No Of Days:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtNoOfDays = ttk.Entry(lableframeleft,textvariable=self.var_noofdays, width=29, font=("arial", 13, 'bold'))

        # paid tax
        lblpaidtax = Label(lableframeleft, font=("arial", 12, 'bold'), text='Paid Tax:', padx=2, pady=6)
        txtpaidtax = ttk.Entry(lableframeleft,textvariable=self.var_paidtax, width=29, font=("arial", 13, 'bold'))

        # sub total
        lblsubtotal = Label(lableframeleft, font=("arial", 12, 'bold'), text='Sub Total:', padx=2, pady=6)
        txtsubtotal = ttk.Entry(lableframeleft,textvariable=self.var_actualtotal, width=29, font=("arial", 13, 'bold'))


        # total cost
        lbltotalcost = Label(lableframeleft, text='Total Cost:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txttotalcost = ttk.Entry(lableframeleft,textvariable=self.var_total, width=29, font=("arial", 13, 'bold'))
        #----------------bill button------------------------

        btnbill = Button(lableframeleft, text="Bill",command=self.total, font=("arial", 13, 'bold'), bg='black',
                        fg='white', width=9)
        btnbill.grid(row=10, column=0, padx=1,sticky=W)


        #----------------btn--------------------------------

        btn_frame = Frame(lableframeleft, bd=2, relief="ridge")
        btn_frame.place(x=0, y=385, width=412, height=40)

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

        #-------------------table frame search system------------------------------

        tableframe = LabelFrame(self.window, bd=2, relief="ridge", text="View Details and Search System",
                                font=("times new roman", 12, 'bold'))
        tableframe.place(x=435, y=200, width=860, height=300)

        lblsearchby = Label(tableframe, text='Search By:', font=("arial", 12, 'bold'), bg='yellow', fg='black')
        lblsearchby.grid(row=0, column=0, padx=2)

        self.search_var = StringVar()

        combo_search = ttk.Combobox(tableframe, textvariable=self.search_var, width=10, state='readonly',
                                    font=("arial", 13, 'bold'))
        combo_search['value'] = ('Mobile', 'Ref')
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(tableframe, textvariable=self.txt_search, width=20, font=("arial", 13, 'bold'))
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(tableframe, text="Search",command=self.search,font=("arial", 13, 'bold'), bg='black',
                           fg='white', width=9, )
        btnsearch.grid(row=0, column=3, padx=2)
        btnshowall = Button(tableframe, text="ShowAll",command=self.fetchdata, font=("arial", 13, 'bold'), bg='black',
                            fg='white', width=9)
        btnshowall.grid(row=0, column=4, padx=2)

        # -----------------------data table--------------------------------
        detail_table = Frame(tableframe, bd=2, relief="ridge")
        detail_table.place(x=0, y=50, width=855, height=200)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(detail_table, column=("contact", "checkin", "checkout", "roomtype", "roomavailiable", "meal",
                                                             "noofdays"),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Checkin")
        self.room_table.heading("checkout", text="Checkout")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailiable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No Of Days")
        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=150)
        self.room_table.column("checkin", width=150)
        self.room_table.column("checkout", width=150)
        self.room_table.column("roomtype", width=150)
        self.room_table.column("roomavailiable", width=150)
        self.room_table.column("meal", width=150)
        self.room_table.column("noofdays", width=150)
        self.room_table.pack(fill=BOTH, expand=1)
        self.fetchdata()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)







        # ------------- placement -------------------

        self.hdlbl.place(x=0, y=0, width=w, height=30)
        lableframeleft.place(x=5, y=30, width=425, height=490)
        (lbl_cust_contact.grid(row=0, column=0, sticky=W))
        enty_contact.grid(row=0, column=1, sticky=W)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date.grid(row=1,column=1)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date.grid(row=2, column=1)
        label_roomtype.grid(row=3,column=0,sticky=W)
        combo_roomtype.grid(row=3,column=1)
        lblroomavailiable.grid(row=4,column=0,sticky=W)
        txtroomavailiable.grid(row=4,column=1)
        lblmeal.grid(row=5, column=0, sticky=W)
        txtmeal.grid(row=5, column=1)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays.grid(row=6, column=1)
        lblpaidtax.grid(row=7, column=0, sticky=W)
        txtpaidtax.grid(row=7, column=1)
        lblsubtotal.grid(row=8, column=0, sticky=W)
        txtsubtotal.grid(row=8, column=1)
        lbltotalcost.grid(row=9, column=0, sticky=W)
        txttotalcost.grid(row=9, column=1)

        # ------call required functions ----------
        self.databaseConnection()

        self.window.mainloop()


    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Connection Error", "Error in Database Connection : \n" + str(e))

    def saveData(self):

        try:

            qry = 'insert into room values(%s,%s,%s,%s,%s,%s,%s)'
            rowcount = self.curr.execute(qry, (self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(),
                                            self.var_roomtype.get(),self.var_roomavailiable.get(),self.var_meal.get(),
                                            self.var_noofdays.get()))
            self.conn.commit()
            self.fetchdata()


            if rowcount==1:

                tkinter.messagebox.showinfo("Success"," Record Saved successfully",parent=self.window)
                   # self.clearPage()
            else:
                tkinter.messagebox.showwarning("Failure","Record not Saved y",parent=self.window)

        except Exception as e:
                tkinter.messagebox.showerror("Query Error","Error in insertion : \n"+str(e),parent=self.window)

    def update(self):
        try:
            if self.var_contact.get() == "":
                messagebox.showerror("Error", "Please enter mobile number")
            else:
                self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
                self.curr = self.conn.cursor()
                qry = 'update room set check_in=%s, check_out=%s,roomtype=%s, roomavailiable=%s, meal=%s,noofdays=%s' \
                      'where contact=%s'
                rowcount = self.curr.execute(qry, (self.var_checkin.get(),self.var_checkout.get(),
                                            self.var_roomtype.get(),self.var_roomavailiable.get(),self.var_meal.get(),
                                            self.var_noofdays.get(),self.var_contact.get()))
                self.conn.commit()
                self.fetchdata()
                if rowcount == 1:

                    tkinter.messagebox.showinfo("Success", "customer Record Updated successfully",parent=self.window)

                else:
                    tkinter.messagebox.showwarning("Failure", "customer Record not Updated ",parent=self.window)

        except Exception as e:
            tkinter.messagebox.showerror("Query Error", "Error in insertion : \n" + str(e))

    def delete(self):
        delete = tkinter.messagebox.askyesno("Hotel Management System", "Do you want delete this customer",
                                             parent=self.window)
        if delete > 0:
            qry = 'delete from room where contact=%s'
            value = (self.var_contact.get(),)
            self.curr.execute(qry, value)
        else:
            if not delete:
                return
        self.conn.commit()
        self.fetchdata()
        self.reset()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailiable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")

        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


    def fetchdata(self):
        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()
        rowcount = self.curr.execute('select * from room')
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailiable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact number")
        else:
            qry=("select name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            self.curr.execute(qry,value)
            row=self.curr.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found")
            else:
                self.conn.commit()

                showDataframe=Frame(self.window,bd=4,relief="ridge",padx=2)
                showDataframe.place(x=455,y=45,width=300,height=150)
                lblname=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                qry = ("select gender from customer where mobile=%s")
                value = (self.var_contact.get(),)
                self.curr.execute(qry, value)
                row = self.curr.fetchone()

                lblgender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=30)

                #-------------------email------------------------

                qry = ("select email from customer where mobile=%s")
                value = (self.var_contact.get(),)
                self.curr.execute(qry, value)
                row = self.curr.fetchone()

                lblgender = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=60)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)

                # -------------------nationality------------------------

                qry = ("select nationality from customer where mobile=%s")
                value = (self.var_contact.get(),)
                self.curr.execute(qry, value)
                row = self.curr.fetchone()

                lblgender = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=90)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=90)

                # -------------------nationality------------------------

                qry = ("select address from customer where mobile=%s")
                value = (self.var_contact.get(),)
                self.curr.execute(qry, value)
                row = self.curr.fetchone()

                lblgender = Label(showDataframe, text="address:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=120)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)


    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkout.get()

        indate = datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)

        if(self.var_meal.get() == "breakfast" and self.var_roomtype.get()=="luxary"):
            q1=float(300)
            q2=float(500)
            q3=float(self.var_noofdays.get())
            q4= float(q1+q2)
            q5= float(q3+q4)

            tax="Rs."+str('%.2f'%((q5)*0.1))
            ST="Rs."+str('%.2f'%((q5)))
            TT="Rs."+str('%.2f'%(q5+((q5)*0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "single"):
            q1 = float(500)
            q2 = float(800)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "breakfast" and self.var_roomtype.get() == "double"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "lunch" and self.var_roomtype.get() == "single"):
            q1 = float(500)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "lunch" and self.var_roomtype.get() == "double"):
            q1 = float(800)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "lunch" and self.var_roomtype.get() == "luxary"):
            q1 = float(800)
            q2 = float(1800)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "single"):
            q1 = float(800)
            q2 = float(1400)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "double"):
            q1 = float(800)
            q2 = float(1800)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "dinner" and self.var_roomtype.get() == "luxary"):
            q1 = float(800)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            tax = "Rs." + str('%.2f' % ((q5) * 0.1))
            ST = "Rs." + str('%.2f' % ((q5)))
            TT = "Rs." + str('%.2f' % (q5 + ((q5) * 0.1)))

            self.var_paidtax.set(tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




    def search(self):
        try:
            self.room_table.delete(*self.room_table.get_children())
            #rollno	name	phone	gender	dob	address	department	course
            qry = 'select * from room where contact like %s'
            rowcount = self.curr.execute(qry,(self.var_contact.get()+"%") )
            rowdata = self.curr.fetchall()
            if rowdata:
                for row in rowdata:
                    self.room_table.insert('',END,values=row)
            else:
                messagebox.showwarning("Empty","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error","Error in fetching : \n"+str(e),parent=self.window)










# --------- for testing only ------------
if __name__ == '__main__':
    dummy_home=Tk()
    Room(dummy_home)
    dummy_home.mainloop()