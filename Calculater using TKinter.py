from tkinter import *

class Calculator:
    def __init__(self, parent, x, y):
        self.button_font = ('Verdana', 40)
        self.entry_font = ('Verdana', 20)
        self.parent = parent

        self.button_width = 4
        self.button_height = 1
        self.container = Frame(self.parent)
        self.container.grid(row=x, column=y)

        self.string = ''

        self.entry(0, 0)

        self.button('7', 1, 0)
        self.button('8', 1, 1)
        self.button('9', 1, 2)

        self.button('4', 2, 0)
        self.button('5', 2, 1)
        self.button('6', 2, 2)

        self.button('1', 3, 0)
        self.button('2', 3, 1)
        self.button('3', 3, 2)

        self.button('0', 4, 0)

        self.button('+', 1, 3)
        self.button('-', 1, 4)
        self.button('*', 2, 3)
        self.button('/', 2, 4)

        self.button('(', 3, 3)
        self.button(')', 3, 4)

        self.button_eq('=', 4, 1)

        self.button_clear('clear', 4, 3)
        self.button_rem('<', 4, 4)

    def entry(self, x_, y_):
        self.entry = Text(
            self.container, font=self.entry_font, state=DISABLED,
            height=self.button_height//2, width=self.button_width*5)
        self.entry.grid(row=x_, column=y_, columnspan=5, sticky='we')

    def button(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=lambda: self.normal_button_click(char_))
        self.b.grid(row=x_, column=y_)

    def button_eq(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.equal_button_click)
        self.b.grid(row=x_, column=y_, sticky='we', columnspan=2)

    def button_rem(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.rem_button_click)
        self.b.grid(row=x_, column=y_)

    def button_clear(self, char_, x_, y_):
        self.b = Button(
            self.container, text=char_, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.clear_button_click)
        self.b.grid(row=x_, column=y_)

    def display(self, text_):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text_)
        self.entry.config(state=DISABLED)

    def normal_button_click(self, text_):
        self.string = '' + self.string + text_
        self.display(self.string)

    def equal_button_click(self):
        self.display(eval(self.string))
        self.string = ''

    def rem_button_click(self):
        self.string = '' + self.string[0:-1]
        self.display(self.string)

    def clear_button_click(self):
        self.display('')
        self.string = ''


class App:
    def __init__(self, master):
        self.master = master

        calc = Calculator(self.master, 0, 0)


root = Tk()
app = App(root)
root.title('calculator by hassan')
root.mainloop()