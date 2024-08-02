from tkinter import *
from tkinter import ttk
import tkinter.messagebox

import messagebox
#from tkinter.ttk import Treeview

import pymysql
import random


class CustomerPage:


    def __init__(self,hwindow):
        self.window = Toplevel(hwindow)
        self.window.title("Royal Hotal/Customer")

        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        x1 = 200
        w1 = w-x1
        y1 = 50
        h1 = h-y1-245
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1+7,x1-5,y1+165))#wxh+x+y

        #------------------------variables-----------------------------------
        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))

        self.var_cname=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post= StringVar()
        self.var_mobile = StringVar()
        self.var_email= StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()

      #----------------------widgets------------------------------
        self.hdlbl = Label(self.window, text='Add Customer Details', background='grey', fg='black', relief='ridge',
                           font=('times new roman', 20, 'bold'))

        #--------------------lableframe-----------------------------------------
        lableframeleft=LabelFrame(self.window,bd=2,relief="ridge",text="Customer Details",font=("times new roman",12,'bold'))

        #-------------------lables and entrys-----------------------------------

        #custref
        lbl_cust_ref=Label(lableframeleft,text='Customer Ref',font=("arial",12,'bold'),padx=2,pady=6)
        enty_ref=ttk.Entry(lableframeleft,width=29,textvariable=self.var_ref,font=("times new roman",13,'bold'),state='readonly')

        #cust name
        cname = Label(lableframeleft, text='Customer Name:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtcname= ttk.Entry(lableframeleft, width=29,textvariable=self.var_cname, font=("arial", 13, 'bold'))

        #mother name
        lblmname=Label(lableframeleft, text='Mother Name:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtmname= ttk.Entry(lableframeleft, width=29,textvariable=self.var_mother, font=("arial", 13, 'bold'))

        #gender combobox
        label_gender=Label(lableframeleft,font=("arial", 12, 'bold'),text='Gender:', padx=2, pady=6)
        combo_gender=ttk.Combobox(lableframeleft, width=27,textvariable=self.var_gender,state='readonly', font=("arial", 13, 'bold'))
        combo_gender['value']=('Male','Female')
        combo_gender.current(0)


        #postcode
        lblpostcode=Label(lableframeleft, text='Postcode:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtpostcode= ttk.Entry(lableframeleft, width=29,textvariable=self.var_post, font=("arial", 13, 'bold'))

        #mobilenumber
        lblmobile=Label(lableframeleft, text='Mobile:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtmobile= ttk.Entry(lableframeleft, width=29,textvariable=self.var_mobile, font=("arial", 13, 'bold'))

        #email
        lblEmail=Label(lableframeleft,text='Email:', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtEmail= ttk.Entry(lableframeleft, width=29,textvariable=self.var_email, font=("arial", 13, 'bold'))

        #nationality
        lblnationality=Label(lableframeleft,font=("arial", 12, 'bold'), text='Nationality:',padx=2, pady=6)
        combo_nationality = ttk.Combobox(lableframeleft, width=27,textvariable=self.var_nationality, state='readonly', font=("arial", 13, 'bold'))
        combo_nationality['value'] = ('Indian', 'American','British')
        combo_nationality.current(0)


        #idproof type  combobox
        lblIdProof=Label(lableframeleft,font=("arial", 12, 'bold'), text='Id Proof Type:',padx=2, pady=6)
        combo_id = ttk.Combobox(lableframeleft, width=27,textvariable=self.var_idproof, state='readonly', font=("arial", 13, 'bold'))
        combo_id['value'] = ('AdhaarCard', 'DrivingLicence', 'Passport')
        combo_id.current(0)

        #id number
        lblidnumber = Label(lableframeleft, text='Id Number', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtidnumber = ttk.Entry(lableframeleft, width=29,textvariable=self.var_idnumber, font=("arial", 13, 'bold'))

        #address
        lbladdress = Label(lableframeleft, text='Address', font=("arial", 12, 'bold'), padx=2, pady=6)
        txtaddress = ttk.Entry(lableframeleft, width=29,textvariable=self.var_address, font=("arial", 13, 'bold'))


        # ------------- placement -------------------


        self.hdlbl.place(x=0, y=0, width=w, height=30)
        lableframeleft.place(x=5,y=30,width=425,height=490)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref.grid(row=0,column=1)
        cname.grid(row=1, column=0, sticky=W)
        txtcname.grid(row=1,column=1)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname.grid(row=2, column=1)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender.grid(row=3,column=1)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtpostcode.grid(row=4,column=1)
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile.grid(row=5, column=1)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail.grid(row=6, column=1)
        lblnationality.grid(row=7, column=0, sticky=W)
        combo_nationality.grid(row=7, column=1)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id.grid(row=8, column=1)
        lblidnumber.grid(row=9, column=0, sticky=W)
        txtidnumber.grid(row=9, column=1)
        lbladdress.grid(row=10, column=0, sticky=W)
        txtaddress.grid(row=10, column=1)

        #-----------------------buttons-------------------------
        btn_frame=Frame(lableframeleft,bd=2,relief="ridge")
        btn_frame.place(x=0,y=385,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.saveData,font=("arial", 13, 'bold'),bg='black',fg='white',width=9)
        btnadd.grid(row=0,column=0,padx=1)
        btnupdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 13, 'bold'), bg='black', fg='white', width=9)
        btnupdate.grid(row=0, column=1, padx=1)
        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 13, 'bold'), bg='black', fg='white', width=9)
        btnDelete.grid(row=0, column=2, padx=1)
        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 13, 'bold'), bg='black', fg='white', width=9)
        btnReset.grid(row=0, column=3, padx=1)


        #-------------------tableframe-------------------------
        tableframe=LabelFrame(self.window,bd=2,relief="ridge",text="View Details and Search System",font=("times new roman",12,'bold'))
        tableframe.place(x=435,y=30,width=860,height=490)

        lblsearchby = Label(tableframe, text='Search By:', font=("arial", 12, 'bold'),bg='yellow',fg='black')
        lblsearchby.grid(row=0,column=0,padx=2)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(tableframe,textvariable=self.search_var, width=10, state='readonly', font=("arial", 13, 'bold'))
        combo_search['value'] = ('Mobile')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch = ttk.Entry(tableframe,textvariable=self.txt_search, width=20, font=("arial", 13, 'bold'))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch= Button(tableframe, text="Search",command=self.search, font=("arial", 13, 'bold'), bg='black', fg='white', width=9,)
        btnsearch.grid(row=0, column=3, padx=2)
        btnshowall = Button(tableframe, text="ShowAll",command=self.fetchdata, font=("arial", 13, 'bold'), bg='black', fg='white', width=9)
        btnshowall.grid(row=0, column=4, padx=2)

        #-----------------------data table--------------------------------
        detail_table=Frame(tableframe,bd=2,relief="ridge")
        detail_table.place(x=0,y=50,width=855,height=350)

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)

        self.cust_table = ttk.Treeview(detail_table,column=("ref","name","mother","gender","post","mobile",
                                                          "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_table.xview)
        scroll_y.config(command=self.cust_table.yview)

        self.cust_table.heading("ref",text="Refer No")
        self.cust_table.heading("name", text="Name")
        self.cust_table.heading("mother", text="Mother Name")
        self.cust_table.heading("gender", text="Gender")
        self.cust_table.heading("post", text="PostCode")
        self.cust_table.heading("mobile", text="Mobile")
        self.cust_table.heading("email", text="Email")
        self.cust_table.heading("nationality", text="Nationality")
        self.cust_table.heading("idproof", text="Id Proof")
        self.cust_table.heading("idnumber", text="Id Number")
        self.cust_table.heading("address", text="Address")

        self.cust_table["show"]="headings"


        self.cust_table.column("ref",width=100,anchor="center")
        self.cust_table.column("name",width=100,anchor="center")
        self.cust_table.column("mother",width=100,anchor="center")
        self.cust_table.column("gender",width=100,anchor="center")
        self.cust_table.column("post",width=100,anchor="center")
        self.cust_table.column("mobile", width=100,anchor="center")
        self.cust_table.column("email",width=200,anchor="center")
        self.cust_table.column("nationality",width=100,anchor="center")
        self.cust_table.column("idproof",width=100,anchor="center")
        self.cust_table.column("idnumber",width=100,anchor="center")
        self.cust_table.column("address",width=100,anchor="center")
        self.cust_table.pack(fill=BOTH, expand=1)
        self.cust_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

        # ------call required functions ----------
        self.databaseConnection()

        self.window.mainloop()
    def databaseConnection(self):

        try:
            self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
            self.curr = self.conn.cursor()
        except Exception as e:
            tkinter.messagebox.showerror("Connection Error", "Error in Database Connection : \n" + str(e),
                                 parent=self.window)


        #-------------------Function------------------------


    def saveData(self):

        try:

            qry = 'insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            rowcount = self.curr.execute(qry, (self.var_ref.get(), self.var_cname.get(),self.var_mother.get(),
                    self.var_gender.get(),self.var_post.get(),self.var_mobile.get(),
                     self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),
                     self.var_idnumber.get(),self.var_address.get()))
            self.conn.commit()
            self.fetchdata()
            self.reset()
            if rowcount==1:

                tkinter.messagebox.showinfo("Success"," Record Saved successfully",parent=self.window)
                   # self.clearPage()
            else:
                tkinter.messagebox.showwarning("Failure","Record not Saved y",parent=self.window)

        except Exception as e:
                tkinter.messagebox.showerror("Query Error","Error in insertion : \n"+str(e),parent=self.window)


    def fetchdata(self):
        self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
        self.curr = self.conn.cursor()
        rowcount = self.curr.execute('select * from customer')
        rows=self.curr.fetchall()
        if len(rows)!=0:
            self.cust_table.delete(*self.cust_table.get_children())
            for i in rows:
                self.cust_table.insert("",END,values=i)
            self.conn.commit()


    def get_cursor(self,event=""):
        cursor_row=self.cust_table.focus()
        content=self.cust_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cname.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        try:
            if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please enter mobile number")
            else:
                self.conn = pymysql.connect(host='localhost', db='hotel_database', user='root', password='')
                self.curr = self.conn.cursor()
                qry = 'update customer set name=%s, mother=%s,gender=%s, post=%s,' \
                      ' mobile=%s, email=%s,nationality=%s,idproof = %s,idnumber = %s,address = %s where ref=%s'
                rowcount = self.curr.execute(qry, (self.var_cname.get(), self.var_mother.get(),
                                                   self.var_gender.get(), self.var_post.get(), self.var_mobile.get(),
                                                   self.var_email.get(), self.var_nationality.get(), self.var_idproof, self.var_idnumber.get()
                                                   , self.var_address.get(), self.var_ref.get()))
                self.conn.commit()
                self.fetchdata()
                if rowcount == 1:

                    tkinter.messagebox.showinfo("Success", "customer Record Updated successfully", parent=self.window)

                else:
                    tkinter.messagebox.showwarning("Failure", "customer Record not Updated ", parent=self.window)

        except Exception as e:
            tkinter.messagebox.showerror("Query Error", "Error in insertion : \n" + str(e), parent=self.window)

    def delete(self):
        delete=tkinter.messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.window)
        if delete>0:
            qry='delete from customer where ref=%s'
            value=(self.var_ref.get(),)
            self.curr.execute(qry,value)
        else:
            if not delete:
                return
        self.conn.commit()
        self.fetchdata()
        self.reset()


    def reset(self):
        self.var_ref.set(""),
        self.var_cname.set(""),
        self.var_mother.set(""),

        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),

        self.var_idnumber.set(""),
        self.var_address.set("")
        x = random.randint(1000, 10000)
        self.var_ref.set(str(x))

    def search(self):
        try:
            self.cust_table.delete(*self.cust_table.get_children())

            qry = 'select * from customer where mobile like %s'
            rowcount = self.curr.execute(qry, (self.var_mobile.get() + "%"))
            rowdata = self.curr.fetchall()
            if rowdata:
                for row in rowdata:
                    self.cust_table.insert('', END, values=row)
            else:
                messagebox.showwarning("Empty", "No Record Found")

        except Exception as e:
            messagebox.showerror("Query Error", "Error in fetching : \n" + str(e))





# --------- for testing only ------------
if __name__ == '__main__':
     dummy_home=Tk()
     CustomerPage(dummy_home)
     dummy_home.mainloop()