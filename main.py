from tkinter import Tk
from ui import build_ui
from storage import load_data

if __name__ == "__main__":
    root = Tk()
    root.title("Aplikasi Keuangan Pribadi")
    data = load_data()
    build_ui(root, data)
    root.mainloop()
