from datetime import datetime

def tambah_transaksi(data, kategori, jenis, jumlah):
    transaksi = {
        "tanggal": datetime.now().strftime("%Y-%m-%d"),
        "kategori": kategori.strip().title(),
        "jenis": jenis.title(),
        "jumlah": int(jumlah)
    }
    data.append(transaksi)
    return transaksi

def hitung_saldo(data):
    return sum(d["jumlah"] if d["jenis"] == "Pemasukan" else -d["jumlah"] for d in data)

def get_kategori(data, jenis="Pemasukan"):
    return sorted(list({d["kategori"] for d in data if d["jenis"] == jenis}))
