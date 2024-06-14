from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1110x500+220+130")
        self.root.title("Storiso")
        self.root.config(bg="white")
        self.root.focus_force()
#all variables======================
        self.var_Searchby=StringVar()
        self.var_Searchtxt=StringVar()
        
        self.var_student_name=StringVar()
        self.var_student_pid=StringVar()
        self.var_email=StringVar()
        self.var_Branch=StringVar()
        self.var_contact=StringVar()
        self.var_DOB=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_gender=StringVar()
        self.var_supplier=StringVar()

    #=====search==========================
        SearchFrame=LabelFrame(self.root,text="Search student",font=("Times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

#====option=======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("Select","Email","Name","StudentPID","Branch"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=20,y=20,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_Searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=20)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",18),bg="#00B2EE",fg="black").place(x=410,y=20,width=150,height=30)

#======title======================================
        title=Label(self.root,text="Student Details",font=("times new roman",18,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

#======content===============================================
        lbl_student_name=Label(self.root,text="Student Name",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=400,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=750,y=150)

        txt_student_name=Entry(self.root,textvariable=self.var_student_name,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=150,width=150)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=500,y=150,width=150)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=850,y=150,width=150)
#========row1=========================
        lbl_student_name=Label(self.root,text="Student Name",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=400,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=750,y=150)

        txt_student_name=Entry(self.root,textvariable=self.var_student_name,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=150,width=150)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=500,y=150,width=150)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=850,y=150,width=150)

#======row2==============================
        lbl_student_pid=Label(self.root,text="Student PID",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=190)
        lbl_DOB=Label(self.root,text="DOB",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=400,y=190)
        lbl_email=Label(self.root,text="Email",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=750,y=190)

        txt_student_pid=Entry(self.root,textvariable=self.var_student_pid,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=190,width=150)
        txt_DOB=Entry(self.root,textvariable=self.var_DOB,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=500,y=190,width=180)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=850,y=190,width=150)


#======row3==============================
        lbl_Branch=Label(self.root,text="Branch",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=230)
        lbl_utype=Label(self.root,text="User type",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=400,y=230)
        lbl_passdword=Label(self.root,text="Password",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=750,y=230)

        txt_Branch=Entry(self.root,textvariable=self.var_Branch,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=230,width=150)
        txt_utype=Entry(self.root,textvariable=self.var_utype,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","student"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=500,y=230,width=180)
        cmb_utype.current(0)
        txt_password=Entry(self.root,textvariable=self.var_password,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=850,y=230,width=150)

        lbl_supplier=Label(self.root,text="Supplier",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=270)
        txt_supplier=Entry(self.root,textvariable=self.var_supplier,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=270,width=150)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_supplier,values=("Select","rakesh","bronil","anish"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_utype.place(x=200,y=270,width=180)
        cmb_utype.current(0)

#====================BUTTONS===============
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=50,y=310,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=400,y=270,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=750,y=270,width=100,height=30)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=980,y=270,width=100,height=30)

