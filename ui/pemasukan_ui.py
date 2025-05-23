import tkinter as tk
from tkinter import ttk, messagebox
from models import tambah_transaksi
from storage import save_data

class PemasukanView(tk.Frame):
    def __init__(self, master, data, *args, **kwargs):
        super().__init__(master, bg="#f9f9f9", *args, **kwargs)
        self.data = data

        tk.Label(self, text="Input Pemasukan", font=("Segoe UI", 18, "bold"), bg="#f9f9f9", fg="#2c3e50").pack(pady=15)

        form_frame = tk.Frame(self, bg="#f9f9f9")
        form_frame.pack(anchor="w", padx=30, pady=5)

        # --- Kategori ---
        tk.Label(form_frame, text="Kategori:", bg="#f9f9f9", fg="#2c3e50", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.kategori_var = tk.StringVar()
        self.kategori_entry = ttk.Combobox(form_frame, textvariable=self.kategori_var, width=30)
        self.kategori_entry['values'] = self.get_kategori_list()
        self.kategori_entry.grid(row=0, column=1, padx=10, pady=5)

        # --- Jumlah ---
        tk.Label(form_frame, text="Jumlah (Rp):", bg="#f9f9f9", fg="#2c3e50", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.jumlah_entry = tk.Entry(form_frame, width=33)
        self.jumlah_entry.grid(row=1, column=1, padx=10, pady=5)

        # --- Tombol Simpan ---
        simpan_btn = tk.Button(self, text="Simpan", bg="#1abc9c", fg="white",
                               font=("Segoe UI", 11, "bold"), command=self.simpan)
        simpan_btn.pack(pady=10)

        # --- Tabel Transaksi Pemasukan ---
        self.tree = ttk.Treeview(self, columns=("Tanggal", "Kategori", "Jumlah"), show="headings")
        self.tree.heading("Tanggal", text="Tanggal")
        self.tree.heading("Kategori", text="Kategori")
        self.tree.heading("Jumlah", text="Jumlah (Rp)")
        self.tree.column("Tanggal", width=100)
        self.tree.column("Kategori", width=150)
        self.tree.column("Jumlah", width=120)
        self.tree.pack(padx=30, pady=15, fill=tk.X)

        self.refresh_table()

    def get_kategori_list(self):
        kategori = list({d['kategori'] for d in self.data if d['jenis'] == "Pemasukan"})
        return kategori or ["Gaji", "Bonus", "Jual Item Game"]

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for d in self.data:
            if d['jenis'] == "Pemasukan":
                self.tree.insert("", "end", values=(d["tanggal"], d["kategori"], f"Rp {d['jumlah']:,}"))

    def simpan(self):
        kategori = self.kategori_var.get()
        jumlah = self.jumlah_entry.get()

        if not jumlah.isdigit():
            messagebox.showerror("Error", "Jumlah harus angka.")
            return

        tambah_transaksi(self.data, kategori, "Pemasukan", jumlah)
        save_data(self.data)
        messagebox.showinfo("Sukses", "Pemasukan berhasil ditambahkan!")

        self.kategori_var.set("")
        self.jumlah_entry.delete(0, tk.END)
        self.refresh_table()
