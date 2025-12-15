from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root, text="Train Data Set",font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #-----top img-----
        img_top = Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1530,325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=1530, height=325)
        
        #-------button-------
        b1_1 = Button(self.root, text="Train Data",command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)
        
        #------bottom img--------------
        img_bottom = Image.open(r"college_images/opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530,325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=440, width=1530, height=325)
        
    def train_classifier(self):
        data_dir = "data"

        # যদি ফোল্ডার খালি থাকে
        if not os.listdir(data_dir):
            messagebox.showerror("Error", "No images found in 'data' folder!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')  # grayscale
                imageNp = np.array(img, 'uint8')

                # filename: User.ID.ImageNo.jpg → index[1] = ID
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)

                cv2.imshow("Training the captured samples", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                print("Error loading image:", e)
                continue

        ids = np.array(ids)

        #--------------Train the classifier and save-------------
        clf = cv2.face.LBPHFaceRecognizer_create(
            radius=2,
            neighbors=10,
            grid_x=8,
            grid_y=8
        )

        clf.train(faces, ids)
        clf.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully!")

        
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

