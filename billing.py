from tkinter import *

from PIL import Image

from tkinter import ttk

from PIL import ImageTk

from tkinter import messagebox

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and omer")
        self.root.config(bg = "white")

        # title
        self.icon_title = PhotoImage(file = r"images\logo1.png")
        title = Label(self.root, text = "Workforce Information Network", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#010c48", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 2, height = 70)

        # button_logout
        btn_logout = Button(self.root, text = "Logout", font = ("times new roman", 15, "bold"), bg = "yellow", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

        # clock
        self.lbl_clock = Label(self.root, text = "Welcome to Workforce Information Network \t\t Date: DD-MM-YYYY \t\t Time: HH:MM:SS", font = ("times new roman", 15), bg = "#4d636d", fg = "white")
        self.lbl_clock.place(x = 0, y = 70, relwidth = 1, height = 30)

        # product frame
        self.var_search = StringVar()
        
        projectFrame1 = Frame(self.root, bd = 4, relief=RIDGE, bg = "white")
        projectFrame1.place(x=10, y=110, width=410, height=550)

        pTitle = Label(projectFrame1, text="All Projects", font = ("goudy old style", 20, "bold"), bg = "#262626", fg = "white").pack(side = TOP, fill = X)

        # Product Search Frame
        projectFrame2 = Frame(projectFrame1, bd = 2, relief=RIDGE, bg = "white")
        projectFrame2.place(x=2, y=42, width=398, height=80)

        lbl_search = Label(projectFrame2, text="Search Project | By Name ", font = ("times new roman", 15, "bold"), bg = "white", fg = "green").place(x = 2, y = 5)

        lbl_search = Label(projectFrame2, text="Project Name", font = ("times new roman", 15, "bold"), bg = "white").place(x = 2, y = 45)

        txt_search = Entry(projectFrame2, textvariable=self.var_search, font = ("times new roman", 15), bg = "lightyellow").place(x = 128, y = 47, width = 150, height=22)
        btn_search = Button(projectFrame2, text="search", font = ("goudy old style", 15), bg = "#2196f3", fg = "white", cursor="hand2").place(x=285, y=45, width = 100, height=25)
        btn_show_all = Button(projectFrame2, text="Show All", font = ("goudy old style", 15), bg = "#083531", fg = "white", cursor="hand2").place(x=285, y=10, width = 100, height=25)

        # Project Detail Frame
        projectFrame3 = Frame(projectFrame1, bd = 3, relief=RIDGE)
        projectFrame3.place(x = 2, y = 140, width = 398, height = 375)

        scrolly = Scrollbar(projectFrame3, orient = VERTICAL)
        scrollx = Scrollbar(projectFrame3, orient = HORIZONTAL)

        self.project_Table = ttk.Treeview(projectFrame3, columns = ("pid", "name", "stipend", "length", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.project_Table.xview)
        scrolly.config(command=self.project_Table.yview)
        self.project_Table.heading("pid", text = "PID")
        self.project_Table.heading("name", text = "Name")
        self.project_Table.heading("stipend", text = "Stipend")
        self.project_Table.heading("length", text = "Length")
        self.project_Table.heading("status", text = "Status")
        self.project_Table["show"] = "headings"

        self.project_Table.column("pid", width = 90)
        self.project_Table.column("name", width = 100)
        self.project_Table.column("stipend", width = 100)
        self.project_Table.column("length", width = 100)
        self.project_Table.column("status", width = 100)
        self.project_Table.pack(fill = BOTH, expand = 1)
        # self.project_Table.bind("<ButtonRelease-1>", self.get_data)
        lbl_notes = Label(projectFrame1, text="Note:'Enter 0 Quantity to remove product from the Cart'", font=("goudy old style", 12), anchor = 'w', bg = "white", fg = "red").pack(side = BOTTOM, fill = X)

        # customer frame
        self.var_cname = StringVar()
        self.var_contact = StringVar
        customerFrame = Frame(self.root, bd = 4, relief=RIDGE, bg = "white")
        customerFrame.place(x=420, y=110, width=530, height=70)

        cTitle = Label(customerFrame, text="Customer Details", font = ("goudy old style", 15), bg = "lightgray").pack(side = TOP, fill = X)
        lbl_name = Label(customerFrame, text="Name", font = ("times new roman", 15), bg = "white").place(x = 5, y = 35)
        txt_name = Entry(customerFrame, textvariable=self.var_cname, font = ("times new roman", 13), bg = "lightyellow").place(x = 80, y = 35, width = 180)
        
        lbl_contact = Label(customerFrame, text="Contact No.", font = ("times new roman", 15), bg = "white").place(x = 270, y = 35)
        txt_contact = Entry(customerFrame, textvariable=self.var_contact, font = ("times new roman", 13), bg = "lightyellow").place(x = 380, y = 35, width = 140)
        
        # Cal cart Frame
        cal_cart_Frame = Frame(self.root, bd = 2, relief=RIDGE, bg = "white")
        cal_cart_Frame.place(x=420, y=190, width=530, height=360)

        # Calculator Frame
        cal_Frame = Frame(cal_cart_Frame, bd = 2, relief=RIDGE, bg = "white")
        cal_Frame.place(x=5, y=10, width=268, height=340)

        # Cart Frame
        cart_Frame = Frame(cal_cart_Frame, bd = 3, relief=RIDGE)
        cart_Frame.place(x = 280, y = 8, width = 245, height = 342)

        cartTitle = Label(cart_Frame, text="Cart \t Total Projects: [0]", font = ("goudy old style", 15), bg = "lightgray").pack(side = TOP, fill = X)

        scrolly = Scrollbar(cart_Frame, orient = VERTICAL)
        scrollx = Scrollbar(cart_Frame, orient = HORIZONTAL)

        self.cartTable = ttk.Treeview(cart_Frame, columns = ("pid", "name", "stipend", "length", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
        self.cartTable.heading("pid", text = "PID")
        self.cartTable.heading("name", text = "Name")
        self.cartTable.heading("stipend", text = "Stipend")
        self.cartTable.heading("length", text = "Length")
        self.cartTable.heading("status", text = "Status")
        self.cartTable["show"] = "headings"

        self.cartTable.column("pid", width = 40)
        self.cartTable.column("name", width = 100)
        self.cartTable.column("stipend", width = 90)
        self.cartTable.column("length", width = 40)
        self.cartTable.column("status", width = 90)
        self.cartTable.pack(fill = BOTH, expand = 1)
        # self.cartTable.bind("<ButtonRelease-1>", self.get_data)
        
        # Add Cart Widgets Frame
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_stipend = StringVar()
        self.var_length = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bd = 2, relief=RIDGE, bg = "white")
        cal_cart_Frame.place(x=420, y=550, width=530, height=110)

        lbl_p_name = Label(Add_CartWidgetsFrame, text = "Product Name", font = ("times new roman", 15), bg = "white").place(x = 5, y = 5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font = ("times new roman", 15), bg = "lightyellow", state = "readonly").place(x = 5, y = 35, width = 190, height = 22)

        lbl_p_stipend = Label(Add_CartWidgetsFrame, text = "Price per Projects", font = ("times new roman", 15), bg = "white").place(x = 230, y = 5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_stipend, font = ("times new roman", 15), bg = "lightyellow", state = "readonly").place(x = 230, y = 35, width = 150, height = 22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text = "Quantity", font = ("times new roman", 15), bg = "white").place(x = 390, y = 5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_qty, font = ("times new roman", 15), bg = "lightyellow").place(x = 390, y = 35, width = 120, height = 22)

        self.lbl_status = Label(Add_CartWidgetsFrame, text = "In Hand [9999]", font = ("times new roman", 15), bg = "white")
        self.lbl_status.place(x = 5, y = 70)

        btn_clear_cart = Button(Add_CartWidgetsFrame, text = "Clear", font = ("times new roman", 15, "bold"), bg = "lightyellow", cursor = "hand2").place(x = 180, y = 70, width=150, height=30)
        btn_clear_cart = Button(Add_CartWidgetsFrame, text = "Add | Update Cart", font = ("times new roman", 15, "bold"), bg = "orange", cursor = "hand2").place(x = 340, y = 70, width=180, height=30)
        


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()