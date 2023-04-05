from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cus_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        #=============== variables ==============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()

        #============== title ==============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #===========logo================
        img2=Image.open(r"images\royal-logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #===========label frame=============

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # cust ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",12,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        # cust name
        cname=Label(labelframeleft,text="Customer Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",12,"bold"))
        txtcname.grid(row=1,column=1)

        # mother name
        mname=Label(labelframeleft,text="Mother Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("arial",12,"bold"))
        txtmname.grid(row=2,column=1)

        # gender combobox
        label_gender=Label(labelframeleft,text="Gender :",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=27,font=("arial",12,"bold"),state="readonly")
        combo_gender["value"]=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # postcode
        lbl_PostCode=Label(labelframeleft,text="Post Code :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_PostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=29,font=("arial",12,"bold"))
        txtPostCode.grid(row=4,column=1)
        
        # mobile 
        lblMobile=Label(labelframeleft,text="Mobile No. :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",12,"bold"))
        txtMobile.grid(row=5,column=1)

        # email
        lblEmail=Label(labelframeleft,text="Email ID. :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",12,"bold"))
        txtEmail.grid(row=6,column=1)

        # nationality
        lblNationality=Label(labelframeleft,text="Nationality :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=27,font=("arial",12,"bold"),state="readonly")
        combo_Nationality["value"]=("Select","Australia","Argentina","India","United States Of America","United Kingdom")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


        # id proof type combobox
        lbl_IdProof=Label(labelframeleft,text="Id Proof Type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_IdProof.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,width=27,font=("arial",12,"bold"),state="readonly")
        combo_id["value"]=("Select","Passport","Driving License")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)


        # id number
        lblIdNumber=Label(labelframeleft,text="Id Number :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",12,"bold"))
        txtIdNumber.grid(row=9,column=1)

        # address
        lblAddress=Label(labelframeleft,text="Address :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",12,"bold"))
        txtAddress.grid(row=10,column=1)

        #======================btns===================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnReset.grid(row=0,column=3,padx=1)

        #================ table frame =================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_frame,text="SEARCH BY :",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,width=24,font=("arial",12,"bold"),state="readonly")
        combo_Search["value"]=("Select","Mobile","Ref","Email")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("times new roman",12,"bold"),width=10,bg="black",fg="gold")
        btnShowAll.grid(row=0,column=4,padx=1)

        #============ show data table ==============
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","postcode","mobile",
                                                          "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Reference no.")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("postcode",text="Postcode")
        self.Cust_Details_Table.heading("mobile",text="Mobile no. ")
        self.Cust_Details_Table.heading("email",text="Email id.")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id no.")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("postcode",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else :
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                      self.var_ref.get(),
                                                                                                      self.var_cust_name.get(),
                                                                                                      self.var_mother.get(),
                                                                                                      self.var_gender.get(),
                                                                                                      self.var_postcode.get(),
                                                                                                      self.var_mobile.get(),
                                                                                                      self.var_email.get(),
                                                                                                      self.var_nationality.get(),
                                                                                                      self.var_idproof.get(),
                                                                                                      self.var_idnumber.get(),
                                                                                                      self.var_address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer Has Been Added",parent=self.root)
            except Exception as es :
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows :
                self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
            conn.close()
            
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_postcode.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="" :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(                                                                                                                                                                               
                                                                                                                                                                               self.var_cust_name.get(),
                                                                                                                                                                               self.var_mother.get(),
                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                               self.var_postcode.get(),
                                                                                                                                                                               self.var_mobile.get(),
                                                                                                                                                                               self.var_email.get(),
                                                                                                                                                                               self.var_nationality.get(),
                                                                                                                                                                               self.var_idproof.get(),
                                                                                                                                                                               self.var_idnumber.get(),
                                                                                                                                                                               self.var_address.get(),
                                                                                                                                                                               self.var_ref.get(),
                                                                                                                                                                              ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Has Been Updated Successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else :
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):        
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        self.var_postcode.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_idnumber.set(""),
        self.var_address.set(""),
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+ " LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()









if __name__ == "__main__":
    root=Tk()
    obj=Cus_Win(root)
    root.mainloop()
