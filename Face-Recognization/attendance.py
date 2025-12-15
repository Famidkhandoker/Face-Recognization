from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog




class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title(" Attendance System")
        self.myData = []

        # Define StringVars for each field at the start of your class
        self.var_attend_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        #------first image-----
        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_label1 = Label(self.root, image=self.photoimg)
        f_label1.place(x=0, y=0, width=800, height=200)

        #-------second image---------
        img1 = Image.open(r"college_images\bubt3.png")
        img1 = img1.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_label2 = Label(self.root, image=self.photoimg1)
        f_label2.place(x=800, y=0, width=800, height=200)

         # --------- Background Image ----------
        img3 = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\wp2551980.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text=" Attendance System",font=("times new roman", 35, "bold"),bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #-----------main frame-----------------
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)
        
        # --------- Left Label Frame ----------
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(r"college_images\face.jpeg")
        img_left = img_left.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        Left_inside_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_inside_frame.place(x=15, y=165, width=720, height=400)

        #----------labels and entries----------
        labels = ["Attendance ID:", "Roll:", "Name:", "Department:", "Time:", "Date:", "Attendance Status:"]
        vars_list = [self.var_attend_id, self.var_roll, self.var_name, self.var_dept, self.var_time, self.var_date, self.var_status]
        positions = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)]
        
        for (text, var, (row, col)) in zip(labels, vars_list, positions):
            lbl = Label(Left_inside_frame, text=text, font=("times new roman", 12, "bold"), bg="white")
            lbl.grid(row=row, column=col, padx=10, pady=5, sticky=W)
            entry = ttk.Entry(Left_inside_frame, textvariable=var, width=20, font=("times new roman", 12))
            entry.grid(row=row, column=col+1, padx=10, pady=5, sticky=W)

            combostatus = ttk.Combobox(Left_inside_frame, textvariable=self.var_status, font=("times new roman", 12,"bold"), state="readonly", width=18)
            combostatus["values"] = ("Status","Present", "Absent")
            combostatus.current(0)
            combostatus.grid(row=6, column=1, padx=10, pady=5, sticky=W)


        # Button Frames
        btn_frame = Frame(Left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=715, height=35)
        Button(btn_frame, text="Import cvs",command=self.importCsv,  width=17, font=("times new roman", 13, "bold"), bg="red", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export csv",command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="green", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="black", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0,column=3)   

        

        # --------- Right Frame ----------
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=680, height=580)

        
        

        #------table setup---------
        table_frame = Frame(right_frame, bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=5, y=1, width=660, height=550)


        #------------scroll bars------------
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendencereportTable = ttk.Treeview(
            table_frame,
            columns=("id","roll","name","department","time","date","attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # Attach scrollbars to table
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.AttendencereportTable.xview)
        scroll_y.config(command=self.AttendencereportTable.yview)

        # Headings & column sizes
        self.AttendencereportTable.heading("id", text="Attendance ID")
        self.AttendencereportTable.heading("roll", text="Roll")
        self.AttendencereportTable.heading("name", text="Name")
        self.AttendencereportTable.heading("department", text="Department")
        self.AttendencereportTable.heading("time", text="Time")
        self.AttendencereportTable.heading("date", text="Date")
        self.AttendencereportTable.heading("attendance", text="Status")

        self.AttendencereportTable["show"] = "headings"

        self.AttendencereportTable.column("id", width=100)
        self.AttendencereportTable.column("roll", width=100)
        self.AttendencereportTable.column("name", width=150)
        self.AttendencereportTable.column("department", width=100)
        self.AttendencereportTable.column("time", width=100)
        self.AttendencereportTable.column("date", width=100)
        self.AttendencereportTable.column("attendance", width=80)

        self.AttendencereportTable.pack(fill=BOTH, expand=1)
        
        self.AttendencereportTable.bind("<ButtonRelease>",self.get_cursor) 
    #-----------------------fetch data--------------------

    def fetchData(self,rows):
        self.AttendencereportTable.delete(*self.AttendencereportTable.get_children())
        for i in rows:
            self.AttendencereportTable.insert("",END,values=i)

    def importCsv(self):    
        self.myData=[]
        self.myData.clear()
        fIn=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("*csv File","*csv"),("All File","*.*")),parent=self.root)
        with open(fIn) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                self.myData.append(i)
            self.fetchData(self.myData) 
        
    def exportCsv(self):
        try:
            if len(self.myData) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fLn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),defaultextension=".csv", parent=self.root)
            if not fLn:  # Check if save dialog was cancelled
                return False
            with open(fLn, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for row in self.myData:
                    exp_write.writerow(row)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fLn) + " successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendencereportTable.focus()
        content=self.AttendencereportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dept.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])
    
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()