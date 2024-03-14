from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
    
        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()


        #bg image
        img_4 = Image.open(r"images\bg.jpg")
        img_4 = img_4.resize((1280,720),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=0,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1280,height=720)

        #title
        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("Fixedsys",40,),fg ="grey",bg = "#f5f7fa")
        lbl_title.place(x=0,y=0,width=1280,height = 100)
       
       
        #left frame
        DataLeftFrame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("Fixedsys",10),fg="black",bg="#f5f7fa")
        DataLeftFrame.place(x=30,y=120,width=530,height=550)

        #left image
        img_5 = Image.open(r"images\student.jpg")
        img_5 = img_5.resize((530,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(DataLeftFrame,image=self.photoimg_5,bd=0,relief=RIDGE)
        my_img.place(x=0,y=0,width=520,height=120)

        #Course information LabelFrame 
        std_infoframe=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Course Information",font=("Fixedsys",10),fg="black",bg="#f5f7fa")
        std_infoframe.place(x=0,y=120,width=520,height=120)

        #Labels and combobox
        #department
        lbl_dep=Label(std_infoframe,text = "Department",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_dep.grid(row=0,column=0,padx=7,pady=15,sticky=W)

        combo_dep=ttk.Combobox(std_infoframe,textvariable=self.var_dep,font=("Fixedsys",6),width=20,state="readonly")
        combo_dep["value"]=("Select department","Computer and Electronics","Civil","Mechanical","Chemical","Architecture")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        #Year
        lbl_year=Label(std_infoframe,text = "Year",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_year.grid(row=0,column=2,padx=2,sticky=W)

        combo_year=ttk.Combobox(std_infoframe,textvariable=self.var_year,font=("Fixedsys",6),width=15,state="readonly")
        combo_year["value"]=("Select Year","I","II","III","IV","V")
        combo_year.current(0)
        combo_year.grid(row=0,column=3,padx=2,pady=2,sticky=W)

        #Semester
        lbl_semester=Label(std_infoframe, text = "Semester",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_semester.grid(row=1,column=0,padx=7,sticky=W)

        combo_semester=ttk.Combobox(std_infoframe,textvariable=self.var_semester,font=("Fixedsys",6),width=20,state="readonly")
        combo_semester["value"]=("Select Semester","I","II")
        combo_semester.current(0)
        combo_semester.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        #Course
        lbl_course=Label(std_infoframe,text = "Course",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_course.grid(row=1,column=2,padx=2,sticky=W)

        combo_course=ttk.Combobox(std_infoframe,textvariable=self.var_course,font=("Fixedsys",6),width=15,state="readonly")
        combo_course["value"]=("Select Course","BE","MSc")
        combo_course.current(0)
        combo_course.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        #Details entry frame
        std_detailsframe=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Details Entry",font=("Fixedsys",10),fg="black",bg="#f5f7fa")
        std_detailsframe.place(x=0,y=240,width=520,height=290)

        #ID
        lbl_id=Label(std_detailsframe,text = "Student-ID:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_id.grid(row=0,column=0,padx=1,pady=10,sticky=W)

        id_entry=ttk.Entry(std_detailsframe,textvariable=self.var_id,font=("Fixedsys",6),width= 20)
        id_entry.grid(row=0,column=1,padx=2,sticky=W)

        #NAME
        lbl_name=Label(std_detailsframe,text = "Name:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_name.grid(row=0,column=2,padx=1,pady=10,sticky=W)

        txt_name=ttk.Entry(std_detailsframe,textvariable=self.var_name,font=("Fixedsys",6),width= 20)
        txt_name.grid(row=0,column=3,padx=2,sticky=W)

        #DIVISION
        lbl_div=Label(std_detailsframe,text = "Division:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_div.grid(row=1,column=0,padx=1,pady=10,sticky=W)

        
        combo_txt_div=ttk.Combobox(std_detailsframe,textvariable=self.var_div,font=("Fixedsys",6),width=18,state="readonly")
        combo_txt_div["value"]=("Select Division","A","B","C")
        combo_txt_div.current(0)
        combo_txt_div.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        #ROLL
        lbl_roll=Label(std_detailsframe,text = "Roll no:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_roll.grid(row=1,column=2,padx=1,pady=10,sticky=W)
        txt_roll=ttk.Entry(std_detailsframe,textvariable=self.var_roll,font=("Fixedsys",6),width= 20)
        txt_roll.grid(row=1,column=3,padx=2,sticky=W)

        #gender
        lbl_gender=Label(std_detailsframe,text = "Gender:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_gender.grid(row=2,column=0,padx=1,pady=10,sticky=W)

        
        combo_txt_gender=ttk.Combobox(std_detailsframe,textvariable=self.var_gender,font=("Fixedsys",6),width=18,state="readonly")
        combo_txt_gender["value"]=("Select Gender","Male","Female","Other")
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=2,column=1,padx=2,pady=2,sticky=W)

        #DOB
        lbl_dob=Label(std_detailsframe,text = "DOB:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_dob.grid(row=2,column=2,padx=1,pady=10,sticky=W)
        txt_dob=ttk.Entry(std_detailsframe,textvariable=self.var_dob,font=("Fixedsys",6),width= 20)
        txt_dob.grid(row=2,column=3,padx=2,sticky=W)

        #EMAIL
        lbl_email=Label(std_detailsframe,text = "Email:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_email.grid(row=3,column=0,padx=1,pady=10,sticky=W)
        txt_email=ttk.Entry(std_detailsframe,textvariable=self.var_email,font=("Fixedsys",6),width= 20)
        txt_email.grid(row=3,column=1,padx=2,sticky=W)

        #PHONE
        lbl_phone=Label(std_detailsframe,text = "Phone:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_phone.grid(row=3,column=2,padx=1,pady=10,sticky=W)
        txt_phone=ttk.Entry(std_detailsframe,textvariable=self.var_phone,font=("Fixedsys",6),width= 20)
        txt_phone.grid(row=3,column=3,padx=2,sticky=W)

        #ADDRESS
        lbl_address=Label(std_detailsframe,text = "Address:",font=("Fixedsys",6),fg="black",bg="#f5f7fa")
        lbl_address.grid(row=4,column=0,padx=1,pady=10,sticky=W)
        txt_address=ttk.Entry(std_detailsframe,textvariable=self.var_address,font=("Fixedsys",6),width= 20)
        txt_address.grid(row=4,column=1,padx=2,sticky=W)

        #button frame
        btn_frame=Frame(DataLeftFrame,bd=4,relief=RIDGE,bg="#f5f7fa")
        btn_frame.place(x=0,y=455,width=520,height=75)
        
        #add buttons
        btn_add=Button(btn_frame,text="SAVE",command =self.add_data,font=("Fixedsys",15),width=12,height=2,bg="blue",fg="white")
        btn_add.grid(row=0,column=0,padx = 10,pady=15)

        btn_delete=Button(btn_frame,text="DELETE",command=self.delete_data,font=("Fixedsys",15),width=12,height=2,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx = 10,pady=15)

        btn_reset=Button(btn_frame,text="RESET",command =self.reset_data,font=("Fixedsys",15),width=12,height=2,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx = 10,pady=15)

        btn_update=Button(btn_frame,text="UPDATE",command = self.update_data,font=("Fixedsys",15),width=12,height=2,bg="blue",fg="white")
        btn_update.grid(row=0,column=4,padx = 10,pady=15)

        #right frame
        DataRightFrame=LabelFrame(bg_lbl,bd=4,relief=RIDGE,padx=2,text="Student Database",font=("Fixedsys",12),fg="Black",bg="#f5f7fa")
        DataRightFrame.place(x=570,y=120,width=700,height=550)

        #right image
        img_6 = Image.open(r"images\records.png")
        img_6 = img_6.resize((530,120),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img=Label(DataRightFrame,image=self.photoimg_6,bd=0,relief=RIDGE)
        my_img.place(x=85,y=0,width=520,height=120)

        #right frame
        searchFrame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="View information",font=("Fixedsys",12),fg="Black",bg="#f5f7fa")
        searchFrame.place(x=0,y=120,width=690,height=55)

        #search by
        search_by=Label(searchFrame,text = "SEARCH BY",font=("Fixedsys",6),fg="WHITE",bg="BLACK")
        search_by.grid(row=0,column=0,padx=1,pady=3,sticky=W)

        self.var_comsearch=StringVar()
        combo_txt_search=ttk.Combobox(searchFrame,textvariable=self.var_comsearch,font=("Fixedsys",6),width=18,state="readonly")
        combo_txt_search["value"]=("Select Option","Roll","Phone","StudentID")
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0,column=1,padx=10,pady=2,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(searchFrame,textvariable=self.var_search,font=("Fixedsys",6),width= 20)
        txt_search.grid(row=0,column=2,padx=2,sticky=W)

        btn_search=Button(searchFrame,command=self.search_data,text="SEARCH",font=("Fixedsys",15),width=10,height=1,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx = 5,pady=3,sticky=W)

        btn_showall=Button(searchFrame,text="SHOW ALL",command=self.fetch_data,font=("Fixedsys",15),width=10,height=1,bg="blue",fg="white")
        btn_showall.grid(row=0,column=4,padx = 1,pady=3,sticky=W)

        #*********************TABLE AND SCROLL BAR*************************************

        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=176,width = 690, height = 350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","semester","id","name","div","roll","gender","dob","email","phone","address",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=150)
        self.student_table.column("course",  width=50)
        self.student_table.column("year",   width=50)
        self.student_table.column("semester",width=50)
        self.student_table.column("id",  width=50)
        self.student_table.column("name", width=100)
        self.student_table.column("div",width=50)
        self.student_table.column("roll",width=50)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=200)
        self.student_table.column("address",width=200)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        
    def add_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_id.get()==""):
             messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="jas")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_id.get(),
                                    self.var_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get()
            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)  
  
    # fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="jas")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close()    


    #GET Cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        
    #UPDATE DATA
    def update_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_id.get()==""):
             messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="jas")
                    my_cursor=conn.cursor()     
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s where studentID=%s",(
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),                                                                            
                                    self.var_id.get()       
                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Successfully updated", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)                


    #DELETE
    def delete_data(self):
        if self.var_id.get=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure?")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="jas")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    value=(self.var_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Delete Successful",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)


    #RESET
    def reset_data(self):

        self.var_dep.set("Select department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_semester.set("Select semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select division")
        self.var_roll.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")

    #SEARCH
    def search_data(self):
        if self.var_comsearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="jas")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student where "+str(self.var_comsearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}", parent=self.root)        
















if __name__  == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()



