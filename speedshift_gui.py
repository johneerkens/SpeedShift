#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

# Conversion factors (to m/s)
CONVERSION_TO_MS = {
    "km/h": 0.277778,
    "mph": 0.44704,
    "m/s": 1.0,
    "knots": 0.514444
}

def convert():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        value_ms = value * CONVERSION_TO_MS[from_unit]
        result = value_ms / CONVERSION_TO_MS[to_unit]

        result_label.config(text=f"{result:.3f} {to_unit}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#1e1e1e" if dark_mode else "#f0f0f0"
    fg = "#ffffff" if dark_mode else "#000000"
    entry_bg = "#2d2d2d" if dark_mode else "#ffffff"

    root.configure(bg=bg)
    style.configure("TLabel", background=bg, foreground=fg)
    style.configure("TButton", background=bg)
    style.configure("TCombobox", fieldbackground=entry_bg)
    entry_value.configure(background=entry_bg, foreground=fg)

# Main window
root = tk.Tk()
root.title("SpeedShift")
root.geometry("340x260")
root.resizable(False, False)

dark_mode = False
style = ttk.Style()
style.theme_use("default")

# Title
title = ttk.Label(root, text="SpeedShift", font=("Arial", 16))
title.pack(pady=10)

# Entry
entry_value = tk.Entry(root, justify="center", font=("Arial", 11))
entry_value.pack(pady=5)

# Units
units = list(CONVERSION_TO_MS.keys())

from_unit_var = tk.StringVar(value="km/h")
to_unit_var = tk.StringVar(value="mph")

from_unit = ttk.Combobox(root, textvariable=from_unit_var, values=units, state="readonly")
to_unit = ttk.Combobox(root, textvariable=to_unit_var, values=units, state="readonly")

from_unit.pack(pady=4)
to_unit.pack(pady=4)

# Convert button
convert_btn = ttk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=8)

# Result
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Theme toggle
theme_btn = ttk.Button(root, text="🌙 / 🌞 Toggle Theme", command=toggle_theme)
theme_btn.pack(pady=8)

root.mainloop()
