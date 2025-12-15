from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========== variables =======
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # --------- Top Banner Images ----------
        img = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\1st.jpeg")
        img = img.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\haha.jpeg")
        img1 = img1.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\bubt1.jpeg")
        img2 = img2.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)

        # --------- Background Image ----------
        img3 = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\wp2551980.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text=" Attendance System",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # --------- Main Frame ----------
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        # --------- Left Label Frame ----------
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\face.jpeg")
        img_left = img_left.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        # ------Current Course information-------
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "CSE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "cse", "eee", "os", "architechture","algorithm","sdp")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white").grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2022-21", "2023-22", "2024-23", "2025-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white").grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # ------Class Student information-------
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # Labels & Entries
        labels = ["Student ID:", "Student Name:", "Class Division:", "Roll No:", "Gender:", "DOB:",
                  "Email:", "Phone No:", "Address:", "Teacher Name:"]
        vars_list = [self.var_std_id, self.var_std_name, self.var_div, self.var_roll, self.var_gender,
                     self.var_dob, self.var_email, self.var_phone, self.var_address, self.var_teacher]
        positions = [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2),(3,0),(3,2),(4,0),(4,2)]

        for i, label in enumerate(labels):
            row, col = positions[i]
            Label(class_student_frame, text=label, font=("times new roman", 13, "bold"), bg="white").grid(row=row, column=col, padx=10, pady=5, sticky=W)
            # For Division ComboBox
            if label == "Class Division:":
                div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
                div_combo["values"] = ("Select Division", "A", "B", "C", "D")
                div_combo.current(0)
                div_combo.grid(row=row, column=col+1, padx=10, pady=5, sticky=W)
            # For Gender ComboBox
            elif label == "Gender:":
                gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly", width=18)
                gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
                gender_combo.current(0)
                gender_combo.grid(row=row, column=col+1, padx=10, pady=5, sticky=W)
            # All others stay as Entry
            else:
                ttk.Entry(class_student_frame, textvariable=vars_list[i], width=20, font=("times new roman", 13, "bold")).grid(row=row, column=col+1, padx=10, pady=5, sticky=W)


        # Radio Buttons
        ttk.Radiobutton(class_student_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes").grid(row=5, column=0, padx=10, pady=5, sticky=W)
        ttk.Radiobutton(class_student_frame, text="No Photo Sample", variable=self.var_radio1, value="No").grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Button Frames
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=715, height=35)
        Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Delete",command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=235, width=715, height=35)
        Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)

        # --------- Right Frame ----------
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=780, y=10, width=660, height=580)

        img_right = Image.open(r"C:\Users\Famid Khandoker\Desktop\face_recognition_system\college_images\bubt3.png")
        img_right = img_right.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(right_frame, image=self.photoimg_right).place(x=5, y=0, width=720, height=130)

        #----search system----
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll-no", "Phone-No", "Semester-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Button(search_frame, text="Search", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=3, padx=1)
        Button(search_frame, text="Show All", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=4, padx=1)

        # --------- Table Setup ---------
        table_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=810, y=420, width=650, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email",
                     "phone", "address", "teacher", "photo"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # Column setup
        for col in ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"):
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #================= Function Declaration =================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@AllahuAkber1234",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO student
                    (Dep, Course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email,Phone, Address, Teacher, PhotoSample)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        try:
            update_confirmed = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if update_confirmed>0:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@AllahuAkber1234",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    UPDATE student SET
                        Dep=%s,
                        Course=%s,
                        Year=%s,
                        Semester=%s,
                        Name=%s,
                        Division=%s,
                        Roll=%s,
                        Gender=%s,
                        Dob=%s,
                        Email=%s,
                        Phone=%s,
                        Address=%s,
                        Teacher=%s,
                        PhotoSample=%s
                    WHERE Student_id=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
            else:
                if not update_confirmed:
                    return
            
            messagebox.showinfo("Success", "Student details successfully update complete", parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()
        
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


    def fetch_data(self):
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@AllahuAkber1234",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                rows = my_cursor.fetchall()
                if rows:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        # Fill entry fields with selected row values
        try:
            self.var_dep.set(row[0])
            self.var_course.set(row[1])
            self.var_year.set(row[2])
            self.var_semester.set(row[3])
            self.var_std_id.set(row[4])
            self.var_std_name.set(row[5])
            self.var_div.set(row[6])
            self.var_roll.set(row[7])
            self.var_gender.set(row[8])
            self.var_dob.set(row[9])
            self.var_email.set(row[10])
            self.var_phone.set(row[11])
            self.var_address.set(row[12])
            self.var_teacher.set(row[13])
            self.var_radio1.set(row[14])
        except IndexError:
            # If row is incomplete, don't fill all fields
            pass
    #----------delete function-------------
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be selected to delete.", parent=self.root)
        try:
            delete_confirmed = messagebox.askyesno("Delete", "Do you want to delete this student details?", parent=self.root)
            if delete_confirmed:
                  conn = mysql.connector.connect(
                 host="localhost",
                 username="root",
                 password="@AllahuAkber1234",
                 database="face_recognizer"
            )
            my_cursor = conn.cursor()
            sql = "DELETE FROM student WHERE Student_id=%s"
            my_cursor.execute(sql, (self.var_std_id.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details deleted successfully.", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
    #-----reset function-----
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
        #-------generate dataset or take photo samples-------------
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@AllahuAkber1234",
                database="face_recognizer"
                )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("""
                    UPDATE student SET
                        Dep=%s,
                        Course=%s,
                        Year=%s,
                        Semester=%s,
                        Name=%s,
                        Division=%s,
                        Roll=%s,
                        Gender=%s,
                        Dob=%s,
                        Email=%s,
                        Phone=%s,
                        Address=%s,
                        Teacher=%s,
                        PhotoSample=%s
                    WHERE Student_id=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1
                ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            
            #-----load predefined data on face frontals from opencv----------
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor=1.3
                #Minimum neighbor=5
                
                for (x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
            
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Crooped Face",face)
                
                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets completed!!!")                    
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)       

        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()