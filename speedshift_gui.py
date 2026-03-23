#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

from speedshift_core import SPEED_UNITS_TO_MS, convert_speed


def convert():
    try:
        value = float(entry_value.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        result = convert_speed(value, from_unit, to_unit)
        result_label.config(text=f"{result:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


def clear_fields():
    entry_value.delete(0, tk.END)
    result_label.config(text="")


def quit_app():
    root.destroy()


def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#1e1e1e" if dark_mode else "#f0f0f0"
    fg = "#ffffff" if dark_mode else "#000000"
    entry_bg = "#2d2d2d" if dark_mode else "#ffffff"
    btn_bg = DARK_BTN_BG if dark_mode else LIGHT_BTN_BG

    root.configure(bg=bg)
    style.configure("TLabel", background=bg, foreground=fg)
    style.configure("TCombobox", fieldbackground=entry_bg)
    entry_value.configure(background=entry_bg, foreground=fg)

    theme_btn.configure(
        background=btn_bg,
        foreground=fg,
        activebackground=btn_bg,
    )


# --- GUI setup ---
root = tk.Tk()
root.title("SpeedShift")
root.geometry("360x300")
root.resizable(False, False)

dark_mode = False
style = ttk.Style()
style.theme_use("default")
LIGHT_BTN_BG = "#e0e0e0"
DARK_BTN_BG = "#3a3a3a"

# Title
title = ttk.Label(root, text="SpeedShift", font=("Arial", 16))
title.pack(pady=10)

# Input
entry_value = tk.Entry(root, justify="center", font=("Arial", 11))
entry_value.pack(pady=6)

# Units (dynamic)
units = list(SPEED_UNITS_TO_MS.keys())

from_unit_var = tk.StringVar(value="km/h")
to_unit_var = tk.StringVar(value="mph")

from_unit = ttk.Combobox(
    root,
    textvariable=from_unit_var,
    values=units,
    state="readonly",
)
to_unit = ttk.Combobox(
    root,
    textvariable=to_unit_var,
    values=units,
    state="readonly",
)

from_unit.pack(pady=4)
to_unit.pack(pady=4)

# Buttons frame (Convert + Clear)
button_frame = ttk.Frame(root)
button_frame.pack(pady=8)

convert_btn = ttk.Button(button_frame, text="Convert", command=convert)
convert_btn.grid(row=0, column=0, padx=5)

clear_btn = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_btn.grid(row=0, column=1, padx=5)

# Exit Button
exit_btn = ttk.Button(root, text="Exit", command=quit_app)
exit_btn.pack(pady=6)

# Result
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=6)

# Theme toggle button (full width)
theme_frame = tk.Frame(root, bg=root["bg"])
theme_frame.pack(pady=10)

theme_btn = tk.Button(
    theme_frame,
    text="🌙  Dark  /  ☀️  Light",
    command=toggle_theme,
    width=25,
    relief="raised",
    pady=15,
)
theme_btn.pack()

root.mainloop()
