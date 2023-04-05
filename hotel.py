from tkinter import*
from PIL import Image,ImageTk
from customer import Cus_Win
from room import Roombooking
from report import Reporting 
from details import Details 
from log_wind import Cust_wind

    
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #===========1st img==============
        img1=Image.open(r"images\hotel2.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimage1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #===========logo================
        img2=Image.open(r"images\royal-logo.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimage2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #===============label============
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #==============main frame===========
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #============MENU===================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),fg="gold",bg="black",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #===========button frame===========
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=38,width=228,height=190)

        cus_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=20,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="gold",bg="black",cursor="hand1")
        cus_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=20,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="gold",bg="black",cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.detail,width=20,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="gold",bg="black",cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",command=self.reporting,width=20,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="gold",bg="black",cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout, width=20,font=("times new roman",14,"bold"),bd=0,relief=RIDGE,fg="gold",bg="black",cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #========right photo================
        img3=Image.open(r"images\hotel1.jpg")
        img3=img3.resize((1310,630),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimage3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=630)

        #=============down images==============
        img4=Image.open(r"images\gst-food.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg1=Label(main_frame,image=self.photoimage4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"images\food.jpg")
        img5=img5.resize((230,200),Image.ANTIALIAS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        lblimg1=Label(main_frame,image=self.photoimage5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=200)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cus_Win(self.new_window)   


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def reporting(self):
        self.new_window=Toplevel(self.root)
        self.app=Reporting(self.new_window)

    def detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)

    def logout(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_wind(self.new_window)




if __name__=="__main__":
    root=Tk()
    app=HotelManagementSystem(root)
    root.mainloop()