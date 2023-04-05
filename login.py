from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        
        self.bg=ImageTk.PhotoImage(file=r"images\SDT_Zoom-Backgrounds_April-8_Windansea-1_1600x800.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        
        #============Login image================
        
        img1=Image.open(r"C:\Users\ompat\OneDrive\Desktop\project\images\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)


        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon images

        img2=Image.open(r"C:\Users\ompat\OneDrive\Desktop\project\images\login.png")
        img2=img2.resize((27,27),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=27,height=27)

        img3=Image.open(r"C:\Users\ompat\OneDrive\Desktop\project\images\password.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        
        #LoginButton
        loginbtn=Button(frame,command=self.login ,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#488bc4",activeforeground="white",activebackground="#488bc4")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #RegisterButton
        registerbtn=Button(frame,text="New User Regitration",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=17,y=350,width=160)

        #ForgatpassButton
        forgotpassbtn=Button(frame,text="Forgot Password?",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=9,y=370,width=160)
    

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" and self.txtpass.get()=="":
           messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="OmPatil" or "Sakshi" and self.txtpass.get()=="1234":
           messagebox.showinfo("Success","Welcome to Hotel Management System")
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register2 where email=%s and password=%s",(
                                                                                        self.var_email.get(),
                                                                                        self.var_password.get()
                                                                                       ))

            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid Username And Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter The Valid Email Address To Reset The Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor=conn.cursor()
            query=("select * from register2 where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        
        #===========variables=============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()


       #===========bg image=============
        self.bg=ImageTk.PhotoImage(file=r"images\SDT_Zoom-Backgrounds_April-8_Windansea-1_1600x800.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

      #=============left image=============
        self.bg1=ImageTk.PhotoImage(file=r"images\register-left.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        
        #==============================ROW AND LABEL============================================

        #====row 1=======
        fname=Label(frame,text="FIRST NAME",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,     font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="LAST NAME",font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #====row 2======
        contact=Label(frame,text="CONTACT NO.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
       
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="EMAIL ID",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)
       
        self.txt_EMAIL=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_EMAIL.place(x=370,y=200,width=250)

        #---------ROW 3-----------
        security_Q=Label(frame,text="SELECT SECURITY QUESTION",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("SELECT","YOUR BIRTHPLACE","YOUR GIRLFRIEND NAME","YOUR PET NAME")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="SECURITY ANSWER",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #------------ROW 4------------
        password=Label(frame,text="ENTER YOUR PASSWORD",font=("times new roman",15,"bold"),bg="white")
        password.place(x=50,y=310)
       
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        confirm_password=Label(frame,text="CONFIRM PASSWORD",font=("times new roman",15,"bold"),bg="white")
        confirm_password.place(x=370,y=310)
       
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15))
        self.txt_confirm_password.place(x=370,y=340,width=250)


        #===================Checkbox======================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("areial",12,"bold"),bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #===================button=======================
        img=Image.open(r"images\register-now.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=50,y=420,width=200)


        img1=Image.open(r"images\login-now.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        b1.place(x=370,y=420,width=200)

    
    #===========Function Declaration================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="SELECT" or self.var_security_A.get()=="" or self.var_password.get()=="" or self.var_confirm_password.get()=="" :
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password And Confirm Password Should be Same")
        elif self.var_check.get()==0:
            messagebox.showerror("Erro","Please Select Our Term & Conditions")
        else :
            conn=mysql.connector.connect(host="localhost",user="root",password="Sonu@2001",database="th300")
            my_cursor=conn.cursor()
            query=("select * from register2 where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist . Please Try Another Email")
            else:
                my_cursor.execute("insert into register2 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_security_Q.get(),
                                                                                        self.var_security_A.get(),
                                                                                        self.var_password.get()
                                                                                        
                                                                                        ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","You have been Registered Successfully")






if __name__ == "__main__":
    main()
