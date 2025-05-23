def tambah_transaksi(data, kategori, jenis, jumlah):
    from datetime import datetime
    transaksi = {
        "tanggal": datetime.now().strftime("%Y-%m-%d"),
        "kategori": kategori,
        "jenis": jenis,
        "jumlah": int(jumlah)
    }
    data.append(transaksi)
    return data

def hitung_saldo(data):
    saldo = 0
    for d in data:
        saldo += d["jumlah"] if d["jenis"] == "Pemasukan" else -d["jumlah"]
    return saldo
