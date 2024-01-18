from tkinter import messagebox
from app.quicktkinter_ui import QuickTkinterUI

class QuickTkinter(QuickTkinterUI):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
    
    def on_click_me(self):
        self.master.option_add('*Dialog.msg.width', 20)
        messagebox.showinfo(title="Information", message="Hello")
