from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1110x500+220+130")
        self.root.title("Storiso")
        self.root.config(bg="white")
        self.root.focus_force()
#all variables======================
        self.var_Searchby=StringVar()
        self.var_Searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
    #=====search==========================
        SearchFrame=LabelFrame(self.root,text="supplier",font=("Times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

#====option=======
        lbl_search=Label(SearchFrame,text="search by invoice no",font=("times new roman",15))
        lbl_search.place(x=20,y=20)
        

        txt_search=Entry(SearchFrame,textvariable=self.var_Searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=20)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",18),bg="#00B2EE",fg="black").place(x=410,y=20,width=150,height=30)

#======title======================================
        title=Label(self.root,text="Suppliers Details",font=("times new roman",18,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

#======content===============================================
              #========row1=========================
        lbl_sup_invoice=Label(self.root,text="Invoice no",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=150)
       
        txt_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=150,width=150)
        
#======row2==============================
        lbl_name=Label(self.root,text="supplier name",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=190,width=150)
        

#======row3==============================
        lbl_contact=Label(self.root,text="Contact",font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=200,y=230,width=150)
        
#============row4========================
        


#====================BUTTONS===============
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=620,y=270,width=100,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=740,y=270,width=100,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=860,y=270,width=100,height=30)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=980,y=270,width=100,height=30)

#=============student details=============
        supplier_frame=Frame(self.root,bd=3,relief=RIDGE)
        supplier_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(supplier_frame,orient=VERTICAL)
        scrollx=Scrollbar(supplier_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(supplier_frame,columns=("Invoice","Name","Contact"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        self.supplierTable.heading("Invoice",text="Invoice")
        self.supplierTable.heading("Name",text="Name")
        self.supplierTable.heading("Contact",text="Contact")
        
        self.supplierTable["show"]="headings"
        self.supplierTable.column("Invoice",width=90)
        self.supplierTable.column("Name",width=100)
        self.supplierTable.column("Contact",width=100)
        


        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#=============================================================================
     def add(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no already assigned,try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact)values(?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success","supplier added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     def show(self):
         con=sqlite3.connect(database=r'shu.db')
         cur=con.cursor()
         try:
             cur.execute("select * from supplier")
             rows=cur.fetchall()
             self.supplierTable.delete(*self.supplierTable.get_children())
             for row in rows:
                 self.supplierTable.insert('',END,values=row)
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         

     def get_data(self,ev):
         f=self.supplierTable.focus()
         content=(self.supplierTable.item(f))
         row=content['values']
         #print(row)
         self.var_sup_invoice.set(row[0]),
         self.var_name.set(row[1]),
         self.var_contact.set(row[2]),
         
#=======update=================================================
     def update(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no",parent=self.root)
                else:
                    cur.execute(" update supplier set Name=?,contact=? where invoice=?",(
                                
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_sup_invoice.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("success","supplier updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
      #=======delete========================================
     def delete(self):
         con=sqlite3.connect(database='shu.db')
         cur=con.cursor()
         try:
          if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","invoice no must be required",parent=self.root)
          else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid invoice no",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do u really want to delete?",parent=self.root)
                    if op==True:
                      cur.execute("delete from supplier where invoice=? ",(self.var_sup_invoice.get(),))
                      con.commit()
                      messagebox.showinfo("delete","supplier deleted succesfully",parent=self.root)
                      self.show()
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 #=============clear=====================================
     def clear(self):
       self.var_sup_invoice.set("")
       self.var_name.set("")
       self.var_contact.set("")
       self.var_Searchtxt.set("")
       self.show()   
     def search(self):
        con=sqlite3.connect(database=r'shu.db')
        cur=con.cursor()
        try:
            if self.var_Searchtxt.get()=="":
               messagebox.showerror("error","invoice no should be required",parent=self.root)
            else:
                 cur.execute("select * from supplier where invoice=?",(self.var_Searchtxt.get(),))
                 row=cur.fetchone()
                 if row!=None:
                  self.supplierTable.delete(*self.supplierTable.get_children())
                  
                  self.supplierTable.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
  root=Tk()
  obj=supplierClass(root)
  root.mainloop()
