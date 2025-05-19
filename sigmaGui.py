import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from fpdf import FPDF

def hitung_sigma():
    try:
        lower = int(entry_lower.get())
        upper = int(entry_upper.get())
        expr = entry_expr.get()
        sum_ai = entry_sum_ai.get()
        sum_bi = entry_sum_bi.get()

        jumlah_suku = upper - lower + 1
        langkah = ""
        total = 0

        if 'ai' in expr or 'bi' in expr:
            if sum_ai == "":
                sum_ai = 0
            if sum_bi == "":
                sum_bi = 0

            sum_ai = float(sum_ai)
            sum_bi = float(sum_bi)

            expr_mod = expr.replace('ai', f'({sum_ai})').replace('bi', f'({sum_bi})')
            expr_mod = expr_mod.replace('i', str(jumlah_suku))

            total = eval(expr_mod)
            langkah += f"Jumlah suku = {jumlah_suku}\n"
            langkah += f"Ekspresi dimodifikasi: {expr_mod}\n"
            langkah += f"Hasil: {total}\n"
        else:
            for i in range(lower, upper + 1):
                nilai = eval(expr, {"i": i})
                total += nilai
                langkah += f"i = {i}: {expr} = {nilai}\n"

        label_result.config(text=f"Hasil Sigma = {total}")
        text_steps.delete("1.0", tk.END)
        text_steps.insert(tk.END, langkah)

    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def tampilkan_grafik():
    try:
        lower = int(entry_lower.get())
        upper = int(entry_upper.get())
        expr = entry_expr.get()

        x_vals = []
        y_vals = []

        for i in range(lower, upper + 1):
            y = eval(expr, {"i": i})
            x_vals.append(i)
            y_vals.append(y)

        plt.plot(x_vals, y_vals, marker='o')
        plt.title("Grafik Ekspresi Sigma")
        plt.xlabel("i")
        plt.ylabel("f(i)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Grafik Error", str(e))

def export_pdf():
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Laporan Kalkulasi Sigma", ln=True, align='C')
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Ekspresi: {entry_expr.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Batas Bawah: {entry_lower.get()}, Batas Atas: {entry_upper.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Jumlah ∑aᵢ: {entry_sum_ai.get()} | ∑bᵢ: {entry_sum_bi.get()}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt="Langkah Perhitungan:\n" + text_steps.get("1.0", tk.END))
        pdf.ln(5)
        hasil = label_result.cget("text").replace("∑", "Sigma")
        pdf.cell(200, 10, txt=hasil, ln=True)
        pdf.output("hasil_sigma.pdf")
        messagebox.showinfo("Sukses", "Berhasil diekspor ke hasil_sigma.pdf")
    except Exception as e:
        messagebox.showerror("Export Error", str(e))

# UI Tkinter
root = tk.Tk()
root.title("Kalkulator Sigma (Σ) Dinamis")
root.geometry("660x470")
root.configure(bg="#f0f0f0")

font_label = ("Arial", 10)
font_button = ("Arial", 10, "bold")

tk.Label(root, text="Batas Bawah (i = ...):", bg="#f0f0f0", font=font_label).grid(row=0, column=0, sticky='e', pady=5)
entry_lower = tk.Entry(root)
entry_lower.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Batas Atas (i = ...):", bg="#f0f0f0", font=font_label).grid(row=1, column=0, sticky='e', pady=5)
entry_upper = tk.Entry(root)
entry_upper.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Ekspresi suku ke-i (gunakan i, ai, bi):", bg="#f0f0f0", font=font_label).grid(row=2, column=0, sticky='e', pady=5)
entry_expr = tk.Entry(root, width=40)
entry_expr.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

tk.Label(root, text="Jumlah ∑aᵢ (jika pakai ai):", bg="#f0f0f0", font=font_label).grid(row=3, column=0, sticky='e', pady=5)
entry_sum_ai = tk.Entry(root)
entry_sum_ai.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Jumlah ∑bᵢ (jika pakai bi):", bg="#f0f0f0", font=font_label).grid(row=4, column=0, sticky='e', pady=5)
entry_sum_bi = tk.Entry(root)
entry_sum_bi.grid(row=4, column=1, padx=5, pady=5)

tk.Button(root, text="Hitung Sigma", font=font_button, bg='green', fg='white', command=hitung_sigma).grid(row=5, column=0, pady=10)
tk.Button(root, text="Tampilkan Grafik", font=font_button, bg='orange', command=tampilkan_grafik).grid(row=5, column=1)
tk.Button(root, text="Export ke PDF", font=font_button, bg='blue', fg='white', command=export_pdf).grid(row=5, column=2, padx=5)

tk.Label(root, text="Langkah Penyelesaian:", bg="#f0f0f0", font=font_label).grid(row=6, column=0, columnspan=3, pady=5)
text_steps = tk.Text(root, height=10, width=80)
text_steps.grid(row=7, column=0, columnspan=3, padx=10)

label_result = tk.Label(root, text="Hasil Sigma = ...", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_result.grid(row=8, column=0, columnspan=3, pady=10)

root.mainloop()
