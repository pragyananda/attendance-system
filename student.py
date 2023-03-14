from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import*
import time
import os




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("attendence system")
        self.root.config(background='#eff5f6')


        self.header =Frame(self.root ,bg='#009df4')
        self.header.place(x=350 ,y=0,width=1250,height=60)
        self.logout_text = Button(self.header,text='Logout',bg='#32cfBe',font=("",13,"bold",),bd=0,fg='white',
        cursor='hand2',activebackground='#32cfBe',borderwidth=3)
        self.logout_text.place(x=1080,y=15)

        self.sidebar =Frame(self.root ,bg='#ffffff')
        self.sidebar.place(x=0,y=0,width=350,height=800)

        self.heading = Label(self.root,text='Dashboard',font=("",13,"bold"),fg='#0064d3',bg='#eff5f6')
        self.heading.place(x=380,y=70)

        
        icon =Image.open(r"images\th copy.png")
        icon = icon.resize((150, 120), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(icon)
        self.logo= Button(self.sidebar,image=photo,bg='#ffffff',cursor='hand2',bd=0)
        self.logo.image=photo
        self.logo.place(x=100,y=70)

        self.admin =Label(self.sidebar,text='Dsvv Admin',bg='#ffffff',font=("",15,"bold"))
        self.admin.place(x=115,y=190)

        dashicon =Image.open(r"images\student.jpg")
        dashicon = dashicon.resize((30, 30), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(dashicon)
        self.dash= Button(self.sidebar,image=photo,bg='#ffffff',cursor='hand2',bd=0)
        self.dash.image=photo
        self.dash.place(x=50,y=289)
        self.student_regist =Button(self.sidebar,text='Student Registration',activebackground='#ffffff',font=("",15,"bold"),cursor='hand2',bg='#ffffff',bd=0)
        self.student_regist.place(x=100,y=290)

        trainicon =Image.open(r"images\train.jpg")
        trainicon = trainicon.resize((30, 30), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(trainicon)
        self.dashtrain= Button(self.sidebar,image=photo,bg='#ffffff',cursor='hand2',bd=0)
        self.dashtrain.image=photo
        self.dashtrain.place(x=50,y=349)
        self.student_regist =Button(self.sidebar,text='Train',activebackground='#ffffff',font=("",15,"bold"),cursor='hand2',bg='#ffffff',bd=0)
        self.student_regist.place(x=100,y=350)


        atticon =Image.open(r"images\att.jpg")
        atticon = atticon.resize((30, 30), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(atticon)
        self.dashatt=Button(self.sidebar,image=photo,bg='#ffffff',cursor='hand2',bd=0)
        self.dashatt.image=photo
        self.dashatt.place(x=50,y=409)
        self.student_regist =Button(self.sidebar,text='Attendence',activebackground='#ffffff',font=("",15,"bold"),cursor='hand2',bg='#ffffff',bd=0)
        self.student_regist.place(x=100,y=410)
        

        exiticon =Image.open(r"images\exit.jpg")
        exiticon = exiticon.resize((30, 30), Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(exiticon)
        self.exit= Button(self.sidebar,image=photo,bg='#ffffff',cursor='hand2',bd=0)
        self.exit.image=photo
        self.exit.place(x=50,y=469)
        self.student_regist =Button(self.sidebar,text='Exit',activebackground='#ffffff',font=("",15,"bold"),cursor='hand2',bg='#ffffff',bd=0)
        self.student_regist.place(x=100,y=470)

        main_frame=Frame(bg='#ffffff',bd=2)
        main_frame.place(x=380,y=110,width=1120,height=650)

        innerleftframe=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Datails',font=("",12,"bold"))
        innerleftframe.place(x=10,y=10,width=500,height=500)

        leftcourse=LabelFrame(innerleftframe,bd=2,bg='white',relief=RIDGE,text='current course',font=("",12,"bold"))
        leftcourse.place(x=5,y=10,width=490,height=150)

        deptlable=Label(leftcourse,text='Department',font=("",12,"bold"),padx=10,bg='white')
        deptlable.grid(row=0,column=0,sticky=W)
        deptcombo=ttk.Combobox(leftcourse,font=("",12,"bold"),width=12,state="readonly")
        deptcombo['values']=("department",'MCA','JMC','BCA')
        deptcombo.current(0)
        deptcombo.grid(row=0,column=1,padx=2,pady=10)

        semlabel=Label(leftcourse,text='Degree',font=("",12,"bold"),padx=10,bg='white')
        semlabel.grid(row=0,column=2,sticky=W)
        semcombo=ttk.Combobox(leftcourse,font=("",12,"bold"),width=12,state="readonly")
        semcombo['values']=("Degree",'Graduation','Master','Certificate')
        semcombo.current(0)
        semcombo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        yearlabel=Label(leftcourse,text='Year',font=("",12,"bold"),padx=10,bg='white')
        yearlabel.grid(row=1,column=0,sticky=W)
        yearcombo=ttk.Combobox(leftcourse,font=("",12,"bold"),width=12,state="readonly")
        yearcombo['values']=("Year",'2021','2022','2023')
        yearcombo.current(0)
        yearcombo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        semlabel=Label(leftcourse,text='Semester',font=("",12,"bold"),padx=10,bg='white')
        semlabel.grid(row=1,column=2,sticky=W)
        semcombo=ttk.Combobox(leftcourse,font=("",12,"bold"),width=12,state="readonly")
        semcombo['values']=("Semester",'First','Secoend','Third','Fourth')
        semcombo.current(0)
        semcombo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        studentinfo=LabelFrame(innerleftframe,bd=2,bg='white',relief=RIDGE,text='Student info',font=("",12,"bold"))
        studentinfo.place(x=5,y=170,width=490,height=300)

        stidlabel=Label(studentinfo,text='Name:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=0,column=0,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='ID NO:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=0,column=2,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='Gender:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=1,column=0,sticky=W)
        stidentry=ttk.Combobox(studentinfo,width=12,font=("",12,"bold"),state="readonly")
        stidentry['values']=("Gender",'Male','Female')
        stidentry.current(0)
        stidentry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='DOB:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=1,column=2,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='Email:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=2,column=0,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='Phone no:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=2,column=2,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        stidlabel=Label(studentinfo,text='Address:',font=("",12,"bold"),padx=10,bg='white')
        stidlabel.grid(row=3,column=0,sticky=W)
        stidentry=ttk.Entry(studentinfo,width=13,font=("",12,"bold"))
        stidentry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #radio button
        radiobtn1=ttk.Radiobutton(studentinfo,text='Take Photo',value='Yes')
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(studentinfo,text='No Photo',value='Yes')
        radiobtn2.grid(row=4,column=1)
    
        Btnframe=Frame(studentinfo,bd=2,relief=RIDGE)
        Btnframe.place(x=0,y=180,width=484,height=34)

        savebtn=Button(Btnframe,text='Save',width=11,font=("",12,"bold"),bg='green',fg='white',cursor='hand2')
        savebtn.grid(row=0,column=0)
        updbtn=Button(Btnframe,text='Update',width=11,font=("",12,"bold"),bg='blue',fg='white',cursor='hand2')
        updbtn.grid(row=0,column=1)
        delbtn=Button(Btnframe,text='Delete',width=11,font=("",12,"bold"),bg='red',fg='white',cursor='hand2')
        delbtn.grid(row=0,column=2)
        resetbtn=Button(Btnframe,text='Reset',width=11,font=("",12,"bold"),bg='blue',fg='white',cursor='hand2')
        resetbtn.grid(row=0,column=3)

        Btnframe2=Frame(studentinfo,bd=2,relief=RIDGE)
        Btnframe2.place(x=0,y=220,width=484,height=34)

        takephoto=Button(Btnframe2,text='Take photo',width=24,font=("",12,"bold"),bg='orange',fg='white',cursor='hand2')
        takephoto.grid(row=0,column=0)
        updphpto=Button(Btnframe2,text='Update Photo',width=24,font=("",12,"bold"),bg='orangered',cursor='hand2',fg='white')
        updphpto.grid(row=0,column=1)



        innerrightframe=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Student Datails',font=("",12,"bold"))
        innerrightframe.place(x=520,y=10,width=590,height=500)

        #search
        searchfrm=LabelFrame(innerrightframe,bd=2,bg='white',relief=RIDGE,text='Search',font=("",12,"bold"))
        searchfrm.place(x=5,y=0,width=575,height=60)

        serchlbl=Label(searchfrm,text='Search by:',font=("",12,"bold"),padx=10,bg='skyblue',fg='white')
        serchlbl.grid(row=0,column=0,sticky=W)
        serchcombo=ttk.Combobox(searchfrm,font=("",12,"bold"),width=10,state="readonly")
        serchcombo['values']=("Select",'ID NO','Phone no')
        serchcombo.current(0)
        serchcombo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        serchentry=ttk.Entry(searchfrm,width=13,font=("",12,"bold"))
        serchentry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search=Button(searchfrm,text='Search',width=9,font=("",12,"bold"),bg='green',fg='white',cursor='hand2')
        search.grid(row=0,column=3)
        showall=Button(searchfrm,text='Show All',width=9,font=("",12,"bold"),bg='blue',fg='white',cursor='hand2')
        showall.grid(row=0,column=4)

        #data
        datafrm=LabelFrame(innerrightframe,bd=2,bg='white',relief=RIDGE,font=("",12,"bold"))
        datafrm.place(x=5,y=65,width=575,height=410)

        #scroll
        scrollx=ttk.Scrollbar(datafrm,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(datafrm,orient=VERTICAL)

        self.std_table=ttk.Treeview(datafrm,column=('Name','ID','Dept','degree','year','sem','gender','Email','Phone','Dob','Address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.std_table.xview)
        scrolly.config(command=self.std_table.yview)

        self.std_table.heading("Name",text="Name")
        self.std_table.heading("ID",text="ID no")
        self.std_table.heading("Dept",text="Department")
        self.std_table.heading("degree",text="Degree")
        self.std_table.heading("year",text="Year")
        self.std_table.heading("sem",text="Sem")
        self.std_table.heading("gender",text="Gender")
        self.std_table.heading("Email",text="Email")
        self.std_table.heading("Phone",text="Phone")
        self.std_table.heading("Dob",text="Dob")
        self.std_table.heading("Address",text="Address")
        self.std_table["show"]="headings"


        self.std_table.column("Name",width=100)
        self.std_table.column("ID",width=100)
        self.std_table.column("Dept",width=100)
        self.std_table.column("degree",width=100)
        self.std_table.column("year",width=100)
        self.std_table.column("sem",width=100)
        self.std_table.column("gender",width=100)
        self.std_table.column("Email",width=100)
        self.std_table.column("Phone",width=100)
        self.std_table.column("Dob",width=100)
        self.std_table.column("Address",width=100)

        self.std_table.pack(fill=BOTH,expand=1)










if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

