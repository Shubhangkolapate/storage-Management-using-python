from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1110x500+220+130")
        self.root.title("Storiso")
        self.root.config(bg="white")
        self.root.focus_force()
        #================variables================
        self.var_invoice=StringVar()
        self.bill_list=[]

#======title===========================
        lbl_title=Label(self.root,text=" View Student Bills ",font=("Times new roman",30),bg="light blue",fg="black",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_invoice=Label(self.root,text="Invoice No",font=("times new roman",16),bg="white",fg="black").place(x=50,y=100)

        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("Times new roman",16),bg="white",fg="black").place(x=160,y=100,width=180,height=26)
        
        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",16,"bold"),bg="#2196f3",fg="black",cursor="hand2").place(x=350,y=100,width=120,height=26)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("times new roman",16,"bold"),bg="light blue",fg="black",cursor="hand2").place(x=480,y=100,width=120,height=26)

#================frame(bill list)================================
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)
        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        
        self.sales_list=Listbox(sales_Frame,font=("times new roman",16),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

#===============Bill Area==========================
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=410,height=330)
        lbl_title2=Label(bill_Frame,text=" Billing Area",font=("Times new roman",20),bg="blue").pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        
        self.bill_area=Text(bill_Frame,bg="lightyellow",yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

#===========IMAGE=======================
        self.bill_photo=Image.open("image/img1.jpg")
        self.bill_photo=self.bill_photo.resize((400,300))
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)
        
        lbl_image=Label(self.root,image=self.bill_photo,bg="white",bd=0)
        lbl_image.place(x=700,y=150)
        
        self.show()
#======================================
     def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        #print(os.listdir('../shu'))
        for i in os.listdir('bill'):
           #print(i.split('.'),i.split('.')[-1])
           if i.split('.')[-1]=='txt':
              self.sales_list.insert(END,i)
              self.bill_list.append(i.split('.')[0])

     def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
           self.bill_area.insert(END,i)
        fp.close()
     def search(self):
        if self.var_invoice.get()=="":
           messagebox.showerror("error","Invoice no. should be required",parent=self.root)
        else:
           if self.var_invoice.get() in self.bill_list:
              print("yes find the invoice")
              fp=open(f'bill/{self.var_invoice.get()}.txt','r')
              self.bill_area.delete('1.0',END)
              for i in fp:
                self.bill_area.insert(END,i)
              fp.close()
           else:
              messagebox.showerror("Error","Invalid invice no",parent=self.root)

     def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)




if __name__=="__main__":
  root=Tk()
  obj=salesClass(root)
  root.mainloop()