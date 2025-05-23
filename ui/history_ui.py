import tkinter as tk
from tkinter import ttk
from models import hitung_saldo

class HistoryView(tk.Frame):
    def __init__(self, master, data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.data = data
        self.saldo_var = tk.StringVar()
        
        style = ttk.Style()
        style.configure("Treeview", background="#ecf0f1", fieldbackground="#ecf0f1", foreground="black")
        style.map("Treeview", background=[("selected", "#1abc9c")])
        # Label saldo
        tk.Label(self, text="Saldo:", font=("Arial", 12)).pack()
        tk.Label(self, textvariable=self.saldo_var, font=("Arial", 16, "bold")).pack()
        # Tabel transaksi
        columns = ("Tanggal", "Kategori", "Jenis", "Jumlah")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill=tk.X)

        self.refresh_ui()

    def refresh_ui(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for d in self.data:
            self.tree.insert("", "end", values=(d["tanggal"], d["kategori"], d["jenis"], d["jumlah"]))
        self.saldo_var.set(f"Rp {hitung_saldo(self.data):,}")