#=============student details=============
        student_frame=Frame(self.root,bd=3,relief=RIDGE)
        student_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(student_frame,orient=VERTICAL)
        scrollx=Scrollbar(student_frame,orient=HORIZONTAL)

        self.studentTable=ttk.Treeview(student_frame,columns=("Pid","Name","Branch","Email","Utype","DOB","contact","password","gender"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)
        self.studentTable.heading("Pid",text="Pid")
        self.studentTable.heading("Name",text="Name")
        self.studentTable.heading("Branch",text="Branch")
        self.studentTable.heading("Email",text="Email")
        self.studentTable.heading("Utype",text="Utype")
        self.studentTable.heading("DOB",text="DOB")
        self.studentTable.heading("contact",text="contact")
        self.studentTable.heading("password",text="password")
        self.studentTable.heading("gender",text="gender")
        self.studentTable["show"]="headings"
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#=============================================================================
     def add(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_student_name.get()=="":
                messagebox.showerror("Error","Student ID must be required",parent=self.root)
            else:
                cur.execute("Select * from student where pid=?",(self.var_student_pid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This is student Name already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into student (Pid,Name,Branch,Email,Utype,DOB,contact,password,gender)values(?,?,?,?,?,?,?,?,?)",(
                                        self.var_student_pid.get(),
                                        self.var_student_name.get(),
                                        self.var_Branch.get(),
                                        self.var_email.get(),
                                        self.var_utype.get(),
                                        self.var_DOB.get(),
                                        self.var_contact.get(),
                                        self.var_password.get(),
                                        self.var_gender.get(),


                    ))
                    con.commit()
                    messagebox.showinfo("success","student added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     def show(self):
         con=sqlite3.connect(database=r'shu.db')
         cur=con.cursor()
         try:
             cur.execute("select * from student")
             rows=cur.fetchall()
             self.studentTable.delete(*self.studentTable.get_children())
             for row in rows:
                 self.studentTable.insert('',END,values=row)
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         

     def get_data(self,ev):
         f=self.studentTable.focus()
         content=(self.studentTable.item(f))
         row=content['values']
         #print(row)
         self.var_student_pid.set(row[0]),
         self.var_student_name.set(row[1]),
         self.var_Branch.set(row[2]),
         self.var_email.set(row[3]),
         self.var_utype.set(row[4]),
         self.var_DOB.set(row[5]),
         self.var_contact.set(row[6]),
         self.var_password.set(row[7]),
         self.var_gender.set(row[8]),
#=======update=================================================
     def update(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_student_pid.get()=="":
                messagebox.showerror("Error","Student ID must be required",parent=self.root)
            else:
                cur.execute("Select * from student where pid=?",(self.var_student_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid student pid",parent=self.root)
                else:
                    cur.execute(" update student set Name=?,Branch=?,Email=?,Utype=?,DOB=?,contact=?,password=?,gender=?  where pid=?",(
                                
                                        self.var_student_name.get(),
                                        self.var_Branch.get(),
                                        self.var_email.get(),
                                        self.var_utype.get(),
                                        self.var_DOB.get(),
                                        self.var_contact.get(),
                                        self.var_password.get(),
                                        self.var_gender.get(),
                                        self.var_student_pid.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("success","student updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
      #=======delete========================================
     def delete(self):
         con=sqlite3.connect(database='shu.db')
         cur=con.cursor()
         try:
          if self.var_student_name.get()=="":
                messagebox.showerror("Error","Student ID must be required",parent=self.root)
          else:
                cur.execute("Select * from student where pid=?",(self.var_student_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invalid student pid",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do u really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from student where pid=? ",(self.var_student_pid.get(),))
                      con.commit()
                      messagebox.showinfo("delete","student deleted succesfully",parent=self.root)
                    self.show()
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 #=============clear=====================================
     def clear(self):
       self.var_student_pid.set(""),
       self.var_student_name.set(""),
       self.var_Branch.set(""),
       self.var_email.set(""),
       self.var_utype.set("Search"),
       self.var_DOB.set(""),
       self.var_contact.set(""),
       self.var_password.set(""),
       self.var_gender.set("Search"),     
       self.show()    
     def search(self):
        con=sqlite3.connect(database=r'shu.db')
        cur=con.cursor()
        try:
             if self.var_Searchby.get()=="select":
               messagebox.showerror("error","select search by option",parent=self.root)
             elif self.var_Searchtxt.get()=="":
               messagebox.showerror("error","select search input should be required",parent=self.root)
             else:
                 cur.execute("select * from student where "+self.var_Searchby.get()+" LIKE '%"+self.var_Searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                  self.studentTable.delete(*self.studentTable.get_children())
                  for row in rows:
                   self.studentTable.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
  root=Tk()
  obj=studentClass(root)
  root.mainloop()
