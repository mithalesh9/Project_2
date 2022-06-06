from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # *****************Variable********************
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateretufine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        # ======================DataFrameLeft===================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",bg="powder blue",padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",font=("arial",12,"bold"))
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("arial",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="LastName:",font=("arial",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)       

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile:",font=("arial",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("arial",12,"bold"),padx=2,pady=4)
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,bg="powder blue",text="Autor Name:",font=("arial",12,"bold"),padx=2,pady=4)
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)
 
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=4)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lateretufine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=4)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.finalprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

         # ======================DataFrameRight===================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
      
        listBooks=['Python Programming','Java Programming','SQL CookBook','Grokking Algorithms','AI By Example','Cognative Psychlogy','Core Javascript',
                    'Advnace Python','PHP programming','R Programming','Css3','Web Development','Android Development','Data Mining','Machine learning',
                    'Deep learning','Data Science','Data Analytics','SEO Book','DBMS']

        def SelectBook(Event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Python Programming"):
                self.bookid_var.set("BKID5152")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("Eric Matthews")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")
            elif (x=="Java Programming"):
                self.bookid_var.set("BKID5752")
                self.booktitle_var.set("Java Programming")
                self.author_var.set("James Gosling")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.810")
            elif (x=="SQL CookBook"):
                self.bookid_var.set("BKID5735")
                self.booktitle_var.set("SQL CookBook")
                self.author_var.set("Anthony Molinaro")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.550")
            elif (x=="Grokking Algorithms"):
                self.bookid_var.set("BKID2335")
                self.booktitle_var.set("Grokking Algorithms")
                self.author_var.set("Aditya Bhargava")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.550")
            elif (x=="AI By Example"):
                self.bookid_var.set("BKID1001")
                self.booktitle_var.set("AI By Example")
                self.author_var.set("Denis Rothman")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.900")
            elif (x=="Cognative Psychlogy"):
                self.bookid_var.set("BKID1011")
                self.booktitle_var.set("Cognative Psychlogy")
                self.author_var.set("Mark Keane")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.730")
            elif (x=="Core Javascript"):
                self.bookid_var.set("BKID1071")
                self.booktitle_var.set("Core Javascript")
                self.author_var.set("Douglas Crockford")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.540")
            elif (x=="Advnace Python"):
                self.bookid_var.set("BKID1051")
                self.booktitle_var.set("Advnace Python")
                self.author_var.set("Paul Barry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.3137")
            elif (x=="PHP programming"):
                self.bookid_var.set("BKID1101")
                self.booktitle_var.set("PHP programming")
                self.author_var.set("Alan Orbes")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1820")
            elif (x=="R Programming"):
                self.bookid_var.set("BKID3124")
                self.booktitle_var.set("R Programming")
                self.author_var.set("Andriede Vries")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2175")
            elif (x=="Css3"):
                self.bookid_var.set("BKID3134")
                self.booktitle_var.set("The Book Css3")
                self.author_var.set("Peter Gasston")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1835")
            elif (x=="Web Development"):
                self.bookid_var.set("BKID2934")
                self.booktitle_var.set("Web Development")
                self.author_var.set("Randy Connolly")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.695")
            elif (x=="Android Development"):
                self.bookid_var.set("BKID2934")
                self.booktitle_var.set("Android Development")
                self.author_var.set("Lan F.Darwin")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.4500")
            elif (x=="Data Mining"):
                self.bookid_var.set("BKID1604")
                self.booktitle_var.set("Data Mining")
                self.author_var.set("Jain Pei")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.625")
            elif (x=="Machine learning"):
                self.bookid_var.set("BKID1617")
                self.booktitle_var.set("Machine learning")
                self.author_var.set("John Paul Mueller")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1460")
            elif (x=="Deep learning"):
                self.bookid_var.set("BKID1527")
                self.booktitle_var.set("Deep learning")
                self.author_var.set("Mohamed Elgendy")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2847")
            elif (x=="Data Science"):
                self.bookid_var.set("BKID2317")
                self.booktitle_var.set("Data Science")
                self.author_var.set("Allen Hamilton")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1300")
            elif (x=="Data Analytics"):
                self.bookid_var.set("BKID2327")
                self.booktitle_var.set("Data Analytics")
                self.author_var.set("Wes McKinney")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1450")
            elif (x=="SEO Book"):
                self.bookid_var.set("BKID2437")
                self.booktitle_var.set("SEO Book")
                self.author_var.set("Eric Enge")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2100")
            elif (x=="DBMS"):
                self.bookid_var.set("BKID2237")
                self.booktitle_var.set("DBMS")
                self.author_var.set("Rajiv Chopra")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateretufine_var.set("Rs.25")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.499")

        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        # ***********************Buttons frame**************************
        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameButton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(frameButton,command=self.addData,text="Add Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(frameButton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(frameButton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(frameButton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(frameButton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(frameButton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        # ***********************Information frame**************************
        frameInfomation=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameInfomation.place(x=0,y=600,width=1530,height=230)

        Table_frame=Frame(frameInfomation,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=195)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1",
                                                            "address2","postid","mobile","bookid","booktitle","author","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="FirstName")
        self.library_table.heading("lastname",text="LastName")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetchData()
        self.library_table.bind("<ButtonRelease-1>",self.getCursor)


    # Add or insert data into database
    def addData(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='librarymanagement')
        my_cursor=conn.cursor()
        if self.member_var.get() == "" or self.prn_var.get() == "" or self.firstname_var.get() == "" or self.lastname_var.get() == "" or self.address1_var.get() == "" or self.address2_var.get() == "":
            messagebox.showerror("Error","All Field Are Required..")
        else:
            my_cursor.execute("insert into information values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.member_var.get(),
                                                                                        self.prn_var.get(),
                                                                                        self.id_var.get(),                                                                                        
                                                                                        self.firstname_var.get(),
                                                                                        self.lastname_var.get(),
                                                                                        self.address1_var.get(),
                                                                                        self.address2_var.get(),
                                                                                        self.postcode_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.bookid_var.get(),
                                                                                        self.booktitle_var.get(),
                                                                                        self.author_var.get(),
                                                                                        self.dateborrowed_var.get(),
                                                                                        self.datedue_var.get(),
                                                                                        self.daysonbook_var.get(),
                                                                                        self.lateretufine_var.get(),
                                                                                        self.dateoverdue_var.get(),
                                                                                        self.finalprice_var.get()
                                                                                        ))
            conn.commit()
            self.fetchData()
            conn.close()                                                                 
            messagebox.showinfo("Success","Member has been inserted successfully")
    # Update Data 
    def update(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='librarymanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("update information set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookId=%s,Booktitle=%s,Author=%s,DateBorrowed=%s,Datedue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN=%s",(
                                                            self.member_var.get(),
                                                            self.id_var.get(),                                                            
                                                            self.firstname_var.get(),
                                                            self.lastname_var.get(),
                                                            self.address1_var.get(),
                                                            self.address2_var.get(),
                                                            self.postcode_var.get(),
                                                            self.mobile_var.get(),
                                                            self.bookid_var.get(),
                                                            self.booktitle_var.get(),
                                                            self.author_var.get(),
                                                            self.dateborrowed_var.get(),
                                                            self.datedue_var.get(),
                                                            self.daysonbook_var.get(),
                                                            self.lateretufine_var.get(),
                                                            self.dateoverdue_var.get(),
                                                            self.finalprice_var.get(),
                                                            self.prn_var.get(),
                                                            ))
        conn.commit()
        self.fetchData()
        self.reset()
        conn.close()                                                                 
        messagebox.showinfo("Success","Member has been Updated")

    # Delete membar
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='',database='librarymanagement')
            my_cursor = conn.cursor()
            query="delete from information where PRN=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetchData()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been Deleted")
            
            

    # Fetch data drom database
    def fetchData(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='librarymanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from information")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    # click on fetched data and get in input filed 
    def getCursor(self,event=''):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateretufine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book Id:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.lateretufine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateretufine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)
    # Exit
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()