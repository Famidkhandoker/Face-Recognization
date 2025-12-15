from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk     #pip install pillow
from tkinter import messagebox


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")
  
        self.bg_image = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\login.jpeg")
        self.bg_image = self.bg_image.resize((1550, 800), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, width=1550, height=800)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_str.place(x=110,y=115)

        #------------Label----------
        username=lbl=Label(frame,text="username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #-----------icon images------------
        img2=Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)
        
        #--------------Buttons-------------
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red",command=self.login)
        loginbtn.place(x=110,y=300,width=120,height=35)


        btn=Button(frame,text="New User Register",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        btn.place(x=20,y=350,width=160)


        btn=Button(frame,text="Forget Password",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        btn.place(x=20,y=390,width=160)

    def login(self):
        if self.txtuser.get()==""   or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get() == "hydraryin@gmail.com" and self.txtpass.get() == "iloveyouammupubg":
            messagebox.showinfo("Succes","Welcome!! Access Granted")
        else:
            messagebox.showwarning("Invalid", "Access Denied!\n Username or Password wrong!")




if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()