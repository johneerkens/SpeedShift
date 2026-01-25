#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def kmh_to_mph():
    try:
        kmh = float(entry_value.get())
        mph = kmh * 0.621371
        result_label.config(text=f"{mph:.2f} mph")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def mph_to_kmh():
    try:
        mph = float(entry_value.get())
        kmh = mph / 0.621371
        result_label.config(text=f"{kmh:.2f} km/h")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Main window
root = tk.Tk()
root.title("SpeedShift")
root.geometry("300x200")
root.resizable(False, False)

# Widgets
title = ttk.Label(root, text="SpeedShift", font=("Arial", 16))
title.pack(pady=10)

entry_value = ttk.Entry(root, justify="center")
entry_value.pack(pady=5)

btn_kmh = ttk.Button(root, text="km/h → mph", command=kmh_to_mph)
btn_kmh.pack(pady=5)

btn_mph = ttk.Button(root, text="mph → km/h", command=mph_to_kmh)
btn_mph.pack(pady=5)

result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
