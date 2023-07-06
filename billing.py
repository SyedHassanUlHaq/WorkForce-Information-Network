from tkinter import *

from PIL import Image

from tkinter import ttk

from PIL import ImageTk

from tkinter import messagebox

import sqlite3

import time

import os

import tempfile

from datetime import date, datetime

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and Omer")
        self.root.config(bg = "white")
        self.cart_list = []
        self.chk_print = 0

        # title
        self.icon_title = PhotoImage(file = r"images\logo1.png")
        title = Label(self.root, text = "Workforce Information Network", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#010c48", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 2, height = 70)

        # button_logout
        btn_logout = Button(self.root, command = self.logout, text = "Logout", font = ("times new roman", 15, "bold"), bg = "yellow", cursor = "hand2").place(x = 1150, y = 10, height = 50, width = 150)

        # clock
        current_date = date.today()
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.lbl_clock = Label(root, text=f"Welcome to Workforce Information Network \t\t Date: {current_date} \t\tTime: {current_time}", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # product frame        
        projectFrame1 = Frame(self.root, bd = 4, relief=RIDGE, bg = "white")
        projectFrame1.place(x=10, y=110, width=410, height=550)

        pTitle = Label(projectFrame1, text="All Projects", font = ("goudy old style", 20, "bold"), bg = "#262626", fg = "white").pack(side = TOP, fill = X)

        # Project Search Frame
        self.var_search = StringVar()
        projectFrame2 = Frame(projectFrame1, bd = 2, relief=RIDGE, bg = "white")
        projectFrame2.place(x=2, y=42, width=398, height=80)

        lbl_search = Label(projectFrame2, text="Search Project | By Name ", font = ("times new roman", 15, "bold"), bg = "white", fg = "green").place(x = 2, y = 5)

        lbl_search = Label(projectFrame2, text="Project Name", font = ("times new roman", 15, "bold"), bg = "white").place(x = 2, y = 45)

        txt_search = Entry(projectFrame2, textvariable=self.var_search, font = ("times new roman", 15), bg = "lightyellow").place(x = 128, y = 47, width = 150, height=22)
        btn_search = Button(projectFrame2, command = self.search, text="search", font = ("goudy old style", 15), bg = "#2196f3", fg = "white", cursor="hand2").place(x=285, y=45, width = 100, height=25)
        btn_show_all = Button(projectFrame2, command = self.show, text="Show All", font = ("goudy old style", 15), bg = "#083531", fg = "white", cursor="hand2").place(x=285, y=10, width = 100, height=25)

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

        self.project_Table.column("pid", width = 40)
        self.project_Table.column("name", width = 100)
        self.project_Table.column("stipend", width = 100)
        self.project_Table.column("length", width = 40)
        self.project_Table.column("status", width = 90)
        self.project_Table.pack(fill = BOTH, expand = 1)
        self.project_Table.bind("<ButtonRelease-1>", self.get_data)
        lbl_notes = Label(projectFrame1, text="Note:'Enter 0 Quantity to remove product from the Cart'", font=("goudy old style", 12), anchor = 'w', bg = "white", fg = "red").pack(side = BOTTOM, fill = X)

        # customer frame
        self.var_cname = StringVar()
        self.var_contact = StringVar()
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
        self.var_cal_input = StringVar()

        cal_Frame = Frame(cal_cart_Frame, bd = 9, relief = RIDGE, bg = "white")
        cal_Frame.place(x = 5, y = 10, width = 268, height = 340)

        txt_cal_input = Entry(cal_Frame, textvariable= self.var_cal_input, font= ('arial', 15, 'bold'), width=21, bd = 10, relief=GROOVE, state='readonly', justify = RIGHT)
        txt_cal_input.grid(row = 0, columnspan = 4)

        btn_7 = Button(cal_Frame, command = lambda:self.get_input(7), text = '7', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 1, column = 0)
        btn_8 = Button(cal_Frame, command = lambda:self.get_input(8) ,text = '8', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 1, column = 1)
        btn_9 = Button(cal_Frame, command = lambda:self.get_input(9), text = '9', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 1, column = 2)
        btn_sum = Button(cal_Frame, command = lambda:self.get_input('+'), text = '+', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 1, column = 3)

        btn_4 = Button(cal_Frame, command = lambda:self.get_input(4), text = '4', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 2, column = 0)
        btn_5 = Button(cal_Frame, command = lambda:self.get_input(5), text = '5', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 2, column = 1)
        btn_6 = Button(cal_Frame, command = lambda:self.get_input(6), text = '6', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 2, column = 2)
        btn_sub = Button(cal_Frame, command = lambda:self.get_input('-'), text = '-', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 2, column = 3)

        btn_1 = Button(cal_Frame, command = lambda:self.get_input(1), text = '1', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 3, column = 0)
        btn_2 = Button(cal_Frame, command = lambda:self.get_input(2), text = '2', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 3, column = 1)
        btn_3 = Button(cal_Frame, command = lambda:self.get_input(3), text = '3', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 3, column = 2)
        btn_sum = Button(cal_Frame, command = lambda:self.get_input('*'), text = '*', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 10, cursor="hand2").grid(row = 3, column = 3)

        btn_0 = Button(cal_Frame, command = lambda:self.get_input(0), text = '0', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 15, cursor="hand2").grid(row = 4, column = 0)
        btn_c = Button(cal_Frame, command = self.clear, text = 'C', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 15, cursor="hand2").grid(row = 4, column = 1)
        btn_eq = Button(cal_Frame, command = self.perform_cal, text = '=', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 15, cursor="hand2").grid(row = 4, column = 2)
        btn_div = Button(cal_Frame, command = lambda:self.get_input('/'), text = '/', font = ('arial', 15, 'bold'), bd = 5, width = 4, pady = 15, cursor="hand2").grid(row = 4, column = 3)


        # Cart Frame
        cart_Frame = Frame(cal_cart_Frame, bd = 3, relief=RIDGE)
        cart_Frame.place(x = 280, y = 8, width = 245, height = 342)

        self.cartTitle = Label(cart_Frame, text="Cart \t Total Projects: [0]", font = ("goudy old style", 15), bg = "lightgray")
        self.cartTitle.pack(side = TOP, fill = X)

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
        self.cartTable.column("name", width = 90)
        self.cartTable.column("stipend", width = 90)
        self.cartTable.column("length", width = 40)
        self.cartTable.pack(fill = BOTH, expand = 1)
        # self.cartTable.bind("<ButtonRelease-1>", self.get_data)
        
        # Add Cart Widgets Frame
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_stipend = StringVar()
        self.var_length = StringVar()
        self.var_status = StringVar()

        Add_CartWidgetsFrame = Frame(self.root, bd = 2, relief=RIDGE, bg = "white")
        Add_CartWidgetsFrame.place(x=420, y=550, width=530, height=110)

        lbl_p_name = Label(Add_CartWidgetsFrame, text = "Product Name", font = ("times new roman", 15), bg = "white").place(x = 5, y = 5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_pname, font = ("times new roman", 15), bg = "lightyellow", state = "readonly").place(x = 5, y = 35, width = 190, height = 22)

        lbl_p_stipend = Label(Add_CartWidgetsFrame, text = "Price per Projects", font = ("times new roman", 15), bg = "white").place(x = 230, y = 5)
        txt_p_name = Entry(Add_CartWidgetsFrame, textvariable=self.var_stipend, font = ("times new roman", 15), bg = "lightyellow", state = "readonly").place(x = 230, y = 35, width = 150, height = 22)

        lbl_p_qty = Label(Add_CartWidgetsFrame, text = "Project Length", font = ("times new roman", 15), bg = "white").place(x = 390, y = 5)
        txt_p_qty = Entry(Add_CartWidgetsFrame, textvariable=self.var_length, font = ("times new roman", 15), bg = "lightyellow").place(x = 390, y = 35, width = 120, height = 22)

        self.lbl_status = Label(Add_CartWidgetsFrame, text = "In Hand", font = ("times new roman", 15), bg = "white")
        self.lbl_status.place(x = 5, y = 70)

        btn_clear_cart = Button(Add_CartWidgetsFrame, command = self.clear_cart, text = "Clear", font = ("times new roman", 15, "bold"), bg = "lightyellow", cursor = "hand2").place(x = 180, y = 70, width=150, height=30)
        btn_add_cart = Button(Add_CartWidgetsFrame, command=self.add_update_cart, text = "Add | Update Cart", font = ("times new roman", 15, "bold"), bg = "orange", cursor = "hand2").place(x = 340, y = 70, width=180, height=30)

        # Billing Area
        # self.var_cal_input = StringVar()

        billFrame = Frame(self.root, bd = 2, relief = RIDGE, bg = "white")
        billFrame.place(x = 953, y = 110, width = 410, height = 410)

        BTitle = Label(billFrame, text="Customer Bill Area", font = ("goudy old style", 20, "bold"), bg = "#f44336", fg = "white").pack(side = TOP, fill = X)
        scrolly = Scrollbar(billFrame, orient = VERTICAL)
        scrolly.pack(side = RIGHT, fill = Y)

        self.txt_bill_area = Text(billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # billing buttons
        billMenuFrame = Frame(self.root, bd = 2, relief = RIDGE, bg = "white")
        billMenuFrame.place(x = 953, y = 520, width = 410, height = 140)

        self.lbl_amnt = Label(billMenuFrame, text="Bill Amount\n[0]", font = ("goudy old style", 15, "bold"), bg = "#3f51b5", fg = "white")
        self.lbl_amnt.place(x = 2, y = 5, width = 120, height = 70)

        self.lbl_discount = Label(billMenuFrame, text="Discount\n[5%]", font = ("goudy old style", 15, "bold"), bg = "#8bc34a", fg = "white")
        self.lbl_discount.place(x = 124, y = 5, width = 120, height = 70)

        self.lbl_net_pay = Label(billMenuFrame, text="Net pay\n[0]", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white")
        self.lbl_net_pay.place(x = 245, y = 5, width = 160, height = 70)

        btn_print = Button(billMenuFrame, command = self.print_bill, text="Print", cursor = "hand2", font = ("goudy old style", 15, "bold"), bg = "lightgreen", fg = "white")
        btn_print.place(x = 2, y = 80, width = 120, height = 50)

        btn_clear_all = Button(billMenuFrame, command = self.clear_all, cursor="hand2", text="Clear All", font = ("goudy old style", 15, "bold"), bg = "gray", fg = "white")
        btn_clear_all.place(x = 124, y = 80, width = 120, height = 50)

        btn_generate = Button(billMenuFrame, command = self.generate_bill, cursor = "hand2", text="Generate Bill/Save Bill", font = ("goudy old style", 10, "bold"), bg = "#009688", fg = "white")
        btn_generate.place(x = 246, y = 80, width = 160, height = 50)

        footer = Label(self.root, text = "WIN-Workforce Information Network | Developed By Rangesh\nFor any Technical Issue contact: 03320208649", font = ("times new roman", 11), bg = "#4d636d", fg = "white").pack(side = BOTTOM, fill = X)
        
        self.show()
        self.bil_top()
        self.update_date_time()


        # Functions
    def get_input(self, num):
        current_value = self.var_cal_input.get()
        new_value = current_value + str(num)
        self.var_cal_input.set(new_value)

    def clear(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            # self.project_Table = ttk.Treeview(projectFrame3, columns = ("pid", "name", "stipend", "length", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            cur.execute("select pid, name, stipend, length, status from project where status = 'Active'")
            rows = cur.fetchall()
            self.project_Table.delete(*self.project_Table.get_children())
            for row in rows:
                self.project_Table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def search(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search Input is Required", parent = self.root)
            else:
                cur.execute("select pid, name, stipend, length, status from project where name LIKE '%"+self.var_search.get()+"%' and status = 'Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.project_Table.delete(*self.project_Table.get_children())
                    for row in rows:
                        self.project_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.project_Table.focus()
        content = (self.project_Table.item(f))
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_stipend.set(row[2])
        self.var_length.set(row[3])
        self.lbl_status.config(text = f"In Hand [{str(row[3])}]")
        self.var_status.set(row[4])
        
    def add_update_cart(self):
        f = self.cartTable.focus()
        content = (self.cartTable.item(f))
        row= content['values']
        print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_stipend.set(row[2])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror('Error', "Please Select Projet from the list", parent = self.root)
        elif self.var_length.get() == '':
            messagebox.showerror('Error', "Project Length is Required", parent = self.root)
        else:
            # price_cal = int(self.var_length.get())*float(self.var_stipend.get())
            # price_cal = float(price_cal)
            price_cal = self.var_stipend.get()
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_length.get(), self.var_status.get]
            # update cart
            present = 'no'
            index_ = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index_ += 1
            if present == 'yes':
                op = messagebox.askyesno('confirm', "Project already present\nDo you want to Update | Remove from the Cart List", parent = self.root)
                if op == True:
                    if self.var_length.get() == "0":
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2] = price_cal
                        self.cart_list[index_][3] = self.var_length.get()
            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get() == '':
            messagebox.showerror("Error", f"Customer Details are required", parent = self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", f"Please Add product to the Cart !!!", parent = self.root)
        else:
            # Bill Top
            self.bil_top()
            # Bill Middle
            self.bill_middle()
            # Bill Bottom
            self.bill_bottom()

            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved', "Bill has been generated/Saved in the Backend", parent = self.root)
            self.chk_print = 1


    def bil_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone No 0332***** , Karachi
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("=" * 47)}
 Bill Amount\t\t\t\tRs. {self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("=" * 47)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(row[2]) * int(row[3]))

        self.discount = (self.bill_amnt * 5) / 100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text = f"Cart \t Total Projects: [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def bill_middle(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid = row[0]
                name = row[1]
                length = int(StringVar(row[4])) - int(StringVar(row[3]))
                if int(StringVar(row[3])) == int(StringVar(row[4])):
                    status = 'Inactive'
                if int(StringVar(row[3])) != int(StringVar(row[4])):
                    status = 'Active'

                price = float(row[2])*int(StringVar(row[3]))
                price = str(price)
                self.txt_bill_area.insert(END, "\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                # update length in project table
                cur.execute('update project set length = ?, status = ? where pid ?',(
                    length,
                    status,
                    pid,
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_stipend.set('')
        self.var_length.set('')
        self.lbl_status.config(text = f"In Stock")
        self.var_status.set('')

    def clear_all(self):
        self.chk_print = 0
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set()
        self.txt_bill_area.delete('1.0', END)
        self.cartTitle.config(text = f"Cart\t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text = f"Welcome to Workforce Information Network \t\t Date: {current_date}\t\t Time: {current_time}")
        self.lbl_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo('Print', "Please wait while printing", parent = self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror('Print', "Please generate bill, to print the receipt", parent = self.root)


    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()