from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1110x500+220+130")
        self.root.title("Storiso")
        self.root.config(bg="white")
        self.root.focus_force()
        #===============variable=================
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        

    #======================title============================
        lbl_title=Label(self.root,text="Manage Product Category",font=("Times new roman",30),bg="sky blue",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text=" Enter Category Name",font=("Times new roman",30),bg="white").place(x=50,y=100,)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Times new roman",18),bg="lightblue",fg="black").place(x=70,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("Times new roman",15),bg="#0f4d7d",fg="white",cursor="hand2").place(x=380,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Times new roman",15),bg="blue",fg="white",cursor="hand2").place(x=540,y=170,width=150,height=30)


#=======================category details=======================
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=70,width=380,height=430)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,columns=("Cid","Name"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.heading("Cid",text="C ID")
        self.categoryTable.heading("Name",text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("Cid",width=90)
        self.categoryTable.column("Name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
       

      #============image================
       
        self.im1=Image.open("image/cat2.jpg")
        self.im1=self.im1.resize((600,270))
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=70,y=220)

        self.show()
     def add(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name must be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category Name already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into category (Name)values(?)",( self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("success","category added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
     def show(self):
         con=sqlite3.connect(database=r'shu.db')
         cur=con.cursor()
         try:
             cur.execute("select * from category")
             rows=cur.fetchall()
             self.categoryTable.delete(*self.categoryTable.get_children())
             for row in rows:
                 self.categoryTable.insert('',END,values=row)
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

     def get_data(self,ev):
         f=self.categoryTable.focus()
         content=(self.categoryTable.item(f))
         row=content['values']
         #print(row)
         self.var_cat_id.set([0]),
         self.var_name.set(row[1])
     def delete(self):
         con=sqlite3.connect(database='shu.db')
         cur=con.cursor()
         try:
          if self.var_name.get()=="":
                messagebox.showerror("Error"," please select or enter category name ",parent=self.root)
          else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do u really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from category where name=? ",(self.var_name.get(),))
                      con.commit()
                      messagebox.showinfo("delete","category deleted succesfully",parent=self.root)
                    self.show()
                    self.var_cat_id.set(" ")
                    self.var_name.set(" ")
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
     
         


if __name__=="__main__":
  root=Tk()
  obj=categoryClass(root)
  root.mainloop()