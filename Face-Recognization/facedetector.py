from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from datetime import datetime
import threading

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_left = Image.open(r"college_images/face_detector1.jpg")
        img_left = img_left.resize((650,700), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(self.root, image=self.photoimg_left).place(x=0, y=55, width=650, height=700)
        
        img_right = Image.open(r"college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right = img_right.resize((950,700), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        self.img_right_label = Label(self.root, image=self.photoimg_right)
        self.img_right_label.place(x=650, y=55, width=950, height=700)

        Button(self.img_right_label, text="Face Recognition", command=self.start_face_recognition,
               cursor="hand2", font=("times new roman", 18, "bold"), bg="dark green", fg="white").place(x=365, y=620, width=200, height=40)

    def mark_attendence(self, i, r, n, d):
        with open("ryinfamidrahimsifathnaorin.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            found = False
            for line in myDataList:
                entry = line.strip().split(",")[:4]
                if entry == [str(i), r, n, d]:
                    found = True
                    break
            if not found:
                now = datetime.now()
                d1 = now.strftime("%d-%m-%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},present")

    def start_face_recognition(self):
        threading.Thread(target=self.Face_Recognition, daemon=True).start()

    def Face_Recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        
            coord=[]
        
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])

                # Fixed confidence calculation
                confidence = int(100 * (1 - predict / 400))
                
                # Fetch student info from database
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",        # <-- fixed user
                        password="@AllahuAkber1234",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name from student where student_id=%s", (id,))
                    n = my_cursor.fetchone()
                    n = n[0] if n else "Unknown"
                    
                    my_cursor.execute("select Roll from student where student_id=%s", (id,))
                    r = my_cursor.fetchone()
                    r = r[0] if r else "Unknown"
                    
                    my_cursor.execute("select Dep from student where student_id=%s", (id,))
                    d = my_cursor.fetchone()
                    d = d[0] if d else "Unknown"
                    conn.close()
                      
                except Exception as e:
                    print(f"DB error: {e}")
                    n = r = d = "Unknown"

                # Display recognized face info if confidence > 77
                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendence(id, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



