import tkinter as tk
from tkinter import ttk, messagebox
from models import tambah_transaksi, hitung_saldo
from storage import save_data

def build_ui(root, data):
    saldo_var = tk.StringVar()

    def refresh_ui():
        for row in tree.get_children():
            tree.delete(row)
        for d in data:
            tree.insert("", "end", values=(d["tanggal"], d["kategori"], d["jenis"], d["jumlah"]))
        saldo_var.set(f"Rp {hitung_saldo(data):,}")

    def on_submit():
        kategori = kategori_entry.get()
        jenis = jenis_var.get()
        jumlah = jumlah_entry.get()
        if not jumlah.isdigit():
            messagebox.showerror("Error", "Jumlah harus angka")
            return
        tambah_transaksi(data, kategori, jenis, jumlah)
        save_data(data)
        refresh_ui()
        jumlah_entry.delete(0, tk.END)

    # Form input
    form = tk.Frame(root)
    form.pack(pady=10)

    kategori_entry = tk.Entry(form)
    kategori_entry.grid(row=0, column=0)
    jenis_var = tk.StringVar(value="Pemasukan")
    jenis_box = ttk.Combobox(form, textvariable=jenis_var, values=["Pemasukan", "Pengeluaran"])
    jenis_box.grid(row=0, column=1)
    jumlah_entry = tk.Entry(form, width=10)
    jumlah_entry.grid(row=0, column=2)
    tk.Button(form, text="Tambah", command=on_submit).grid(row=0, column=3)

    # Tabel transaksi
    columns = ("Tanggal", "Kategori", "Jenis", "Jumlah")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(pady=10, fill=tk.X)

    # Label saldo
    tk.Label(root, text="Saldo:", font=("Arial", 12)).pack()
    tk.Label(root, textvariable=saldo_var, font=("Arial", 16, "bold")).pack()

    refresh_ui()
