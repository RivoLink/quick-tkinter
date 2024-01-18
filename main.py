#!/usr/bin/python3

import tkinter as tk
import app.quicktkinter as qt

if __name__ == "__main__":
    master = tk.Tk()
    master.title("Quick Tkinter")
    master.resizable(False, False)

    window_w = 300
    window_h = 200

    screen_w = master.winfo_screenwidth()
    screen_h = master.winfo_screenheight()

    center_x = int((screen_w - window_w)/2)
    center_y = int((screen_h - window_h)/2)

    master.geometry("{}x{}+{}+{}".format(
        window_w, 
        window_h, 
        center_x, 
        center_y
    ))

    app = qt.QuickTkinter(master)
    app.run()
