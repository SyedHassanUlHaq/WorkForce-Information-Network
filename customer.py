from tkinter import *

from PIL import Image

from PIL import ImageTk

from tkinter import ttk, messagebox

import sqlite3

class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and omer")
        self.root.config(bg = "white")
        self.root.focus_force()

        # All variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_cust_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        



        # search Frame
        SearchFrame = LabelFrame(self.root, text = "Search Employee", font = ("goudy old style", 12, "bold"), bg = "white")
        SearchFrame.place(x = 250, y = 20, width = 600, height = 70)

        # options
        lbl_search = Label(SearchFrame, text= "Search By Invoice No", bg = "white", font = ("goudy old style", 15))
        lbl_search.place(x = 10, y = 10)

        txt_search = Entry(SearchFrame, textvariable = self.var_searchtxt, font = ("goudy old style", 15), bg = "lightyellow").place(x = 200, y = 10)
        btn_search = Button(SearchFrame, command=self.search, text = "Search", font = ("goudy old style", 15), bg = "#4caf50", cursor="hand2", fg="white").place(x = 410, y = 9, width = 150, height = 30)

        # title
        title = Label(self.root, text = "Customer Details", font = ("goudy old style", 15), bg = "#0f4d7d", fg = "white").place(x = 50, y = 100, width=1000)

        # content
        # row 1
        lbl_supplier_invoice = Label(self.root, text = "Invoice No.", font = ("goudy old style", 15), bg = "white").place(x = 50, y = 150)

        txt_supplier_invoice = Entry(self.root, textvariable = self.var_cust_invoice, font = ("goudy old style", 15), bg = "lightyellow").place(x = 150, y = 150, width = 180)

        # row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=190, width=180)

        # row 3
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=230)  
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=150, y=230, width=180)
        
        # row 4
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=270)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=150, y=270, width=300, height = 60)


        # buttons
        btn_add = Button(self.root, text="Save", command = self.add, font=("goudy old style", 15), bg="#2196f3", cursor="hand2", fg="white").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, command=self.update, text="Update", font=("goudy old style", 15), bg="#4caf50", cursor="hand2", fg="white").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, command = self.delete, text="Delete", font=("goudy old style", 15), bg="#f44336", cursor="hand2", fg="white").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, command=self.clear, text="Clear", font=("goudy old style", 15), bg="#607d8b", cursor="hand2", fg="white").place(x=860, y=305, width=110, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd = 3, relief=RIDGE)
        emp_frame.place(x = 0, y = 350, relwidth = 1, height = 150)

        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.customerTable = ttk.Treeview(emp_frame, columns = ("invoice", "name", "contact", "gender", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.customerTable.xview)
        scrolly.config(command=self.customerTable.yview)
        self.customerTable.heading("invoice", text = "EMP ID")
        self.customerTable.heading("name", text = "Name")
        self.customerTable.heading("contact", text = "Email")
        self.customerTable.heading("desc", text = "Gender")
        self.customerTable["show"] = "headings"

        self.customerTable.column("invoice", width = 90)
        self.customerTable.column("name", width = 100)
        self.customerTable.column("contact", width = 100)
        self.customerTable.column("desc", width = 100)
        self.customerTable.column("contact", width = 100)
        self.customerTable.pack(fill = BOTH, expand = 1)
        self.customerTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()

    def add(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent = self.root)
            else:
                cur.execute("Select * from customer where invoice = ?", (self.self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Invoice No. already assigned, try different", parent = self.root)
                else:
                    cur.execute("Insert into customer(invoice, name, contact, desc) values(?, ?, ?, ?)",
                                [
                                    self.self.var_cust_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0', END),                                
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Customer Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            cur.execute("select * from customer")
            rows = cur.fetchall()
            self.customerTable.delete(*self.customerTable.get_children())
            for row in rows:
                self.customerTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def get_data(self, ev):
        f = self.customerTable.focus()
        content = (self.customerTable.item(f))
        row = content['values']
        self.self.var_cust_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0', END),
        self.txt_desc.insert(END, row[3]),
        
    def update(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent = self.root)
            else:
                cur.execute("Select * from customer where invoice = ?", (self.self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent = self.root)
                else:
                    cur.execute("Update customer set name = ?, contact = ?, desc = ? where invoice = ?",
                                [
                                    self.var_name.get(),
                                    self.var_email.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0', END),
                                    self.self.var_cust_invoice.get()
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Customer Updated Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. Must be required", parent=self.root)
            else:
                cur.execute("Select * from customer where invoice = ?", (self.self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from customer where invoice = ?", (self.self.var_cust_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "customer Deleted Successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):

        self.self.var_cust_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0', END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. is Required", parent = self.root)
            else:
                cur.execute("select * from customer where invoice = ?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.customerTable.delete(*self.customerTable.get_children())
                    self.customerTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = customerClass(root)
    root.mainloop()