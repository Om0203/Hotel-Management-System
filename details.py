from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Details:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x550+230+220")
        self.root.title("Hotel Management System")

        # variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        # title
        lbl_title = Label(self.root, text="ADD REPORT DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img2=Image.open(r"images\royal-logo.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        img3=Image.open(r"images\bed.jpg")
        img3=img3.resize((520,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=426,y=55,width=720,height=200)


        # label frames
        lbl_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Add New Room", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_frame.place(x=0, y=50, width=425, height=490)

        # Floor
        lbl_floor = Label(lbl_frame, text="Floor", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()
        enty_floor = ttk.Entry(lbl_frame,textvariable=self.var_floor, width=29, font=("arial", 13, "bold"))
        enty_floor.grid(row=0, column=1)

        # Room No
        lbl_RoomNo = Label(lbl_frame, text="Room Number", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomNo=StringVar()
        enty_RoomNo = ttk.Entry(lbl_frame,textvariable=self.var_roomNo, width=29, font=("arial", 13, "bold"))
        enty_RoomNo.grid(row=1, column=1)

        # Room Type
        lbl_RoomType = Label(lbl_frame, text="Room Type", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomType=StringVar()
        enty_RoomType = ttk.Entry(lbl_frame,textvariable=self.var_roomType, width=29, font=("arial", 13, "bold"))
        enty_RoomType.grid(row=2, column=1)

        # buttonsframe
        btn_frame = Frame(lbl_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        # Buttons
        add = Button(btn_frame, text="ADD",command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        add.grid(row=0, column=0, padx=1)

        update = Button(btn_frame, text="UPDATE", command=self.update_now, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        update.grid(row=0, column=1, padx=1)

        clear = Button(btn_frame, text="CLEAR", command=self.deletem, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        clear.grid(row=0, column=2, padx=1)

        reset = Button(btn_frame, text="RESET",command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        reset.grid(row=0, column=3, padx=1)

        # tableframe
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=(
            "arial", 12, "bold"), padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        # scrollbars
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
  
        self.cust_dit_table = ttk.Treeview(table_frame, column=(
            "floor", "roomNo", "roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_dit_table.xview)
        scroll_y.config(command=self.cust_dit_table.yview)

        self.cust_dit_table.heading("floor", text="Floor")
        self.cust_dit_table.heading("roomNo", text="Room Number")
        self.cust_dit_table.heading("roomType", text="Room Type")

        self.cust_dit_table["show"] = "headings"

        self.cust_dit_table.column("floor",width=100)
        self.cust_dit_table.column("roomNo",width=100)
        self.cust_dit_table.column("roomType",width=100)

        self.cust_dit_table.pack(fill=BOTH, expand=1)
        self.cust_dit_table.bind("<ButtonRelease-1>", self.get_curser)
        self.fetch_data()
         
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_roomType.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Reported", "New Room Added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001", database="th300")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.cust_dit_table.delete(*self.cust_dit_table.get_children())
            for i in rows:
                self.cust_dit_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_curser(self, event=""):
        cursor_row = self.cust_dit_table.focus()
        content = self.cust_dit_table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2])
        
    def update_now(self):
        if self.var_roomNo.get() == "":
            messagebox.showerror(
                "Error", "Please enter floor number", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set floor=%s,roomType=%s where roomNo=%s", (
                self.var_floor.get(),
                self.var_roomType.get(),
                self.var_roomNo.get()
            ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo(
            "Updated", "Room details updated successfully", parent=self.root)

    def deletem(self):
        deletem = messagebox.askyesno(
            "Report Tab", "Do you want to delete this information", parent=self.root)
        if deletem > 0:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor = conn.cursor()
            query = "delete from details where roomNo=%s"
            value = (self.var_roomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not deletem:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomType.set(""),
        self.var_roomNo.set("")

    


if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()