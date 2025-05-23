# main.py
import tkinter as tk
from ui.history_ui import HistoryView
from storage import load_data

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manajemen Keuangan")
        self.geometry("800x500")
        self.configure(bg="#f0f2f5")  # warna background abu muda

        self.data = load_data()

        # Frame Sidebar
        sidebar = tk.Frame(self, width=150, bg="#2c3e50")
        sidebar.pack(side="left", fill="y")

        # Frame Konten
        self.content = tk.Frame(self, bg="white")
        self.content.pack(side="right", fill="both", expand=True)

        tk.Label(
            sidebar,
            text="Menu",
            bg="#2c3e50",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            pady=20
        ).pack()

        # Tombol navigasi
        buttons = [
            ("History", self.show_history),
            ("Pemasukan", self.show_dummy),
            ("Pengeluaran", self.show_dummy),
            ("Bagan", self.show_dummy),
            ("Kalkulator", self.show_dummy),
        ]

        # Ganti bagian loop tombol navigasi:
        for text, command in buttons:
            btn = tk.Button(
                sidebar,
                text=text,
                fg="white",
                bg="#34495e",
                activebackground="#1abc9c",
                relief="flat",
                font=("Segoe UI", 12, "bold"),
                padx=10,
                pady=10,
                anchor="w",  # align ke kiri
                command=command
            )
            btn.pack(fill="x", pady=6, padx=10)


        # Tampilkan default
        self.show_history()

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_history(self):
        self.clear_content()
        view = HistoryView(self.content, self.data)
        view.pack(fill="both", expand=True)

    def show_dummy(self):
        self.clear_content()
        label = tk.Label(self.content, text="Fitur belum tersedia 🛠️", font=("Arial", 20), bg="white")
        label.pack(pady=100)

if __name__ == "__main__":
    app = App()
    app.mainloop()
