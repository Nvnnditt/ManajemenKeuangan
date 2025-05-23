import json, os

DATA_FILE = "keuangan.json"

def load_data():
    # Jika file belum ada → kembalikan list kosong
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:          # file kosong
                return []
            return json.loads(content)
    except json.JSONDecodeError:     # file rusak/format salah
        # Bisa pilih: return [] atau raise error + pesan
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
