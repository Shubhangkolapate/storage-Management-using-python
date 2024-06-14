from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
import email_pass
import smtplib
import time

class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1800x1500+0+0")
        self.root.config(bg="white")


        self.otp=''
#===========images==========================
        self.phone_image=PhotoImage(file="image/im8.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=20,y=120)

    #===============login frame================
        login_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="white")
        login_Frame.place(x=840,y=170,width=350,height=400)

#========title=========================
        self.student_pid=StringVar()
        self.password=StringVar()
        title=Label(login_Frame,text="Login System",font=("Elephant",20,"bold"),bg="white").place(x=0,y=0,relwidth=1)

        lbl_student_pid=Label(login_Frame,text="Admin Id",font=("times new roman",16),bg="white").place(x=50,y=75)
        
        txt_student_pid=Entry(login_Frame,textvariable=self.student_pid,font=("Andalus",12),bg="white").place(x=65,y=105,width=200)

        lbl_password=Label(login_Frame,text="Password",font=("tims new roman",15),bg="white").place(x=50,y=142)
        txt_password=Entry(login_Frame,textvariable=self.password,show="*",font=("Andalus",12),bg="white").place(x=65,y=170,width=200)

        btn_login=Button(login_Frame,text="LogIn",command=self.login,font=("Arial Rounded MT bold ",15,),bg="black",fg="white",activebackground="black",activeforeground="white",cursor="hand2").place(x=80,y=220,height=30,width=170)

        hr=Label(login_Frame,bg="black").place(x=70,y=280,width=200,height=2)
        or_=Label(login_Frame,text="OR",bg="white",font=("Andalus",8)).place(x=145,y=270,)

        btn_forget=Button(login_Frame,text="forget Password ?",command=self.forget_window,font=("Arial Rounded MT bold ",12,),bg="white",bd=0,fg="black",activebackground="white",activeforeground="white",cursor="hand2").place(x=100,y=300)

        lbl_regiter=Label(login_Frame,text="Welcome!!",font=("Andalus",18,"bold"),bg="white",fg="black").place(x=0,y=350,relwidth=1)
        
#=================animation of images=====================
        self.im1=ImageTk.PhotoImage(file="image/im3.png")
        self.im2=ImageTk.PhotoImage(file="image/im4.png")
        self.im3=ImageTk.PhotoImage(file="image/im5.png")
        self.im4=ImageTk.PhotoImage(file="image/im6.png")
        self.im5=ImageTk.PhotoImage(file="image/im7.png")
        self.im6=ImageTk.PhotoImage(file="image/im9.png")
        self.im7=ImageTk.PhotoImage(file="image/im10.png")
        self.im8=ImageTk.PhotoImage(file="image/im11.png")
        self.im9=ImageTk.PhotoImage(file="image/im12.png")
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=215,y=200,width=528,height=310)
        self.animation()
        

#=========================================================
    def animation(self):

        self.img4=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im4
        self.im4=self.im5
        self.im5=self.im6
        self.im6=self.im7
        self.im7=self.im8
        self.im8=self.im9
        self.im9=self.img4
        self.lbl_change_image.config(image=self.img4)
        self.lbl_change_image.after(2000,self.animation)
    def login(self):
        con=sqlite3.connect(database=r'shu.db')
        cur=con.cursor()
        try:
            if self.student_pid.get()=="" or self.password.get()=="":
                messagebox.showerror("error","All fields are required",parent=self.root)
            else:
                cur.execute("select Utype from student where pid= ? and password=?",(self.student_pid.get(),self.password.get(),))
                user=cur.fetchone()
                if user==NONE:
                    messagebox.showerror("error","invalid user name/password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    
    def forget_window(self):
        con=sqlite3.connect(database=r'shu.db')
        cur=con.cursor()
        try:
            if self.student_pid.get()=="":
                messagebox.showerror("error","Student pid must be required",parent=self.root)
            else:
                cur.execute("select email from student where pid=?",(self.student_pid.get(),))
                email=cur.fetchone()
                if email==NONE:
                    messagebox.showerror("error","Invalid student pid,please try again",parent=self.root)
                else: 
                    #==========forget window===========
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_confirm_pass=StringVar()
                    #all send_email_function()
                    chk=self.send_email(email[0])
                    if chk!='s':
                        messagebox.showerror("Error","Check your connections error,try again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="RESET PASSWORD",font=("times new roman",15,"bold"),bg="lightblue",fg="black").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP Sent on registered email",font=("times new roman",12)).place(x=20,y=60)
                        txt_rest=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",12),bg="lightyellow").place(x=20,y=85,width=250,height=30)
                    
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validation_otp,font=("times new roman",12),bg="blue",fg="black")
                        self.btn_reset.place(x=280,y=85,width=100,height=30)


                        lbl_new_password=Label(self.forget_win,text="New passowrd",font=("times new roman",12)).place(x=20,y=140)
                        txt_new_password=Entry(self.forget_win,textvariable=self.var_new_password,font=("times new roman",12),bg="lightyellow").place(x=20,y=175,width=250,height=30)
                    
                        lbl_confirm_pass=Label(self.forget_win,text="Confirm Your password",font=("times new roman",12)).place(x=20,y=205)
                        txt_confirm_pass=Entry(self.forget_win,textvariable=self.var_confirm_pass,font=("times new roman",12),bg="lightyellow").place(x=20,y=235,width=250,height=30)


                        self.btn_update=Button(self.forget_win,text="UPDATE",command=self.update_password,state=DISABLED,font=("times new roman",12),bg="lightblue",fg="black")
                        self.btn_update.place(x=165,y=273,width=100,height=30)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def update_password(self):
        if self.var_new_password.get()=="" or self.var_confirm_pass.get()=="":
            messagebox.showerror("error","password is required ",parent=self.forget_win)
        elif self.var_new_password.get()!= self.var_confirm_pass.get():
            messagebox.showerror("error","password and confirm password must be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'shu.db')
            cur=con.cursor()
            try:
                cur.execute("Update student SET password=? where pid=?",(self.var_confirm_pass.get(),self.student_pid.get()))
                con.commit()
                messagebox.showinfo("Sucess","Passsword UPDATED sucessfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
              messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




    def validation_otp(self):
        if str(self.otp)==str(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("error","Invalid OTP,Please try again",parent=self.forget_win)

    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email=email_pass.email
        pass_=email_pass.pass_

        s.login(email,pass_)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        print(self.otp)

        subj='shu-reset password OTP'
        msg=f'DearSir/Madam,\n\nYour reset OTP is {str(self.otp)}\n\nwith regards,\nshu'
        msg="subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'


if __name__=="__main__":
 root=Tk()
 obj=login_system(root)
 root.mainloop()
