#!/usr/bin/python3
import tkinter as tk

class QuickTkinterUI:
    def __init__(self, master=None):
        # build ui
        self.frm_main = tk.Frame(master, name="frm_main")
        self.frm_main.configure(background="#bdc3c7", height=200, width=300)
        self.btn_click_me = tk.Button(self.frm_main, name="btn_click_me")
        self.btn_click_me.configure(
            activebackground="#95a5a6",
            activeforeground="#FFFFFF",
            background="#7f8c8d",
            cursor="hand2",
            font="{Ubuntu Mono} 12 {bold}",
            foreground="#FFFFFF",
            highlightthickness=0,
            overrelief="flat",
            relief="flat",
            text='Click Me !')
        self.btn_click_me.place(
            anchor="nw",
            height=30,
            relx=0.5,
            rely=0.5,
            width=150,
            x=-75,
            y=-15)
        self.btn_click_me.configure(command=self.on_click_me)
        self.frm_main.pack(side="top")

        # Main widget
        self.mainwindow = self.frm_main

    def run(self):
        self.mainwindow.mainloop()

    def on_click_me(self):
        pass
