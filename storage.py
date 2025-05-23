from pathlib import Path
import json

DATA_FILE = Path("data/keuangan.json")

def load_data():
    if not DATA_FILE.exists():
        return []
    try:
        content = DATA_FILE.read_text().strip()
        if not content:
            return []
        data = json.loads(content)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError as e:
        print(f"[ERROR] Gagal load JSON: {e}")
        return []

def backup_data():
    if DATA_FILE.exists():
        backup_path = DATA_FILE.with_suffix(".bak.json")
        DATA_FILE.replace(backup_path)

def save_data(data):
    backup_data()
    DATA_FILE.write_text(json.dumps(data, indent=4))
