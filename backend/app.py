import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =====================================================================
# DILARANG MENGUBAH ATAU MENG-HARDCODE BAGIAN INI!
# =====================================================================
# Sistem akan otomatis membaca Environment Variables dari Azure ACI.
# Jika kalian menulis nama langsung di sini, nilai otomatis dipotong.
nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Misterius')
nim_owner = os.environ.get('NIM_PRAKTIKAN', '00000000')

# Data Katalog
katalog_data = [
    {"id": 1, "nama": "MAD68 Magnetic Keyboard", "kategori": "Peripherals", "spek": "Rapid Trigger, Hall Effect", "stok": 5},
    {"id": 2, "nama": "Truthear Zero: Red", "kategori": "Audio", "spek": "Dual Dynamic Driver IEM", "stok": 3},
    {"id": 3, "nama": "Lenovo LOQ Cooler Stand", "kategori": "Accessories", "spek": "High Airflow, Dual Fan", "stok": 10}
]

@app.route('/api/katalog')
def get_katalog():
    # PERBAIKAN: Nama variabel di sini harus SAMA dengan yang di atas
    return jsonify({
        "nama": nama_owner,
        "nim": nim_owner,
        "katalog": katalog_data
    })

if __name__ == '__main__':
    # host='0.0.0.0' wajib agar bisa diakses dari luar kontainer
    app.run(host='0.0.0.0', port=5000)