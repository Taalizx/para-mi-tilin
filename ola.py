import tkinter as tk
from tkinter import messagebox

def open_letter():
    messagebox.showinfo("Para mi tilin uwu", "Ola DAVID SEBASTIAN DUARTE SERNA \n\n SJAKSJAKSJ \n\n te quiero muchote eres muy hermoso david demasiado me encantas \n\n mi tilin \n\n el cerro de mi escalera \n\n mi corazon de melon \n\n ❤️")

def reset():
    canvas.itemconfig(letter, state='hidden')
    canvas.itemconfig(cover, state='normal')

def reveal():
    canvas.itemconfig(letter, state='normal')
    canvas.itemconfig(cover, state='hidden')
    open_letter()

# Configuración de la ventana
root = tk.Tk()
root.title("Carta de Amor")
root.geometry("400x400")
root.configure(bg='#fde2e4')

canvas = tk.Canvas(root, width=400, height=300, bg='#fde2e4', highlightthickness=0)
canvas.pack()

# Dibujar la carta
cover = canvas.create_polygon(100, 150, 300, 150, 200, 50, fill='#ffb6c1', outline='black')
letter = canvas.create_rectangle(120, 150, 280, 250, fill='white', outline='black', state='hidden')

tk.Button(root, text="Abrir 💌", command=reveal, bg='#ff99c8', fg='white').pack(pady=10)
tk.Button(root, text="Reset", command=reset, bg='#d8a7b1', fg='white').pack()

root.mainloop()
