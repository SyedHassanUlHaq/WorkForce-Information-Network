from tkinter import *

from PIL import Image

from PIL import ImageTk

from tkinter import ttk, messagebox

import sqlite3

class projectClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and omer")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_cust = StringVar()
        self.cat_list = []
        self.cust_list = []
        self.fetch_cat_cust()
        self.var_name = StringVar()
        self.var_stipend = StringVar()
        self.var_length = StringVar()
        self.var_status = StringVar()



        project_Frame = Frame(self.root, bd = 3, relief=RIDGE)
        project_Frame.place(x=10, y=10, width = 450, height=480)

        # title
        title = Label(project_Frame, text = "Project Details", font = ("goudy old style", 18), bg = "#0f4d7d", fg = "white").pack(side = TOP, fill = X)

        # column 1
        lbl_category = Label(project_Frame, text = "Category", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 60)
        lbl_customer = Label(project_Frame, text = "Customer", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 110)
        lbl_Project_name = Label(project_Frame, text = "Name", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 160)
        lbl_stipend = Label(project_Frame, text = "stipend", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 210)
        lbl_project_length = Label(project_Frame, text = "Length", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 260)
        lbl_status = Label(project_Frame, text = "status", font = ("goudy old style", 18), bg = "white").place(x = 30, y = 310)

        # colummn 2
        cmb_cat = ttk.Combobox(project_Frame, textvariable= self.var_cat, values = self.cat_list, state = 'readonly', justify = CENTER, font = ("goudy old style", 15))
        cmb_cat.place(x = 150, y = 60, width = 200)
        cmb_cat.current(0)

        cmb_cust = ttk.Combobox(project_Frame, textvariable= self.var_cust, values = self.cust_list, state = 'readonly', justify = CENTER, font = ("goudy old style", 15))
        cmb_cust.place(x = 150, y = 110, width = 200)
        cmb_cust.current(0)

        txt_name = Entry(project_Frame, textvariable= self.var_name, font = ("goudy old style", 15), bg="light yellow").place(x = 150, y = 160, width = 200)
        txt_stipend = Entry(project_Frame, textvariable= self.var_stipend, font = ("goudy old style", 15), bg="light yellow").place(x = 150, y = 210, width = 200)
        txt_length = Entry(project_Frame, textvariable= self.var_length, font = ("goudy old style", 15), bg="light yellow").place(x = 150, y = 260, width = 200)

        cmb_status = ttk.Combobox(project_Frame, textvariable= self.var_status, values = ("Active", "Inactive"), state = 'readonly', justify = CENTER, font = ("goudy old style", 15))
        cmb_status.place(x = 150, y = 310, width = 200)
        cmb_status.current(0)

        # buttons
        btn_add = Button(project_Frame, text="Save", command = self.add, font=("goudy old style", 15), bg="#2196f3", cursor="hand2", fg="white").place(x=10, y=400, width=100, height=40)
        btn_update = Button(project_Frame, command=self.update, text="Update", font=("goudy old style", 15), bg="#4caf50", cursor="hand2", fg="white").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(project_Frame, command = self.delete, text="Delete", font=("goudy old style", 15), bg="#f44336", cursor="hand2", fg="white").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(project_Frame, command=self.clear, text="Clear", font=("goudy old style", 15), bg="#607d8b", cursor="hand2", fg="white").place(x=340, y=400, width=100, height=40)

         # search Frame
        SearchFrame = LabelFrame(self.root, text = "Search Project", font = ("goudy old style", 12, "bold"), bg = "white")
        SearchFrame.place(x = 480, y = 10, width = 600, height = 80)

        # options
        cmb_search = ttk.Combobox(SearchFrame, textvariable= self.var_searchby, values = ("Select", "Category", "Customer", "Name"), state = 'readonly', justify = CENTER, font = ("goudy old style", 15))
        cmb_search.place(x = 10, y = 10, width = 180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable = self.var_searchtxt, font = ("goudy old style", 15), bg = "lightyellow").place(x = 220, y = 10)
        btn_search = Button(SearchFrame, command=self.search, text = "Search", font = ("goudy old style", 15), bg = "#4caf50", cursor="hand2", fg="white").place(x = 460, y = 9, width = 100, height = 30)


        # project Details
        p_frame = Frame(self.root, bd = 3, relief=RIDGE)
        p_frame.place(x = 480, y = 100, width = 600, height = 390)

        scrolly = Scrollbar(p_frame, orient = VERTICAL)
        scrollx = Scrollbar(p_frame, orient = HORIZONTAL)

        self.project_table = ttk.Treeview(p_frame, columns = ("pid", "Customer", "Category", "name", "stipend", "length", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.project_table.xview)
        scrolly.config(command=self.project_table.yview)
        self.project_table.heading("pid", text = "P ID")
        self.project_table.heading("Category", text = "Category")
        self.project_table.heading("Customer", text = "Customer")
        self.project_table.heading("name", text = "Name")
        self.project_table.heading("stipend", text = "Stipend")
        self.project_table.heading("length", text = "Length")
        self.project_table.heading("status", text = "Status")
        
        self.project_table["show"] = "headings"

        self.project_table.column("pid", width = 90)
        self.project_table.column("Category", width = 100)
        self.project_table.column("Customer", width = 100)
        self.project_table.column("name", width = 100)
        self.project_table.column("stipend", width = 100)
        self.project_table.column("length", width = 100)
        self.project_table.column("status", width = 100)
        self.project_table.pack(fill = BOTH, expand = 1)
        self.project_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        

    def fetch_cat_cust(self):
        self.cat_list.append("Empty")
        self.cust_list.append("Empty")
        con = sqlite3.connect(database = r'win.db')
        cur = con.cursor()
        try:
            cur.execute("select name from category")
            cat = cur.fetchall()
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("select name from customer")
            cust = cur.fetchall()
            if len(cust) > 0:
                del self.cust_list[:]
                self.cust_list.append("Select")
                for i in cust:
                    self.cust_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def add(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_cust.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "All Fields are be required", parent = self.root)
            else:
                cur.execute("Select * from project where name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Project already present, try different", parent = self.root)
                else:
                    cur.execute("Insert into project(Customer, Category, name, stipend, length, status) values(?, ?, ?, ?, ?, ?)",
                                [
                                    self.var_cat.get(),
                                    self.var_cust.get(),
                                    self.var_name.get(),
                                    self.var_stipend.get(),
                                    self.var_length.get(),
                                    self.var_status.get(),
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Project Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
    
    def show(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            cur.execute("select * from project")
            rows = cur.fetchall()
            self.project_table.delete(*self.project_table.get_children())
            for row in rows:
                self.project_table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def get_data(self, ev):
        f = self.project_table.focus()
        content = (self.project_table.item(f))
        row = content['values']
        self.var_pid.set(row[0]),
        self.var_cust.set(row[1])
        self.var_cat.set(row[2]),
        self.var_name.set(row[3]),
        self.var_stipend.set(row[4]),
        self.var_length.set(row[5]),
        self.var_status.set(row[6]),
                            
        
    def update(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please Select project from list", parent = self.root)
            else:
                cur.execute("Select * from project where pid = ?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid project ID", parent = self.root)
                else:
                    cur.execute("Update project set Category = ?, customer = ?, name = ?, stipend = ?, length = ?, status = ? where pid = ?",
                                [
                                    self.var_cat.get(),
                                    self.var_cust.get(),
                                    self.var_name.get(),
                                    self.var_stipend.get(),
                                    self.var_length.get(),
                                    self.var_status.get(),
                                    self.var_pid.get()
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Project Updated Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def create_delete_trigger(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            # Drop the trigger if it already exists
            cur.execute("DROP TRIGGER IF EXISTS delete_project_trigger")

            # Create the trigger
            cur.execute("""
                CREATE TRIGGER delete_project_trigger
                BEFORE DELETE ON project
                FOR EACH ROW
                BEGIN
                    -- Open the file in append mode and write the employee information
                    INSERT INTO project_backup (pid, customer, category, name, stipend, length, status)
                    SELECT OLD.pid, OLD.customer, OLD.category, OLD.name, OLD.stipend, OLD.Length, OLD.status;
                END;
            """)

            con.commit()
            messagebox.showinfo("Trigger Created", "Delete trigger for project table created successfully")

        except Exception as ex:
            messagebox.showerror("Error", f"Error creating trigger: {str(ex)}")

    def add_backup_data_to_file(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM project_backup")
            rows = cur.fetchall()

            with open('Backups/Projects_Backup.txt', 'a') as file_handle:
                for row in rows:
                    file_handle.write('P.I.D: ' + str(row[0]) + '\t')
                    file_handle.write('Customer: ' + row[1] + '\t')
                    file_handle.write('Category: ' + row[2] + '\t')
                    file_handle.write('Name: ' + row[3] + '\t')
                    file_handle.write('Stipend: ' + row[4] + '\t')
                    file_handle.write('Length: ' + row[5] + '\t')
                    file_handle.write('Status: ' + row[6] + '\t')
                    file_handle.write('\n')

            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Select Project from list", parent=self.root)
            else:
                self.create_delete_trigger()
                cur.execute("Select * from project where pid = ?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Project", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from project where pid = ?", (self.var_pid.get(),))
                        con.commit()
                        self.add_backup_data_to_file()
                        messagebox.showinfo("Delete", "Project Deleted Successfully")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def clear(self):
        self.var_cat.set("Select"),
        self.var_cust.set("Select"),
        self.var_name.set(""),
        self.var_stipend.set("Select"),
        self.var_length.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
    
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search Input is Required", parent=self.root)
            else:
                # Construct the SQL query with the search criteria
                query = "CREATE VIEW project_search_view AS SELECT * FROM project WHERE {} LIKE '%{}%'".format(self.var_searchby.get(), self.var_searchtxt.get())
            
                # Create the view
                cur.execute(query)
            
                # Query the view to retrieve the filtered data
                cur.execute("SELECT * FROM project_search_view")
                rows = cur.fetchall()
            
                if len(rows) != 0:
                    self.project_table.delete(*self.project_table.get_children())
                    for row in rows:
                        self.project_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found !!")
            
                # Drop the view after use
                cur.execute("DROP VIEW IF EXISTS project_search_view")
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = projectClass(root)
    root.mainloop()