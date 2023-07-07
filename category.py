from tkinter import *

from PIL import Image

from PIL import ImageTk

from tkinter import ttk, messagebox

import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("WorkForce Information Network ----- A DBMS PROJECT by Hafsa, Hassan and omer")
        self.root.config(bg = "white")
        self.root.focus_force()

        # variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # title
        lbl_title = Label(self.root, text="Manage Project Category", font=("goudy old style", 30), bg = "#184a45", fg = "white", bd = 3, relief=RIDGE).pack(side = TOP, fill = X, padx=10, pady=20)
        
        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 30), bg = "white").place(x=50, y=100)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg = "lightyellow").place(x = 50, y = 170, width=300)

        btn_add = Button(self.root, command = self.add, text="ADD", font=("goudy old style", 15), bg = "#4caf50", fg = "white", cursor="hand2").place(x = 360, y = 170, width=150, height=30)
        btn_delete = Button(self.root, command = self.delete, text="DELETE", font=("goudy old style", 15), bg = "red", fg = "white", cursor="hand2").place(x = 520, y = 170, width=150, height=30)

        # category details
        cat_frame = Frame(self.root, bd = 3, relief=RIDGE)
        cat_frame.place(x = 700, y = 100, width = 300, height = 100)

        scrolly = Scrollbar(cat_frame, orient = VERTICAL)
        scrollx = Scrollbar(cat_frame, orient = HORIZONTAL)

        self.category_table = ttk.Treeview(cat_frame, columns = ("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)
        self.category_table.heading("cid", text = "C ID")
        self.category_table.heading("name", text = "Name")
        
        self.category_table["show"] = "headings"

        self.category_table.column("cid", width = 90)
        self.category_table.column("name", width = 100)
        self.category_table.pack(fill = BOTH, expand = 1)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)
        
        # images
        self.im1 = Image.open("images/cat.jpg")
        self.im1 = self.im1.resize((500, 200), Image.LANCZOS)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image = self.im1, bd=2, relief=RAISED)
        self.lbl_im1.place(x=50, y=220)

        self.im2 = Image.open("images/category.jpg")
        self.im2 = self.im2.resize((500, 200), Image.LANCZOS)
        self.im2 = ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image = self.im1, bd=2, relief=RAISED)
        self.lbl_im2.place(x=580, y=220)
        self.show()

    # funtions
    def add(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent = self.root)
            else:
                cur.execute("Select * from category where name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category already present, try different", parent = self.root)
                else:
                    cur.execute("Insert into category(name) values(?)",
                                [
                                    self.var_name.get(),                                
                                ])
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def show(self):
        con = sqlite3.connect(database='win.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values = row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent = self.root)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = (self.category_table.item(f))
        row = content['values']
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),

    def create_delete_trigger(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            # Drop the trigger if it already exists
            cur.execute("DROP TRIGGER IF EXISTS delete_category_trigger")

            # Create the trigger
            cur.execute("""
                CREATE TRIGGER delete_category_trigger
                BEFORE DELETE ON category
                FOR EACH ROW
                BEGIN
                    -- Open the file in append mode and write the employee information
                    INSERT INTO category_backup (cid, name)
                    SELECT OLD.cid, OLD.name;
                END;
            """)

            con.commit()
            messagebox.showinfo("Trigger Created", "Delete trigger for customer table created successfully")

        except Exception as ex:
            messagebox.showerror("Error", f"Error creating trigger: {str(ex)}")

    def add_backup_data_to_file(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM category_backup")
            rows = cur.fetchall()

            with open('Backups/Category_Backup.txt', 'a') as file_handle:
                for row in rows:
                    file_handle.write('C.I.D: ' + str(row[0]) + '\t')
                    file_handle.write('Name: ' + row[1] + '\t')
                    file_handle.write('\n')

            con.commit()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def delete(self):
        con = sqlite3.connect('win.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "please select category from the list", parent=self.root)
            else:
                self.create_delete_trigger()
                cur.execute("Select * from category where cid = ?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid, please try again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if op == True:
                        cur.execute("delete from category where cid = ?", (self.var_cat_id.get(),))
                        con.commit()
                        self.add_backup_data_to_file()
                        messagebox.showinfo("Delete", "category Deleted Successfully")
                        self.show()
                        # self.var_cat_id.set("")
                        # self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")



if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()