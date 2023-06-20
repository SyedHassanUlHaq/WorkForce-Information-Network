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

        projectFrame2 = Frame(projectFrame1, bd = 2, relief=RIDGE, bg = "white")
        projectFrame2.place(x=2, y=42, width=398, height=80)

        lbl_search = Label(projectFrame2, text="Search Project | By Name ", font = ("times new roman", 15, "bold"), bg = "white", fg = "green").place(x = 2, y = 5)

        lbl_name = Label(projectFrame2, text="Project Name", font = ("times new roman", 15, "bold"), bg = "white").place(x = 5, y = 45)

        txt_search = Entry(projectFrame2, textvariable=self.var_search, font = ("times new roman", 15, "bold"), bg = "lightyellow").place(x = 128, y = 47, width = 150, height=22)
        btn_search = Button(projectFrame2, text="search", font = ("goudy old style", 15), bg = "#2196f3", fg = "white", cursor="hand2").place(x=285, y=45, width = 100, height=25)
        btn_show_all = Button(projectFrame2, text="Show All", font = ("goudy old style", 15), bg = "#083531", fg = "white", cursor="hand2").place(x=285, y=10, width = 100, height=25)

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
        customerFrame = Frame(self.root, bd = 4, relief=RIDGE, bg = "white")
        customerFrame.place(x=420, y=110, width=530, height=70)

        cTitle = Label(customerFrame, text="Customer Details", font = ("goudy old style", 15), bg = "lightgray").pack(side = TOP, fill = X)



if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()