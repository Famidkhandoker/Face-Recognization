from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Developers",font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images\dev.jpg")
        img_top = img_top.resize((1530,720), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_Label=Label(self.root, image=self.photoimg_top)
        f_Label.place(x=0, y=55, width=1530, height=720)

        #-----------main frame-----------------
        main_frame = Frame(f_Label, bd=2)
        main_frame.place(x=1010, y=0, width=500, height=600)

        

        #-----developer infos------------
        developer_label=Label(main_frame, text="Assalamu Alaikum !!!\nMy name is: \n \n Md Ryin Akand \nFamid Khandoker \n Mahathir Mohammad Rahim \n Nadira Naorin \n Sifath Hoassain", font=("times new roman", 13, "bold"), bg="white")
        developer_label.place(x=0,y=5)

        img_top2 = Image.open(r"college_images\b818e669-02fb-45bc-aa3d-d4730927f20e.jpeg")  # change path if needed
        img_top2 = img_top2.resize((230, 200), Image.Resampling.LANCZOS)
        photoimg_top2 = ImageTk.PhotoImage(img_top2)  # Use a local variable (or self. for classes)
        f_Label = Label(main_frame, image=photoimg_top2)
        f_Label.image = photoimg_top2  # Keep reference!
        f_Label.place(x=260, y=5, width=230, height=200)


        img_top3 = Image.open(r"college_images\5ediots.jpeg")
        img_top3 = img_top3.resize((500,390), Image.Resampling.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)
        f_Label=Label(main_frame, image=self.photoimg_top3)
        f_Label.place(x=0, y=160, width=500, height=440)
        

        





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()