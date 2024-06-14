from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1110x500+220+130")
        self.root.title("Storiso")
        self.root.config(bg="white")
        self.root.focus_force()
#======================variables===============================
        self.var_Searchby=StringVar()
        self.var_Searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.category_list=[]
        self.supplier_list=[]
        self.fetch_category_supplier()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
#===========frame================================        
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=500,height=480)

#============option===============
        


#========================================
        title=Label(product_Frame,text="Products Details",font=("times new roman",18,"bold"),bg="#6495ED",fg="white").pack(side=TOP,fill=X)

        lbl_category=Label(self.root,text="Category:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=103)
        lbl_supplier=Label(self.root,text="Supplier:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=145)
        lbl_name=Label(self.root,text="Name:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=195)
        lbl_price=Label(self.root,text="Price:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=250)
        lbl_qty=Label(self.root,text="Qty:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=300)
        lbl_status=Label(self.root,text="Status:",font=("times new roman",18,"bold"),bg="#FFFFFF").place(x=20,y=340)
        
        txt_category=Entry(self.root,textvariable=self.var_category,font=("times new roman",15,"bold"),bg="#FFFFFF")
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_category,values=self.category_list,state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_cat.place(x=130,y=101,width=180)
        cmb_cat.current(0)

        txt_supplier=Entry(self.root,textvariable=self.var_supplier,font=("times new roman",15,"bold"),bg="#FFFFFF")
        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_supplier,values=self.supplier_list,state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_sup.place(x=120,y=143,width=180)
        cmb_sup.current(0)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=130,y=200)
        txt_price=Entry(self.root,textvariable=self.var_price,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=130,y=250)
        txt_qty=Entry(self.root,textvariable=self.var_qty,font=("times new roman",15,"bold"),bg="#FFFFFF").place(x=130,y=300)

        txt_status=Entry(self.root,textvariable=self.var_status,font=("times new roman",15,"bold"),bg="#FFFFFF")
        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Select","Active","Unactive"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_status.place(x=130,y=330,width=180)
        cmb_status.current(0)

#=============buttons=======================
        btn_add=Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=15,y=430,width=110,height=28)
        btn_update=Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=130,y=430,width=100,height=30)
        btn_delete=Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=240,y=430,width=100,height=30)
        btn_clear=Button(product_Frame,text="clear",command=self.clear,font=("goudy old style",15),bg="#00B2EE",fg="black").place(x=350,y=430,width=100,height=30)
       
#=====================rightframe===================
        SearchFrame=LabelFrame(self.root,text="Search",font=("Times new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=510,y=8,width=600,height=80)

#====option=======
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("Select","category","supplier","name"),state="readonly",justify=CENTER,font=("times new roman",15))
        cmb_search.place(x=20,y=20,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_Searchtxt,font=("goudy old style",15),bg="light yellow").place(x=200,y=20)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",18),bg="#00B2EE",fg="black").place(x=410,y=20,width=150,height=30)

#=================================
        p_Frame=Frame(self.root,bd=3,relief=RIDGE)
        p_Frame.place(x=510,y=90,width=600,height=400)

        scrolly=Scrollbar(p_Frame,orient=VERTICAL)
        scrollx=Scrollbar(p_Frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(p_Frame,columns=("pid","category","supplier","name","price","qty","status"),xscrollcommand=scrollx.set) 
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        self.productTable.heading("pid",text="pid")
        self.productTable.heading("category",text="category")
        self.productTable.heading("supplier",text="supplier")
        self.productTable.heading("name",text="name")
        self.productTable.heading("price",text="price")
        self.productTable.heading("qty",text="qty")
        self.productTable.heading("status",text="status")
       
        self.productTable["show"]="headings"

        self.productTable.column("pid",width=90)
        self.productTable.column("category",width=100)
        self.productTable.column("supplier",width=100)
        self.productTable.column("name",width=90)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=100)
        self.productTable.column("status",width=100)
        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_category_supplier()

    #=============================================================================
     def fetch_category_supplier(self):
        self.category_list.append("empty")
        self.supplier_list.append("empty")
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            category=cur.fetchall()
            self.category_list.append("empty")
            self.supplier_list.append("empty")
            
            if len(category)>0:
                del self.category_list[:]
                self.category_list.append("select")
            for i in category:
                self.category_list.append(i[0])

            cur.execute("Select  name from supplier")
            supplier=cur.fetchall()
            if len(supplier)>0:
               del self.supplier_list[:]
                
               self.supplier_list.append("select")
               for i in supplier:
                  self.supplier_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 
     def add(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_category.get()=="select" or  self.var_category.get()=="empty"  or self.var_supplier.get()=="select" or self.var_supplier.get()=="empty"  or self.var_name.get()=="":
                messagebox.showerror("Error","All fields must be required",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","product already present,try different",parent=self.root)
                else:
                    cur.execute("Insert into product (category,supplier,name,price,qty,status)values(?,?,?,?,?,?)",(
                                        self.var_category.get(),
                                        self.var_supplier.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success","product added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     def show(self):
         con=sqlite3.connect(database=r'shu.db')
         cur=con.cursor()
         try:
             cur.execute("select * from product")
             rows=cur.fetchall()
             self.productTable.delete(*self.productTable.get_children())
             for row in rows:
                 self.productTable.insert('',END,values=row)
         except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
         

     def get_data(self,ev):
         f=self.productTable.focus()
         content=(self.productTable.item(f))
         row=content['values']
         #print(row)
         self.var_pid.set(row[0]),
         self.var_category.set(row[1]),
         self.var_supplier.set(row[2]),
         self.var_name.set(row[3]),
         self.var_price.set(row[4]),
         self.var_qty.set(row[5]),
         self.var_status.set(row[6]),
         
#=======update=================================================
     def update(self):
        con=sqlite3.connect(database='shu.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please  select product from list",parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parent=self.root)
                else:
                    cur.execute(" update product set category=?,supplier=?,price=?,qty=?,status=?  where name=?",(
                                
                                        self.var_category.get(),
                                        self.var_supplier.get(),
                                        
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_name.get(),
                                        

                    ))
                    con.commit()
                    messagebox.showinfo("success","product updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 
          #=======delete========================================
     def delete(self):
        con = sqlite3.connect(database='shu.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                 messagebox.showerror("Error", "Select product from list", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
            if row !=None:
                messagebox.showerror("Error", "Invalid product", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                if op == True:
                    cur.execute("DELETE FROM student WHERE name=?", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Product deleted successfully", parent=self.root)
                    self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)
        finally:
            con.close()

 #=============clear=====================================
     def clear(self):
       self.var_qty.set(" "),
       self.var_category.set("search"),
       self.var_supplier.set("search"),
       self.var_name.set(" "),
       self.var_price.set(" "),
       self.var_qty.set(" "),
       self.var_status.set("search"),
       self.var_Searchtxt.set(" ")
       self.var_Searchby.set("select")
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
                 cur.execute("select * from product where "+self.var_Searchby.get()+" LIKE '%"+self.var_Searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                  self.productTable.delete(*self.productTable.get_children())
                  for row in rows:
                   self.productTable.insert('',END,values=row)
                 else:
                     messagebox.showerror("Error","No record found!!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        



if __name__=="__main__":
  root=Tk()
  obj=productClass(root)
  root.mainloop()