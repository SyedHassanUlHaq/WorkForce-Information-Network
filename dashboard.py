import time

from tkinter import *

from tkinter import messagebox

from PIL import Image

from datetime import date, datetime

from tkinter import ttk

from PIL import ImageTk

from employee import employeeClass

from customer import customerClass

from category import categoryClass

from project import projectClass

from sales import salesClass

import sqlite3

import os

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and omer")
        self.root.config(bg = "white")

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
        # Left Menu
        self.MenuLogo = Image.open(r"images\menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd = 2, relief = RIDGE, bg = "white")
        LeftMenu.place(x = 0, y =102, width = 200, height = 565)
        
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side = TOP, fill = X)

        self.icon_side = PhotoImage(file = "images/side.png")
        lbl_menu = Label(LeftMenu, text = "Menu", font=("times new roman", 20), bg="#009688", cursor="hand2").pack(side = TOP, fill = X)
        btn_employee = Button(LeftMenu, text = "Employee", command= self.employee, image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)
        btn_customer = Button(LeftMenu, command = self.customer, text = "Customer", image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)
        btn_category = Button(LeftMenu, command = self.category, text = "Category", image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)
        btn_project = Button(LeftMenu, command = self.project, text = "Project", image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)
        btn_sales = Button(LeftMenu,command=self.sales, text = "Sales", image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)
        btn_exit = Button(LeftMenu, text = "Exit", image = self.icon_side, compound = LEFT, padx = 5,  anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor="hand2").pack(side = TOP, fill = X)

        # content
        self.lbl_employee = Label(self.root, text = "Total Employee\n[ 0 ]", bd = 5, relief = RIDGE, bg = "#33bbf9", fg = "white", font = ("goudy old style", 20, "bold"))
        self.lbl_employee.place(x = 300, y = 120, height = 150, width = 300)

        self.lbl_supplier = Label(self.root, text="Total Suppliers\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # footer
        lbl_footer = Label(self.root, text="Workforce Information Network | Developed by Hafsa, Hassan and omer\n For any Issue Contact: +92 3320208649",font=("times new roman", 15), bg="#4d636d", fg="white").pack(side = BOTTOM, fill = X)

        self.update_content()

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def customer(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = customerClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def project(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = projectClass(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'win.db')
        cur = con.cursor()
        try:
            cur.execute("select * from project")
            project = cur.fetchall()
            self.lbl_product.config(text = f'Total Project\n[{str(len(project))}]')

            cur.execute("select * from customer")
            customer = cur.fetchall()
            self.lbl_supplier.config(text = f'Total customers\n[{str(len(customer))}]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text = f'Total Category\n[{str(len(category))}]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text = f'Total Employee\n[{str(len(employee))}]')
            bill = len(os.listdir('bill'))
            self.lbl_sales.config(text = f'Total Sales [{str(bill)}]')
            current_time = datetime.now().strftime("%I:%M:%S %p")
            current_date = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text = f"Welcome to Workforce Information Network \t\t Date: {current_date}\t\t Time: {current_time}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()