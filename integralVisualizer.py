import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Integral Visualizer")
root.geometry("800x600")
root.configure(bg="#f0f4f8")

x = sp.Symbol('x')

def hitung_integral():
    for widget in frame_hasil.winfo_children():
        widget.destroy()

    fungsi_input = entry_fungsi.get()
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Error", "Batas bawah dan atas harus berupa angka.")
        return

    try:
        fungsi = sp.sympify(fungsi_input)
    except sp.SympifyError:
        messagebox.showerror("Error", "Fungsi tidak valid.")
        return

    integral = sp.integrate(fungsi, (x, a, b))
    hasil = f"Hasil Integral ∫ {fungsi_input} dx dari {a} ke {b} = {float(integral):.3f}"

    tk.Label(frame_hasil, text=hasil, font=("Arial", 14), bg="#f0f4f8").pack(pady=5)

    f_lambdified = sp.lambdify(x, fungsi, modules=['numpy'])
    x_vals = np.linspace(a, b, 400)
    y_vals = f_lambdified(x_vals)

    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=100)
    ax.plot(x_vals, y_vals, label=f"f(x) = {fungsi_input}")
    ax.fill_between(x_vals, y_vals, alpha=0.3)
    ax.set_title("Area di bawah kurva f(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=frame_hasil)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    langkah = f"""
1. Ambil fungsi f(x) = {fungsi_input}
2. Hitung integral tentu dari {a} ke {b}
3. Gunakan aturan kalkulus untuk mendapatkan nilai luas
4. Gambarkan grafik f(x) dan arsiran area integral
"""
    tk.Label(frame_hasil, text=langkah, justify="left", bg="#f0f4f8", font=("Courier", 10)).pack()

frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=20)

tk.Label(frame_input, text="Masukkan fungsi f(x):", bg="#f0f4f8").grid(row=0, column=0, sticky="e")
entry_fungsi = tk.Entry(frame_input, width=30)
entry_fungsi.grid(row=0, column=1)

tk.Label(frame_input, text="Batas bawah (a):", bg="#f0f4f8").grid(row=1, column=0, sticky="e")
entry_a = tk.Entry(frame_input, width=10)
entry_a.grid(row=1, column=1, sticky="w")

tk.Label(frame_input, text="Batas atas (b):", bg="#f0f4f8").grid(row=2, column=0, sticky="e")
entry_b = tk.Entry(frame_input, width=10)
entry_b.grid(row=2, column=1, sticky="w")

tk.Button(frame_input, text="Hitung Integral", command=hitung_integral, bg="#2196F3", fg="white", font=("Arial", 11, "bold")).grid(row=3, columnspan=2, pady=10)

frame_hasil = tk.Frame(root, bg="#f0f4f8")
frame_hasil.pack(fill="both", expand=True)

root.mainloop()
