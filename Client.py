from tkinter import *

from PIL import Image

from PIL import ImageTk

from tkinter import ttk, messagebox

import sqlite3

class ClientClass:
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
        # options
        lbl_search = Label(self.root, text= "Invoice No", bg = "white", font = ("goudy old style", 15))
        lbl_search.place(x = 700, y = 80)

        txt_search = Entry(self.root, textvariable = self.var_searchtxt, font = ("goudy old style", 15), bg = "lightyellow").place(x = 800, y = 80, width = 160)
        btn_search = Button(self.root, command=self.search, text = "Search", font = ("goudy old style", 15), bg = "#4caf50", cursor="hand2", fg="white").place(x = 980, y = 79, width = 100, height = 28)

        # title
        title = Label(self.root, text = "Client Details", font = ("goudy old style", 20, "bold"), bg = "#0f4d7d", fg = "white").place(x = 50, y = 10, width=1000, height=40)

        # content
        # row 1
        lbl_supplier_invoice = Label(self.root, text = "Invoice No.", font = ("goudy old style", 15), bg = "white").place(x = 50, y = 80)
        txt_supplier_invoice = Entry(self.root, textvariable = self.var_cust_invoice, font = ("goudy old style", 15), bg = "lightyellow").place(x = 180, y = 80, width = 180)

        # row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=120, width=180)

        # row 3
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=160)  
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=180, y=160, width=180)
        
        # row 4
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=200)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height = 120)


        # buttons
        btn_add = Button(self.root, text="Save", command = self.add, font=("goudy old style", 15), bg="#2196f3", cursor="hand2", fg="white").place(x=180, y=370, width=110, height=35)
        btn_update = Button(self.root, command=self.update, text="Update", font=("goudy old style", 15), bg="#4caf50", cursor="hand2", fg="white").place(x=300, y=370, width=110, height=35)
        btn_delete = Button(self.root, command = self.delete, text="Delete", font=("goudy old style", 15), bg="#f44336", cursor="hand2", fg="white").place(x=420, y=370, width=110, height=35)
        btn_clear = Button(self.root, command=self.clear, text="Clear", font=("goudy old style", 15), bg="#607d8b", cursor="hand2", fg="white").place(x=540, y=370, width=110, height=35)

        # Employee Details
        emp_frame = Frame(self.root, bd = 3, relief=RIDGE)
        emp_frame.place(x = 700, y = 120, width = 380, height = 350)

        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)

        self.ClientTable = ttk.Treeview(emp_frame, columns = ("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.ClientTable.xview)
        scrolly.config(command=self.ClientTable.yview)
        self.ClientTable.heading("invoice", text = "Invoice No.")
        self.ClientTable.heading("name", text = "Name")
        self.ClientTable.heading("contact", text = "Contact")
        self.ClientTable.heading("desc", text = "Description")
        self.ClientTable["show"] = "headings"

        self.ClientTable.column("invoice", width = 90)
        self.ClientTable.column("name", width = 100)
        self.ClientTable.column("contact", width = 100)
        self.ClientTable.column("desc", width = 100)
        self.ClientTable.column("contact", width = 100)
        self.ClientTable.pack(fill = BOTH, expand = 1)
        self.ClientTable.bind("<ButtonRelease-1>", self.get_data)
        
        self.show()

    def add(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent = self.root)
            else:
                cur.execute("Select * from Client where invoice = ?", (self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Invoice No. already assigned, try different", parent = self.root)
                else:
                    cur.execute("Insert into Client(invoice, name, contact, desc) values(?, ?, ?, ?)",
                                [
                                    self.var_cust_invoice.get(),
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0', END),                                
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Client Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            cur.execute("select * from Client")
            rows = cur.fetchall()
            self.ClientTable.delete(*self.ClientTable.get_children())
            for row in rows:
                self.ClientTable.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def get_data(self, ev):
        f = self.ClientTable.focus()
        content = (self.ClientTable.item(f))
        row = content['values']
        self.var_cust_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0', END),
        self.txt_desc.insert(END, row[3]),
        
    def update(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent = self.root)
            else:
                cur.execute("Select * from Client where invoice = ?", (self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent = self.root)
                else:
                    cur.execute("Update Client set name = ?, contact = ?, desc = ? where invoice = ?",
                                [
                                    self.var_name.get(),
                                    self.var_contact.get(),
                                    self.txt_desc.get('1.0', END),
                                    self.var_cust_invoice.get()
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Client Updated Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def create_delete_trigger(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            # Drop the trigger if it already exists
            cur.execute("DROP TRIGGER IF EXISTS delete_Client_trigger")

            # Create the trigger
            cur.execute("""
                CREATE TRIGGER delete_Client_trigger
                BEFORE DELETE ON Client
                FOR EACH ROW
                BEGIN
                    -- Open the file in append mode and write the employee information
                    INSERT INTO Client_backup (invoice, name, contact, desc)
                    SELECT OLD.invoice, OLD.name, OLD.contact, OLD.desc;
                END;
            """)

            con.commit()
            messagebox.showinfo("Trigger Created", "Delete trigger for Client table created successfully")

        except Exception as ex:
            messagebox.showerror("Error", f"Error creating trigger: {str(ex)}")

    def add_backup_data_to_file(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM Client_backup")
            rows = cur.fetchall()

            with open('Backups/Clients_Backup.txt', 'a') as file_handle:
                for row in rows:
                    file_handle.write('Invoice No.: ' + str(row[0]) + '\t')
                    file_handle.write('Client Name: ' + row[1] + '\t')
                    file_handle.write('Contact: ' + row[2] + '\t')
                    file_handle.write('Client Description: ' + row[3] + '\t')
                    file_handle.write('\n')

            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_cust_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. Must be required", parent=self.root)
            else:
                self.create_delete_trigger()
                cur.execute("Select * from Client where invoice = ?", (self.var_cust_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from Client where invoice = ?", (self.var_cust_invoice.get(),))
                        con.commit()

                        self.add_backup_data_to_file()

                        messagebox.showinfo("Delete", "Client Deleted Successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):

        self.var_cust_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0', END),
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()

        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice No. is Required", parent=self.root)
            else:
                # Construct the SQL query with the search criteria
                query = "CREATE VIEW Client_search_view AS SELECT * FROM Client WHERE invoice = '{}'".format(self.var_searchtxt.get())
            
                # Create the view
                cur.execute(query)
            
                # Query the view to retrieve the filtered data
                cur.execute("SELECT * FROM Client_search_view")
                row = cur.fetchone()
            
                if row is not None:
                    self.ClientTable.delete(*self.ClientTable.get_children())
                    self.ClientTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!")
            
                # Drop the view after use
                cur.execute("DROP VIEW IF EXISTS Client_search_view")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = ClientClass(root)
    root.mainloop()